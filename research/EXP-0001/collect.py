"""EXP-0001: bounded public-data collection. Does not score or print labels."""
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import pathlib
import re
import threading
import time
import urllib.parse
from zoneinfo import ZoneInfo
import requests

ROOT = pathlib.Path(__file__).resolve().parent
RAW = ROOT / "raw"
RAW.mkdir(exist_ok=True)
BASE = "https://external-api.kalshi.com/trade-api/v2"
START, END = dt.date(2025, 7, 1), dt.date(2026, 6, 30)
NY = ZoneInfo("America/New_York")
MONTHS = {s: i + 1 for i, s in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}
rate_lock, log_lock = threading.Lock(), threading.Lock()
next_request = 0.0
local = threading.local()

def event_date(ticker):
    m = re.fullmatch(r"KXHIGHNY-(\d{2})([A-Z]{3})(\d{2})", ticker)
    if not m: return None
    return dt.date(2000 + int(m[1]), MONTHS[m[2]], int(m[3]))

def fetch(path, name):
    global next_request
    dest = RAW / (name + ".json")
    if dest.exists(): return json.loads(dest.read_bytes())
    url = BASE + path
    if not hasattr(local, "session"): local.session = requests.Session()
    for attempt in range(4):
        with rate_lock:
            now = time.monotonic()
            delay = max(0, next_request - now)
            next_request = max(now, next_request) + .25
        if delay: time.sleep(delay)
        began = dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            r = local.session.get(url, timeout=25)
            if r.status_code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** (attempt + 1)); continue
            r.raise_for_status()
            data = r.json()
            dest.write_bytes(r.content)
            entry = {"file": dest.name, "url": url, "retrieved_at_utc": began,
                     "sha256": hashlib.sha256(r.content).hexdigest(), "bytes": len(r.content)}
            with log_lock:
                with (ROOT / "request-manifest.jsonl").open("a", encoding="utf-8") as f:
                    f.write(json.dumps(entry) + "\n")
            return data
        except Exception as e:
            if attempt < 3:
                time.sleep(2 ** (attempt + 1)); continue
            with log_lock:
                with (ROOT / "request-errors.jsonl").open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"url": url, "time": began, "error": str(e)}) + "\n")
            return {"collection_error": str(e)}

def cutoff(day):
    decision = dt.datetime.combine(day - dt.timedelta(days=1), dt.time(12), NY)
    return int(decision.timestamp())

def main():
    fetch("/historical/cutoff", "cutoff")
    markets, cursor, page, cursors = [], "", 0, set()
    while True:
        params = {"series_ticker": "KXHIGHNY", "limit": 1000}
        if cursor: params["cursor"] = cursor
        d = fetch("/historical/markets?" + urllib.parse.urlencode(params), f"markets-{page:03d}")
        if "collection_error" in d: raise RuntimeError("Metadata collection failed")
        markets.extend(d["markets"])
        cursor = d.get("cursor", "")
        print(json.dumps({"metadata_page": page, "records": len(d["markets"])}), flush=True)
        if not cursor: break
        if cursor in cursors: raise RuntimeError("Repeated metadata cursor")
        cursors.add(cursor); page += 1
        if page > 50: raise RuntimeError("Metadata page bound exceeded")
    selected = []
    for m in markets:
        day = event_date(m["event_ticker"])
        if day and START <= day <= END: selected.append(m)
    if len({m["ticker"] for m in selected}) != len(selected):
        raise RuntimeError("Duplicate study market tickers")
    (ROOT / "markets-study.json").write_text(json.dumps(selected, indent=2), encoding="utf-8")
    print(json.dumps({"study_markets": len(selected), "event_dates": len({m['event_ticker'] for m in selected}),
                      "labels_printed": False}), flush=True)
    def one(m):
        t = cutoff(event_date(m["event_ticker"]))
        params = {"start_ts": t - 1800, "end_ts": t - 60, "period_interval": 1}
        path = "/historical/markets/" + urllib.parse.quote(m["ticker"], safe="") + "/candlesticks?" + urllib.parse.urlencode(params)
        d = fetch(path, "candles-" + m["ticker"])
        return "collection_error" not in d
    okay = 0
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        for done, good in enumerate(pool.map(one, selected), 1):
            okay += good
            if done % 100 == 0 or done == len(selected):
                print(json.dumps({"candles_completed": done, "total": len(selected), "responses_ok": okay}), flush=True)
    print(json.dumps({"collection_complete": True, "responses_ok": okay, "requested": len(selected)}), flush=True)

if __name__ == "__main__": main()
