"""One-off EXP-0001 analysis. prepare exposes training/validation only; evaluate exposes tests."""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import json
import math
import pathlib
import urllib.parse
from zoneinfo import ZoneInfo
import numpy as np
from collect import event_date, cutoff, BASE

ROOT = pathlib.Path(__file__).resolve().parent
NY = ZoneInfo("America/New_York")
START, END = dt.date(2025, 7, 1), dt.date(2026, 6, 30)
GRID = [.5, .75, 1., 1.25, 1.5, 1.75, 2.]
TRAIN_LABEL_CUTOFF = cutoff(dt.date(2025, 11, 1))
PROTOCOL = ROOT / "protocol.md"
AMENDMENTS = ROOT / "amendments.md"

def load(name): return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))
def save(name, obj): (ROOT / name).write_text(json.dumps(obj, indent=2, allow_nan=False), encoding="utf-8")
def iso_ts(s):
    if not isinstance(s,str) or not s: raise ValueError("Missing timestamp")
    parsed=dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None: raise ValueError("Timestamp lacks timezone")
    return parsed.timestamp()
def split(day):
    if day < dt.date(2025,11,1): return "train"
    if day < dt.date(2026,1,1): return "validation"
    if day < dt.date(2026,4,1): return "test_a"
    return "test_b"
def calibrate(r, beta):
    x = np.asarray(r, dtype=float) ** beta
    return x / x.sum()
def score(p, y): return float(np.mean((np.asarray(p) - np.asarray(y)) ** 2))

def verify_inputs():
    entries={}
    for line in (ROOT/"request-manifest.jsonl").read_text(encoding="utf-8").splitlines():
        item=json.loads(line)
        if item["file"] in entries and item!=entries[item["file"]]:
            raise RuntimeError("Conflicting provenance entries")
        entries[item["file"]]=item
    rawfiles=list((ROOT/"raw").glob("*.json"))
    for path in rawfiles:
        if path.name not in entries: raise RuntimeError("Raw file without provenance: "+path.name)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=entries[path.name]["sha256"]:
            raise RuntimeError("Raw hash mismatch: "+path.name)
    allmarkets=[]; previous_cursor=""
    pages=sorted((ROOT/"raw").glob("markets-*.json"))
    for page,path in enumerate(pages):
        if path.name!=f"markets-{page:03d}.json": raise RuntimeError("Metadata page sequence gap")
        params={"series_ticker":"KXHIGHNY","limit":1000}
        if previous_cursor: params["cursor"]=previous_cursor
        if entries[path.name]["url"]!=BASE+"/historical/markets?"+urllib.parse.urlencode(params):
            raise RuntimeError("Unexpected metadata URL")
        d=json.loads(path.read_bytes()); allmarkets.extend(d["markets"]); previous_cursor=d.get("cursor","")
    if previous_cursor: raise RuntimeError("Metadata pagination incomplete")
    selected=[m for m in allmarkets if event_date(m["event_ticker"]) and START<=event_date(m["event_ticker"])<=END]
    if selected!=load("markets-study.json"): raise RuntimeError("Derived study metadata differs from verified source")
    expected_candles=set()
    for m in selected:
        name="candles-"+m["ticker"]+".json"; expected_candles.add(name)
        if not (ROOT/"raw"/name).exists(): continue
        t=cutoff(event_date(m["event_ticker"]))
        params={"start_ts":t-1800,"end_ts":t-60,"period_interval":1}
        expected=BASE+"/historical/markets/"+urllib.parse.quote(m["ticker"],safe="")+"/candlesticks?"+urllib.parse.urlencode(params)
        if entries[name]["url"]!=expected: raise RuntimeError("Unexpected candle URL: "+name)
    if set(p.name for p in (ROOT/"raw").glob("candles-*.json"))-expected_candles:
        raise RuntimeError("Unexpected candle file outside study")
    if entries["cutoff.json"]["url"]!=BASE+"/historical/cutoff": raise RuntimeError("Unexpected cutoff URL")
    return {"raw_files_verified":len(rawfiles),"metadata_pages_verified":len(pages),"study_metadata_matches_sources":True}

def partition_ok(ms):
    intervals=[]; lows=highs=0
    for m in ms:
        typ=m.get("strike_type"); lo=m.get("floor_strike"); hi=m.get("cap_strike")
        def integer(x): return isinstance(x,(int,float)) and math.isfinite(x) and int(x)==x
        if typ=="less" and integer(hi):
            lows+=1; intervals.append((-math.inf,int(hi)-1))
        elif typ=="greater" and integer(lo):
            highs+=1; intervals.append((int(lo)+1,math.inf))
        elif typ=="between" and integer(lo) and integer(hi) and lo<=hi:
            intervals.append((int(lo),int(hi)))
        else: return False
    intervals.sort()
    return lows==highs==1 and len(intervals)>=3 and all(a[1]+1==b[0] for a,b in zip(intervals,intervals[1:]))

def prepare():
    provenance=verify_inputs()
    if hashlib.sha256(PROTOCOL.read_bytes()).hexdigest().upper()!=load("protocol-freeze.json")["sha256"].upper():
        raise RuntimeError("Protocol differs from originally frozen bytes")
    ms=load("markets-study.json")
    groups=collections.defaultdict(list)
    for m in ms: groups[m["event_ticker"]].append(m)
    rows=[]; accepted=[]
    for offset in range((END-START).days+1):
        day=START+dt.timedelta(days=offset)
        mon="JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()[day.month-1]
        g=f"KXHIGHNY-{day.year%100:02d}{mon}{day.day:02d}"
        markets=sorted(groups.get(g,[]),key=lambda m:m["ticker"])
        t=cutoff(day)
        row={"date":day.isoformat(),"event":g,"split":split(day),"cutoff_ts":t,
             "returned_bins":len(markets),"eligible":False,"reason":""}
        reasons=[]
        if not markets: reasons.append("no_event_metadata")
        elif not partition_ok(markets): reasons.append("invalid_bin_partition")
        quotes=[]
        for m in markets:
            rules=m.get("rules_primary","").lower()
            if "central park" not in rules or "national weather service" not in rules: reasons.append("rules_mismatch")
            try:
                if max(iso_ts(m["created_time"]),iso_ts(m["open_time"]))>t: reasons.append("not_created_and_open_at_cutoff")
            except (KeyError,TypeError,ValueError): reasons.append("missing_creation_or_open_time")
            path=ROOT/"raw"/("candles-"+m["ticker"]+".json")
            if not path.exists(): reasons.append("request_failed"); continue
            d=json.loads(path.read_bytes())
            if d.get("ticker")!=m["ticker"]: reasons.append("candle_ticker_mismatch"); continue
            if not isinstance(d.get("candlesticks"),list): reasons.append("malformed_candles"); continue
            cs=[]
            for c in d["candlesticks"]:
                ts=c.get("end_period_ts") if isinstance(c,dict) else None
                if not isinstance(ts,(int,float)) or not math.isfinite(ts):
                    reasons.append("malformed_candle_timestamp"); continue
                if t-1800<=ts<=t-60: cs.append(c)
            if not cs: reasons.append("missing_candle_window"); continue
            c=max(cs,key=lambda c:c["end_period_ts"])
            try:
                bid=float(c["yes_bid"]["close"]); ask=float(c["yes_ask"]["close"])
                if not (math.isfinite(bid) and math.isfinite(ask) and 0<=bid<=ask<=1): raise ValueError()
            except (KeyError,TypeError,ValueError): reasons.append("invalid_quote"); continue
            quotes.append({"ticker":m["ticker"],"bid":bid,"ask":ask,"p_raw":(bid+ask)/2,
                           "candle_end_ts":c["end_period_ts"],"candle_age_seconds":t-c["end_period_ts"]})
        # These are mechanical label-integrity checks, not performance inspection or selection on winners.
        labels=[]
        for m in markets:
            if m.get("result") in (None,""): reasons.append("missing_label")
            elif m.get("result") in ("void","canceled","cancelled"): reasons.append("void_label")
            elif m.get("result") not in ("yes","no"): reasons.append("nonbinary_label")
            else: labels.append(int(m["result"]=="yes"))
            if m.get("status") not in ("settled","finalized"): reasons.append("not_final_status")
            try:
                settled=iso_ts(m["settlement_ts"])
                if settled<=t: reasons.append("settled_before_cutoff")
                if row["split"]=="train" and settled>=TRAIN_LABEL_CUTOFF: reasons.append("training_label_not_available")
            except (KeyError,TypeError,ValueError): reasons.append("missing_settlement_time")
        if labels and len(labels)==len(markets) and sum(labels)!=1: reasons.append("not_one_hot_settlement")
        if len(quotes)!=len(markets): reasons.append("incomplete_quotes")
        b=[q["p_raw"] for q in quotes]
        if not b or sum(b)<=0: reasons.append("zero_or_missing_mass")
        if reasons:
            row["reason"]=";".join(sorted(set(reasons)))
        else:
            row.update(eligible=True,bin_count=len(markets),raw_mass=sum(b),
                       max_candle_age=max(q["candle_age_seconds"] for q in quotes),
                       mean_spread=float(np.mean([q["ask"]-q["bid"] for q in quotes])))
            r=(np.asarray(b)/sum(b)).tolist()
            accepted.append(dict(row,quotes=quotes,y=labels,r=r,b=b))
        rows.append(row)
    save("coverage.json",rows); save("prepared-events.json",accepted)
    train=[e for e in accepted if e["split"]=="train"]
    if not train: raise RuntimeError("No eligible training events; study cannot fit")
    train_grid=[{"beta":be,"brier":float(np.mean([score(calibrate(e["r"],be),e["y"]) for e in train]))} for be in GRID]
    best=min(x["brier"] for x in train_grid)
    candidates=[x for x in train_grid if x["brier"]<=best+1e-12]
    beta=min(candidates,key=lambda x:(abs(x["beta"]-1),x["beta"]))["beta"]
    counts={}
    for s in ["train","validation","test_a","test_b"]:
        rr=[r for r in rows if r["split"]==s]
        counts[s]={"expected":len(rr),"metadata_present":sum(r["returned_bins"]>0 for r in rr),
                   "returned_contracts":sum(r["returned_bins"] for r in rr),"eligible":sum(r["eligible"] for r in rr),
                   "excluded":sum(not r["eligible"] for r in rr),
                   "reason_counts":dict(collections.Counter(reason for r in rr for reason in r["reason"].split(";") if reason))}
    reasons=collections.Counter(reason for r in rows for reason in r["reason"].split(";") if reason)
    pre={"created_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"beta":beta,"training_grid":train_grid,"provenance_checks":provenance,
         "coverage":counts,"exclusion_reason_counts":dict(reasons),
         "protocol_sha256":load("protocol-freeze.json")["sha256"],
         "script_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         "prepared_events_sha256":hashlib.sha256((ROOT/"prepared-events.json").read_bytes()).hexdigest(),
         "dependency_sha256":{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ["coverage.json","collect.py","protocol.md","amendments.md","protocol-freeze.json","request-manifest.jsonl"]},
         "test_performance_exposed":False}
    for s in ["train","validation"]:
        es=[e for e in accepted if e["split"]==s]
        pre[s+"_scores"]={k:float(np.mean([score((e["r"] if k=="market" else e["b"] if k=="raw" else [1/len(e["r"])]*len(e["r"]) if k=="uniform" else calibrate(e["r"],beta)),e["y"]) for e in es])) if es else None for k in ["market","candidate","raw","uniform"]}
    save("fit-lock.json",pre)
    print(json.dumps(pre,indent=2),flush=True)

def bootstrap(values,block,seed,reps=10000):
    a=np.asarray(values,float); n=len(a); rng=np.random.default_rng(seed)
    starts=rng.integers(0,n,size=(reps,math.ceil(n/block)))
    inds=((starts[:,:,None]+np.arange(block))%n).reshape(reps,-1)[:,:n]
    samples=a[inds]; valid_counts=np.sum(np.isfinite(samples),axis=1)
    if np.any(valid_counts==0):
        return {"lower_one_sided_95":None,"upper_one_sided_95":None,"block_days":block,"repetitions":reps,
                "finite_repetitions":int(np.sum(valid_counts>0)),"seed":seed,"status":"UNAVAILABLE_EMPTY_RESAMPLE"}
    draws=np.nansum(samples,axis=1)/valid_counts
    return {"lower_one_sided_95":float(np.quantile(draws,.05)),"upper_one_sided_95":float(np.quantile(draws,.95)),
            "block_days":block,"repetitions":reps,"finite_repetitions":len(draws),"seed":seed}

def evaluate():
    fit=load("fit-lock.json"); es=load("prepared-events.json"); cov=load("coverage.json"); beta=fit["beta"]
    if fit["script_sha256"]!=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest():
        raise RuntimeError("Script changed after fit lock; review/amend and refreeze before exposing tests")
    if fit["prepared_events_sha256"]!=hashlib.sha256((ROOT/"prepared-events.json").read_bytes()).hexdigest():
        raise RuntimeError("Prepared data changed after fit lock")
    for name,h in fit["dependency_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=h:
            raise RuntimeError("Locked dependency changed: "+name)
    if (ROOT/"results.json").exists(): raise RuntimeError("Results already exist: no second test run without exposure amendment")
    results={"evaluated_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"beta":beta,"scientific_hurdle":.001,
             "fit_lock_sha256":hashlib.sha256((ROOT/"fit-lock.json").read_bytes()).hexdigest(),"splits":{}}
    per=[]
    for e in es:
        vals={"market":score(e["r"],e["y"]),"candidate":score(calibrate(e["r"],beta),e["y"]),"raw":score(e["b"],e["y"]),"uniform":score([1/len(e["r"])]*len(e["r"]),e["y"])}
        per.append({k:e[k] for k in ["date","event","split","bin_count","raw_mass","max_candle_age","mean_spread"]}|vals|{"gain":vals["market"]-vals["candidate"]})
    for s in ["train","validation","test_a","test_b","test_pooled"]:
        ss=["test_a","test_b"] if s=="test_pooled" else [s]
        items=[x for x in per if x["split"] in ss]
        expected=[x for x in cov if x["split"] in ss]
        if not items:
            results["splits"][s]={"eligible":0,"expected":len(expected)}; continue
        res={"eligible":len(items),"expected":len(expected),"coverage":len(items)/len(expected),
             **{k:float(np.mean([x[k] for x in items])) for k in ["market","candidate","raw","uniform","gain"]}}
        if s in ["test_a","test_b","test_pooled"]:
            bydate={x["date"]:x["gain"] for x in items}
            vals=[bydate.get(x["date"],math.nan) for x in expected]
            seed={"test_a":20260918,"test_b":20260919,"test_pooled":20260920}[s]
            res["bootstrap_14"]=bootstrap(vals,14,seed)
            res["bootstrap_7_sensitivity"]=bootstrap(vals,7,seed)
        results["splits"][s]=res
    a=results["splits"]["test_a"]; b=results["splits"]["test_b"]
    minimums=(results["splits"]["train"]["eligible"]>=90 and a["eligible"]+b["eligible"]>=120
              and a["eligible"]>=50 and b["eligible"]>=50 and a.get("coverage",0)>=.7 and b.get("coverage",0)>=.7)
    passes=minimums and all(x["bootstrap_14"]["lower_one_sided_95"] is not None and x["bootstrap_14"]["lower_one_sided_95"]>.001 for x in [a,b])
    results["minimums_pass"]=minimums; results["replicated_screen_pass"]=bool(passes)
    results["strict_claim_status"]="PROMISING_REPLICATED_HISTORICAL_FORECASTING_EVIDENCE" if passes else "NOT_ESTABLISHED"
    results["quote_summary"]={"bin_counts":dict(collections.Counter(x["bin_count"] for x in per)),
        "median_event_max_candle_age_seconds":float(np.median([x["max_candle_age"] for x in per])),
        "mean_event_spread":float(np.mean([x["mean_spread"] for x in per])),
        "mean_raw_probability_mass":float(np.mean([x["raw_mass"] for x in per]))}
    save("results.json",results)
    with (ROOT/"per-event-results.csv").open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(per[0])); writer.writeheader(); writer.writerows(per)
    with (ROOT/"coverage.csv").open("w",newline="",encoding="utf-8") as f:
        names=sorted({k for r in cov for k in r}); writer=csv.DictWriter(f,fieldnames=names); writer.writeheader(); writer.writerows(cov)
    print(json.dumps(results,indent=2),flush=True)

def selfcheck():
    r=np.array([.1,.2,.7])
    assert np.allclose(calibrate(r,1),r)
    assert np.isclose(calibrate(r,2).sum(),1)
    assert np.isclose(score([0,1],[0,1]),0)
    assert np.isclose(score([1,0],[0,1]),1)
    assert dt.datetime.fromtimestamp(cutoff(dt.date(2026,1,2)),dt.timezone.utc).hour==17
    assert dt.datetime.fromtimestamp(cutoff(dt.date(2026,6,2)),dt.timezone.utc).hour==16
    valid=[{"strike_type":"less","cap_strike":10},{"strike_type":"between","floor_strike":10,"cap_strike":11},{"strike_type":"greater","floor_strike":11}]
    assert partition_ok(valid)
    assert not partition_ok(valid[:-1])
    same=bootstrap([.003]*90,14,1,100)
    assert abs(same["lower_one_sided_95"]-.003)<1e-12
    assert bootstrap([math.nan]*30,14,1,100)["lower_one_sided_95"] is None
    for s in [None,"","2026-01-01T12:00:00"]:
        try: iso_ts(s)
        except ValueError: pass
        else: raise AssertionError("Invalid timestamp accepted")
    print("Calculation and boundary self-checks passed; not an empirical result.")

if __name__=="__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("mode",choices=["prepare","evaluate","selfcheck"])
    mode=parser.parse_args().mode
    {"prepare":prepare,"evaluate":evaluate,"selfcheck":selfcheck}[mode]()
