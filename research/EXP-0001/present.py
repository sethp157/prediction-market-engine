"""Create standalone research figures and a report from locked EXP-0001 results."""
import csv
import datetime as dt
import html
import json
import pathlib
import platform
import shutil
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import requests

ROOT=pathlib.Path(__file__).resolve().parent
DEST=ROOT/"presentation"
DEST.mkdir(exist_ok=True)
res=json.loads((ROOT/"results.json").read_text()); fit=json.loads((ROOT/"fit-lock.json").read_text())
rows=list(csv.DictReader((ROOT/"per-event-results.csv").open(encoding="utf-8")))
passed=res["replicated_screen_pass"]; beta=res["beta"]
title="Promising historical forecast calibration" if passed else "Calibration gains were small and inconclusive"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False})
fig,axs=plt.subplots(1,2,figsize=(12,4.6),layout="constrained")
labels=["Validation\nNov–Dec 2025","Test A\nJan–Mar 2026","Test B\nApr–Jun 2026"]
ss=[res["splits"][s] for s in ["validation","test_a","test_b"]]
x=np.arange(3); w=.34
axs[0].bar(x-w/2,[s.get("market",np.nan) for s in ss],w,label="Normalized market",color="#71859b")
axs[0].bar(x+w/2,[s.get("candidate",np.nan) for s in ss],w,label=f"Fixed calibration (β={beta:g})",color="#087e8b")
axs[0].set_xticks(x,labels); axs[0].set_ylabel("Mean binary Brier loss · lower is better")
axs[0].set_title("Same forecast cutoff and eligible events",loc="left",fontweight="bold"); axs[0].legend(frameon=False,fontsize=9)
for i,s in enumerate(ss): axs[0].text(i,max(s.get("market",0),s.get("candidate",0))*1.04,f"n={s['eligible']} days",ha="center",fontsize=9)
axs[0].set_ylim(0,max(s.get("market",0) for s in ss)*1.30)
for i,key in enumerate(["test_a","test_b","test_pooled"]):
    s=res["splits"][key]; c=s.get("bootstrap_14",{}); val=s.get("gain",np.nan)
    lo=c.get("lower_one_sided_95"); hi=c.get("upper_one_sided_95")
    if lo is not None and hi is not None:
        axs[1].plot([lo,hi],[i,i],color="#087e8b",lw=3)
    axs[1].scatter([val],[i],s=55,color="#073b4c",zorder=3)
axs[1].axvline(0,color="#677587",lw=1); axs[1].axvline(.001,color="#bd5d16",ls="--",label="Frozen hurdle = 0.001")
axs[1].set_yticks(range(3),["Test A","Test B","Pooled tests"]); axs[1].invert_yaxis()
axs[1].set_ylim(2.4,-.7)
axs[1].xaxis.set_major_locator(MaxNLocator(5))
axs[1].set_xlabel("Market loss − calibration loss · positive is better")
axs[1].set_title("Paired improvement and block-bootstrap bounds",loc="left",fontweight="bold")
axs[1].legend(frameon=False,fontsize=9)
fig.suptitle(title,fontsize=15,fontweight="bold",x=.04,ha="left")
fig.text(.5,-.02,"Bars on the right span the 5th–95th percentiles: one-sided 95% marginal bounds, approximate; 14-day calendar blocks.",ha="center",fontsize=8,color="#526171")
fig.savefig(DEST/"validation-summary.png",dpi=180,bbox_inches="tight"); plt.close(fig)

fig,ax=plt.subplots(figsize=(11,3.9),layout="constrained")
test=[r for r in rows if r["split"] in ("test_a","test_b")]
dates=[dt.date.fromisoformat(r["date"]) for r in test]
gains=np.array([float(r["gain"]) for r in test])
ax.plot(dates,np.cumsum(gains),color="#087e8b",lw=2)
ax.axhline(0,color="#71859b",lw=1); ax.axvline(dt.date(2026,4,1),color="#bd5d16",ls="--")
ax.set_title("Cumulative paired score gain across eligible test days",loc="left",fontweight="bold")
ax.set_ylabel("Sum of per-day Brier gains · not money")
ax.text(.01,.02,"Quarter boundary shown; this is a descriptive path, not a sequential significance test.",transform=ax.transAxes,fontsize=9,color="#526171")
fig.savefig(DEST/"score-gain-path.png",dpi=180,bbox_inches="tight"); plt.close(fig)

def num(x): return "unavailable" if x is None else f"{x:.6f}"
table=[]
for s,label in [("train","Training"),("validation","Validation"),("test_a","Test A"),("test_b","Test B"),("test_pooled","Pooled tests")]:
    z=res["splits"][s]; b=z.get("bootstrap_14",{})
    table.append([label,f"{z['eligible']}/{z['expected']}",num(z.get("market")),num(z.get("candidate")),num(z.get("gain")),num(b.get("lower_one_sided_95")),num(b.get("upper_one_sided_95"))])
mdtable="| Period | Eligible days | Market Brier | Candidate Brier | Gain | Lower bound | Upper bound |\n| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n"+"\n".join("| "+" | ".join(r)+" |" for r in table)
statement=("The candidate cleared the frozen 0.001-score hurdle in both held-out quarters using the registered approximate one-sided bounds. This is promising, narrowly scoped historical forecast evidence; prospective replication is still needed." if passed else "The candidate did not establish the frozen replicated forecasting claim. The result must not be presented as validated edge, even if a pooled point estimate is positive. This study is complete; its test periods cannot be reused to validate a revised method.")
if beta==1: statement+=" Training selected β=1, which reproduces the normalized market exactly: there is no fitted calibration improvement."
counts="\n".join(f"| {s} | {d['expected']} | {d['metadata_present']} | {d['returned_contracts']} | {d['eligible']} | {d['excluded']} |" for s,d in fit["coverage"].items())
reasons="\n".join(f"- {k}: {v} event-days (reasons can overlap)." for k,v in fit["exclusion_reason_counts"].items()) or "- No event-days excluded."
report=f'''# {title}

EXP-0001 · 2026-09-18 · historical forecasting research, no trading

## Finding

{statement}

The method was fixed before test results: a single exponent β={beta:g}, selected using training data alone, applied to the event's normalized market probabilities. The primary comparator was the normalized market, so normalization alone cannot account for a reported improvement. The split-specific details below include unsuccessful results as well as favorable ones.

![Validation summary](validation-summary.png)

## What was tested

One year of daily NYC Central Park temperature-bracket events, July 2025–June 2026, from Kalshi's public historical archive. Forecasts use bid/ask midpoint candles whose reported end timestamps fall in the declared window before noon New York time **the day before** the target date. All brackets are grouped into one event-day; they are not independent observations.

Training: July–October 2025. Validation: November–December 2025. Test A: January–March 2026. Test B: April–June 2026. The chosen parameter was never refitted. Every retained day has a complete, coherent bin set, matching quote window, and valid one-hot settlement.

{mdtable}

Lower/upper columns are the bootstrap 5th/95th percentiles, interpreted as one-sided 95% marginal bounds, not a simultaneous 95% interval. They are approximate under dependence/stationarity assumptions. The primary method used 14-day calendar blocks and 10,000 replicates per period. The frozen 7-day sensitivity is included in results.json and cannot replace a failed primary result. The 0.001 hurdle is a scientific screening choice, not an economic dollar threshold.

![Cumulative score gain](score-gain-path.png)

## Coverage and exclusions

| Split | Expected dates | Metadata present | Returned contracts | Eligible dates | Excluded dates |
| --- | ---: | ---: | ---: | ---: | ---: |
{counts}

{reasons}

Operational minimum coverage/sample requirements passed: **{str(res['minimums_pass']).lower()}**. These are not a power guarantee. The effect describes eligible archived event-days; it does not establish performance on excluded dates or show that missingness is random. Full per-date reasons are in coverage.csv; split-specific counts are in fit-lock.json.

## What has and has not been validated

- Validated here: deterministic arithmetic, input hashes/URLs, timestamp filters and New York daylight-saving handling, train-only parameter fitting, equal-event scoring, and the fixed out-of-time comparison. An independent code/method review occurred before test exposure.
- The study uses archived data reconstructed today. It cannot certify original rule versions, deleted listings, exact live candle-publication latency, or actual quote-update freshness. Candle age is not necessarily quote age.
- No historical LLM event forecasts were used. AI assisted research design and review; the study does not demonstrate an AI-specific forecasting advantage.
- No fill, fee, position-sizing, risk-capital, or net-profit model was evaluated. Midpoints are not executable purchase prices. The charts show score units, not money.
- One city, one year, and two test quarters do not establish indefinite persistence or generalization. A prospective sample is needed before a stronger claim; collecting future outcomes takes time.

## Decision and next evidence

{'ADVANCE to a separately registered prospective forecast-only replication if resources justify it; do not advance to trading.' if passed else 'REVISE the research direction or retain the market baseline; do not claim success or advance to trading from this result.'}

The user delegated continued research, so no repeated question-level approval was required. This was one bounded study with a frozen family and reporting rule. The test outcomes are now exposed. Any revised candidate requires fresh confirmation; no city, horizon, parameter family, or cutoff was changed after seeing this test.

The repository and production engine remain deferred. No paid services, accounts, orders, deposits, or scheduled jobs were used. The audit bundle includes raw responses, request hashes, the local protocol freeze, the pre-exposure amendment, locked fit, all parameter-grid training scores, per-event results, exclusions, and one-off reproduction scripts.

## Sources and audit

- [Kalshi historical routing](https://docs.kalshi.com/getting_started/historical_data): explains the archival cutoff and endpoint split.
- [Historical market schema](https://docs.kalshi.com/api-reference/historical/get-historical-markets): metadata and settlement fields.
- [Historical candle schema](https://docs.kalshi.com/api-reference/historical/get-historical-market-candlesticks): timestamped bid/ask/trade fields. These documents establish API structure, not profitability.

See ../protocol.md, ../amendments.md, ../protocol-freeze.json, ../fit-lock.json and ../results.json. Original source responses were fetched on 2026-09-18 UTC without credentials; request-start times and SHA-256 hashes are in ../request-manifest.jsonl.
'''
(DEST/"research-report.md").write_text(report,encoding="utf-8")
environment={"python":sys.version,"platform":platform.platform(),"numpy":np.__version__,"matplotlib":matplotlib.__version__,"requests":requests.__version__}
(ROOT/"environment.json").write_text(json.dumps(environment,indent=2),encoding="utf-8")
print(json.dumps({"presentation_directory":str(DEST),"title":title,"beta":beta,"replicated_screen_pass":passed}))
