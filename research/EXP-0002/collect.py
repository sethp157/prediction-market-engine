"""EXP-0002 public-source collection only; no scoring or settlement-label output.

Run --selfcheck without network, then run without arguments to collect/resume.
One process owns this directory. Successful responses are immutable and every
response, including HTTP errors, has an exact URL, request start, and SHA-256.
"""
import argparse
import concurrent.futures as cf
import contextlib
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import threading
import time
import urllib.parse
from zoneinfo import ZoneInfo

import requests

ROOT = pathlib.Path(__file__).resolve().parent
RAW = ROOT / "raw"
BASE = "https://external-api.kalshi.com/trade-api/v2"
MOS_BASE = "https://mesonet.agron.iastate.edu/api/1/mos.json"
START, END = dt.date(2025, 7, 1), dt.date(2026, 6, 30)
NY = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
MONTHS = {s: i + 1 for i, s in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def emit(**item):
    print(json.dumps(item), flush=True)


def event_date(ticker):
    match = re.fullmatch(r"KXHIGHMIA-(\d{2})([A-Z]{3})(\d{2})", ticker)
    if not match or match[2] not in MONTHS:
        return None
    return dt.date(2000 + int(match[1]), MONTHS[match[2]], int(match[3]))


def cutoff(day):
    return int(dt.datetime.combine(day - dt.timedelta(days=1), dt.time(12), NY).timestamp())


def mos_runtime(day):
    return dt.datetime.combine(day - dt.timedelta(days=1), dt.time(6), UTC)


def mos_url(runtime):
    if runtime.tzinfo is None or runtime.utcoffset() != dt.timedelta(0):
        raise ValueError("MOS runtime must be explicitly UTC")
    return MOS_BASE + "?" + urllib.parse.urlencode({
        "station": "KMIA", "runtime": runtime.strftime("%Y-%m-%dT%H:%MZ"), "model": "GFS"
    })


def mos_filename(day):
    return "mos-KMIA-GFS-" + mos_runtime(day).strftime("%Y%m%d%H") + ".json"


def target_days():
    return [START + dt.timedelta(days=i) for i in range((END - START).days + 1)]


def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False), encoding="utf-8")
    os.replace(temporary, path)


@contextlib.contextmanager
def process_lock():
    """OS lock is released even after an abrupt process exit; never trust stale PID."""
    lock_path = ROOT / "collector.lock"
    with lock_path.open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if not handle.tell():
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as exc:
                raise RuntimeError("Another collector owns research2") from exc
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


class Limiter:
    def __init__(self, interval):
        self.interval, self.previous, self.lock = interval, 0.0, threading.Lock()

    def get(self, session, url):
        # Holding the host lock through the GET prevents queued starts bunching.
        with self.lock:
            time.sleep(max(0.0, self.previous + self.interval - time.monotonic()))
            self.previous = time.monotonic()
            began = dt.datetime.now(UTC).isoformat()
            try:
                return began, session.get(url, timeout=(15, 40))
            except requests.RequestException as exc:
                exc.request_started_at_utc = began
                raise


class Collector:
    def __init__(self):
        RAW.mkdir(exist_ok=True)
        self.entries = {}
        self.log_lock = threading.Lock()
        self.local = threading.local()
        self.limiters = {"kalshi": Limiter(.26), "iem": Limiter(1.01)}
        manifest = ROOT / "request-manifest.jsonl"
        if manifest.exists():
            for line in manifest.read_text(encoding="utf-8").splitlines():
                entry = json.loads(line)
                if entry["file"] in self.entries:
                    raise RuntimeError("Duplicate provenance filename: " + entry["file"])
                self.entries[entry["file"]] = entry
        self.verify_cache()

    def verify_cache(self):
        for name, entry in self.entries.items():
            path = RAW / name
            if not path.resolve().is_relative_to(RAW.resolve()):
                raise RuntimeError("Manifest file escapes raw directory")
            if not path.is_file():
                raise RuntimeError("Manifest response is missing: " + name)
            body = path.read_bytes()
            if len(body) != entry["bytes"] or hashlib.sha256(body).hexdigest() != entry["sha256"]:
                raise RuntimeError("Cached response provenance mismatch: " + name)
            stamp = dt.datetime.fromisoformat(entry["request_started_at_utc"])
            if stamp.utcoffset() != dt.timedelta(0):
                raise RuntimeError("Request-start timestamp is not UTC")
        for path in RAW.rglob("*"):
            if path.is_file() and path.suffix != ".part":
                if path.relative_to(RAW).as_posix() not in self.entries:
                    raise RuntimeError("Unmanifested raw response; refusing silent reuse: " + path.name)

    def record_response(self, name, url, began, response):
        body = response.content
        entry = {"file": name, "url": url, "request_started_at_utc": began,
                 "retrieved_at_utc": began, "response_received_at_utc": dt.datetime.now(UTC).isoformat(),
                 "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
                 "status_code": response.status_code}
        with self.log_lock:
            if name in self.entries or (RAW / name).exists():
                raise RuntimeError("Refusing to overwrite raw response: " + name)
            dest = RAW / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            temporary = dest.with_suffix(dest.suffix + ".part")
            temporary.write_bytes(body)
            os.replace(temporary, dest)
            with (ROOT / "request-manifest.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(entry) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
            self.entries[name] = entry

    def fetch(self, url, name, host):
        if name in self.entries:
            entry = self.entries[name]
            if entry["url"] != url or entry["status_code"] != 200:
                raise RuntimeError("Cached URL/status mismatch: " + name)
            return json.loads((RAW / name).read_bytes())
        if not hasattr(self.local, "session"):
            self.local.session = requests.Session()
            self.local.session.headers["User-Agent"] = "EXP-0002-public-research/1.0 (bounded archival GET collection)"
        last_error = None
        for attempt in range(4):
            began = dt.datetime.now(UTC).isoformat()
            try:
                began, response = self.limiters[host].get(self.local.session, url)
                try:
                    data = response.json()
                    valid = response.status_code == 200 and isinstance(data, dict)
                except ValueError:
                    data, valid = None, False
                if valid:
                    self.record_response(name, url, began, response)
                    return data
                stamp = dt.datetime.now(UTC).strftime("%Y%m%dT%H%M%S%f")
                error_name = "errors/" + name.removesuffix(".json") + f"-{stamp}-a{attempt}.body"
                self.record_response(error_name, url, began, response)
                last_error = "HTTP " + str(response.status_code) + "; expected a JSON object"
                if response.status_code not in (429, 500, 502, 503, 504):
                    break
            except requests.RequestException as exc:
                began = getattr(exc, "request_started_at_utc", began)
                last_error = type(exc).__name__ + ": " + str(exc)
            with self.log_lock:
                with (ROOT / "request-errors.jsonl").open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps({"url": url, "file": name, "request_started_at_utc": began,
                                             "attempt": attempt + 1, "error": last_error}) + "\n")
            if attempt < 3:
                time.sleep(2 ** (attempt + 1))
        return {"collection_error": last_error}

    def collect_mos(self):
        rows, okay = [], 0
        for done, day in enumerate(target_days(), 1):
            runtime = mos_runtime(day)
            name = mos_filename(day)
            data = self.fetch(mos_url(runtime), name, "iem")
            good = "collection_error" not in data
            okay += good
            rows.append({"target_date": day.isoformat(), "station": "KMIA", "model": "GFS",
                         "runtime_utc": runtime.isoformat(),
                         "required_ftime_utc": (runtime + dt.timedelta(hours=42)).isoformat(),
                         "assumed_available_utc": (runtime + dt.timedelta(hours=6)).isoformat(),
                         "raw_file": name, "response_ok": good})
            if done % 25 == 0 or done == 365:
                emit(mos_completed=done, total=365, responses_ok=okay, labels_printed=False)
        atomic_json(ROOT / "mos-study.json", rows)
        return {"requested": len(rows), "responses_ok": okay}

    def collect_markets(self):
        cutoff_data = self.fetch(BASE + "/historical/cutoff", "cutoff.json", "kalshi")
        if "collection_error" in cutoff_data:
            raise RuntimeError("Historical cutoff collection failed")
        markets, cursor, page, cursors = [], "", 0, set()
        while True:
            params = {"series_ticker": "KXHIGHMIA", "limit": 1000}
            if cursor:
                params["cursor"] = cursor
            url = BASE + "/historical/markets?" + urllib.parse.urlencode(params)
            data = self.fetch(url, f"markets-{page:03d}.json", "kalshi")
            if "collection_error" in data or not isinstance(data.get("markets"), list):
                raise RuntimeError("Metadata collection failed")
            markets.extend(data["markets"])
            cursor = data.get("cursor", "")
            emit(metadata_page=page, records=len(data["markets"]), labels_printed=False)
            if not cursor:
                break
            if cursor in cursors:
                raise RuntimeError("Repeated metadata cursor")
            cursors.add(cursor)
            page += 1
            if page > 50:
                raise RuntimeError("Metadata page bound exceeded")
        selected = [m for m in markets if (day := event_date(m["event_ticker"])) and START <= day <= END]
        if len({m["ticker"] for m in selected}) != len(selected):
            raise RuntimeError("Duplicate study market tickers")
        atomic_json(ROOT / "markets-study.json", selected)
        emit(study_markets=len(selected), event_dates=len({m["event_ticker"] for m in selected}), labels_printed=False)

        def one(market):
            t = cutoff(event_date(market["event_ticker"]))
            params = {"start_ts": t - 1800, "end_ts": t - 60, "period_interval": 1}
            url = BASE + "/historical/markets/" + urllib.parse.quote(market["ticker"], safe="")
            url += "/candlesticks?" + urllib.parse.urlencode(params)
            data = self.fetch(url, "candles-" + market["ticker"] + ".json", "kalshi")
            return "collection_error" not in data

        okay = 0
        with cf.ThreadPoolExecutor(max_workers=4) as pool:
            for done, good in enumerate(pool.map(one, selected), 1):
                okay += good
                if done % 100 == 0 or done == len(selected):
                    emit(candles_completed=done, total=len(selected), responses_ok=okay, labels_printed=False)
        return {"requested": len(selected), "responses_ok": okay}


def selfcheck():
    frozen = json.loads((ROOT / "protocol-freeze.json").read_text(encoding="utf-8-sig"))
    if hashlib.sha256((ROOT / "protocol.md").read_bytes()).hexdigest().upper() != frozen["sha256"].upper():
        raise RuntimeError("Frozen protocol hash mismatch")
    assert len(target_days()) == 365 and len(set(target_days())) == 365
    assert event_date("KXHIGHMIA-25JUL01") == START
    assert event_date("KXHIGHNY-25JUL01") is None
    assert dt.datetime.fromtimestamp(cutoff(START), UTC).isoformat() == "2025-06-30T16:00:00+00:00"
    assert dt.datetime.fromtimestamp(cutoff(dt.date(2026, 1, 1)), UTC).hour == 17
    for day in target_days():
        runtime = mos_runtime(day)
        assert (runtime + dt.timedelta(hours=42)).date() == day + dt.timedelta(days=1)
        assert (runtime + dt.timedelta(hours=42)).hour == 0
        assert (runtime + dt.timedelta(hours=6)).timestamp() < cutoff(day)
        assert urllib.parse.parse_qs(urllib.parse.urlparse(mos_url(runtime)).query) == {
            "station": ["KMIA"], "runtime": [runtime.strftime("%Y-%m-%dT%H:%MZ")], "model": ["GFS"]}
    assert ROOT.name == "research2"
    emit(integrity_selfcheck="passed", expected_dates=365, protocol_sha256=frozen["sha256"], network_used=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selfcheck", action="store_true", help="Check frozen protocol and request construction; no network")
    args = parser.parse_args()
    selfcheck()
    if args.selfcheck:
        return
    with process_lock():
        collector = Collector()
        emit(collection_started_at_utc=dt.datetime.now(UTC).isoformat(), cached_responses=len(collector.entries))
        with cf.ThreadPoolExecutor(max_workers=2) as pool:
            mos = pool.submit(collector.collect_mos)
            markets = pool.submit(collector.collect_markets)
            results = {"mos": mos.result(), "candles": markets.result()}
        collector.verify_cache()
        results.update(collection_complete=all(x["requested"] == x["responses_ok"] for x in results.values()),
                       raw_responses_verified=len(collector.entries),
                       completed_at_utc=dt.datetime.now(UTC).isoformat(), labels_printed=False)
        atomic_json(ROOT / "collection-summary.json", results)
        emit(**results)


if __name__ == "__main__":
    main()
