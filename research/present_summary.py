"""Presentation only. Reads final, already exposed study outputs; never fits a model."""
import datetime as dt
import json
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT.parent
DEST=ROOT
DEST.mkdir(exist_ok=True)
studies=[]
for folder,name,city in [("EXP-0001","EXP-0001","NYC"),("EXP-0002","EXP-0002","Miami")]:
    path=ROOT/folder
    read=lambda f:json.loads((path/f).read_text(encoding="utf-8-sig"))
    studies.append(dict(name=name,city=city,result=read("results.json"),fit=read("fit-lock.json"),freeze=read("protocol-freeze.json")))

def fmt(x): return "unavailable" if x is None else f"{x:.6f}"
def bounds(study,z,block=14):
    b=z.get(f"bootstrap_{block}" if block==14 else "bootstrap_7_sensitivity",{})
    level="95" if study["name"]=="EXP-0001" else "97_5"
    return b.get("lower_one_sided_"+level),b.get("upper_one_sided_"+level)

second=studies[1]; passed=second["result"]["replicated_screen_pass"]
title="A promising historical signal, with timing still unverified" if passed else "Neither candidate established the registered forecasting claim"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False})
fig,axs=plt.subplots(1,2,figsize=(12,4.8),layout="constrained")
for ax,st in zip(axs,studies):
    ax.axvline(0,color="#9aa4b2",lw=1)
    ax.axvline(.001,color="#b35720",ls="--",lw=1.5,label="Frozen hurdle: 0.001")
    for i,key in enumerate(["test_a","test_b","test_pooled"]):
        z=st["result"]["splits"][key]; lo,hi=bounds(st,z)
        if lo is not None and hi is not None: ax.plot([lo,hi],[i,i],color="#087e8b",lw=3)
        if z.get("gain") is not None: ax.scatter(z["gain"],i,color="#073b4c",s=55,zorder=3)
    ax.set_yticks(range(3),["Jan–Mar 2026","Apr–Jun 2026","Pooled tests"])
    ax.set_ylim(2.7,-.6); ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.set_title(st["city"]+": "+("market calibration" if st["city"]=="NYC" else "weather + market"),loc="left",fontweight="bold")
    ax.set_xlabel("Paired Brier gain · positive favors candidate")
    ax.legend(loc="lower left",frameon=False,fontsize=9)
fig.suptitle(title,fontsize=15,fontweight="bold",x=.025,ha="left")
fig.text(.5,-.035,"Bounds: NYC 5th–95th percentiles; Miami 2.5th–97.5th. Approximate 14-day block bootstrap. Panel scales may differ.",ha="center",fontsize=8,color="#536170")
fig.savefig(DEST/"two-study-summary.png",dpi=180,bbox_inches="tight"); plt.close(fig)

table=["| Study / period | Eligible days | Market Brier | Candidate Brier | Gain | Lower | Upper |","| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
for st in studies:
    for key,label in [("test_a","Jan–Mar"),("test_b","Apr–Jun"),("test_pooled","Pooled")]:
        z=st["result"]["splits"][key]; lo,hi=bounds(st,z)
        table.append("| "+" | ".join([st["city"]+" / "+label,f"{z['eligible']}/{z['expected']}",fmt(z.get("market")),fmt(z.get("candidate")),fmt(z.get("gain")),fmt(lo),fmt(hi)])+" |")

coverage=["| Study / split | Expected | Market metadata | Market eligible without MOS | Valid MOS | Eligible |","| --- | ---: | ---: | ---: | ---: | ---: |"]
training=["| Study / split | Eligible | Market loss | Candidate loss | Raw midpoint loss | Uniform loss |","| --- | ---: | ---: | ---: | ---: | ---: |"]
exclusions=[]
for st in studies:
    for split,z in st["fit"]["coverage"].items():
        coverage.append("| "+" | ".join(map(str,[st["city"]+" / "+split,z["expected"],z["metadata_present"],z.get("market_eligible_without_mos",z["eligible"]),z.get("mos_valid","not used"),z["eligible"]]))+" |")
    for split in ["train","validation","test_pooled"]:
        z=st["result"]["splits"][split]
        training.append("| "+" | ".join([st["city"]+" / "+split,str(z["eligible"]),*[fmt(z.get(k)) for k in ["market","candidate","raw","uniform"]]])+" |")
    reasons=st["fit"]["exclusion_reason_counts"]
    exclusions.append("- **"+st["city"]+":** "+("; ".join(f"{k}: {v}" for k,v in reasons.items()) or "none")+".")

cfg=second["result"]["config"]
finding=("The weather-plus-market model passed the fixed numerical screen in both Miami test quarters. This is **promising exploratory historical evidence**, not fully validated contemporaneous forecasting. Its weather publication time was assumed, and no score can verify that assumption. The first, NYC calibration study remained inconclusive."
         if passed else "**No validated forecasting edge has been established by these two studies.** Neither candidate passed its registered replicated screen. This is a completed, auditable research result; it does not prove that every possible forecasting advantage is absent. Both attempts are retained, and the test data will not be reused to validate a revised model.")
if cfg[2]==0: finding+=" Miami training selected zero weather weight, so its fitted candidate reproduces the normalized market exactly."
failure_detail=[]
for st in studies:
    r=st["result"]; a=r["splits"]["test_a"]; b=r["splits"]["test_b"]; pool=r["splits"]["test_pooled"]
    failure_detail.append(f"- **{st['city']}:** pooled gain {fmt(pool.get('gain'))}; quarter gains {fmt(a.get('gain'))} and {fmt(b.get('gain'))}. Minimum sample/coverage rule {'passed' if r['minimums_pass'] else 'failed'}; both-quarter numerical screen {'passed' if r['replicated_screen_pass'] else 'failed'}. Test-quarter coverage was {a.get('coverage',0):.1%} and {b.get('coverage',0):.1%}.")
now=dt.datetime.now(dt.timezone.utc).isoformat()
report=f'''# {title}

Research report · {now} · two bounded historical forecasting studies

{finding}

{"\n".join(failure_detail)}

Miami's positive second-quarter estimate did not replicate in its first test quarter. Both Miami lower bounds were below zero, and its second-quarter coverage was 62/91 days (68.1%), below the frozen 70% minimum. The favorable second-quarter point estimate cannot establish the registered claim. NYC's two quarter estimates were positive but small and uncertain.

**Economic profitability, project viability, and an AI-specific forecasting contribution have not been tested or established.** The original ambition remains broader than what these studies can answer.

![Two-study comparison](two-study-summary.png)

## Results and the rule used to judge them

{"\n".join(table)}

Brier loss here is the mean squared probability error across an event's bins, then averaged equally across eligible event-days. Lower loss is better; gain = normalized-market loss minus candidate loss. These are score units, not returns or money. The pooled result is descriptive and cannot replace a failed quarter.

Both studies required at least 90 training days, 120 pooled test days, 50 days in each test quarter, and 70% quarter coverage. Both quarter-specific lower bounds had to exceed **0.001**. This hurdle is a provisional scientific screen, not the user's monetary definition of worthwhile effect.

NYC bounds are the 5th and 95th bootstrap percentiles (one-sided 95% marginal bounds). Miami bounds are the 2.5th and 97.5th percentiles (one-sided 97.5% marginal bounds). These are approximate, not exact or simultaneous coverage guarantees. Each used 10,000 circular calendar-block resamples with 14-day blocks, including missing dates. Dependence and stability assumptions remain. Seven-day sensitivity results are retained in each results.json and did not determine the decision. The stricter second-study screen does **not** establish a research-program-wide 5% error rate or retroactively change the first study's criterion.

## What was fixed before test exposure

Both populations cover daily high-temperature bracket events from July 2025 through June 2026. The decision time was noon America/New_York on the day before the target day. Each bin used its latest bid/ask minute candle with a reported end between 30 minutes and one minute before the decision. Midpoints were normalized to sum to one. These are forecast references; they are not executable trade prices.

Training used July–October 2025; validation November–December; Test A January–March 2026; Test B April–June. Training labels had to settle before the first validation forecast cutoff. Validation scores did not change the model. All bins for a date stayed together, and incomplete events were excluded under fixed rules. The six brackets on a day are not six independent event outcomes.

- **EXP-0001 / NYC:** raise each normalized market probability to a common exponent and renormalize. A training-only grid selected beta={studies[0]['result']['beta']:g}. No external weather information or historical LLM event forecasts were used.
- **EXP-0002 / Miami:** combine normalized market probabilities with a discretized normal temperature forecast. Training selected bias **{cfg[0]:g} F**, dispersion **{cfg[1]:g} F**, and weather weight **{cfg[2]:g}** from the frozen 125-configuration family. Probability = (1 − weight) × market + weight × weather. Zero weight is exactly the market. All training-grid scores are retained.

For Miami, all 2,190 archived contract rules explicitly identify Miami International Airport and the National Weather Service Climatological Report (Daily). The external predictor is the archived NOAA GFS MOS KMIA 06Z run from the preceding day, using its +42-hour n_x value. For an integer bin [a,b], weather probability is Phi((b+0.5−F−bias)/dispersion) − Phi((a−0.5−F−bias)/dispersion), with infinite tails. The bins partition all integers; Phi is the standard normal CDF. This daytime-high predictor differs from the full settlement-day maximum. Treating it as a predictor does not assert identical targets.

Miami was chosen **after** the first study's inconclusive result. The new family adds external information and uses previously uninspected city-specific outcomes. Its study protocol was frozen before retrieving those outcomes. Both cities share calendar dates; a different city does not prove independence. Local hash freezes are auditable records, not independent public registrations.

## Coverage, missingness, and supporting comparisons

{"\n".join(coverage)}

Market eligibility includes complete bins, valid quotes, rules, timestamps, and settlement integrity; it is distinct from metadata presence. MOS validity requires matching station, model, runtime, horizon, and a finite nonsentinel forecast. A successful HTTP response alone is insufficient.

Exclusion reason counts overlap:

{"\n".join(exclusions)}

Effects apply to eligible archived days. Coverage thresholds do not show that missingness is random or establish performance on excluded dates. Per-date coverage and reasons are retained in each coverage.csv.

{"\n".join(training)}

The raw-midpoint and uniform comparisons are supporting diagnostics. They were not substituted for the primary normalized-market benchmark.

## Validation performed and its limits

The audit includes raw-response hashes and request URLs, pagination and derived-data checks, quote windows, daylight-saving handling, complete-bin and one-hot-settlement checks, training-label availability, fixed training selection, locked code/data dependencies, and independent pretest method/code review. Test evaluation is recorded once per study. Independent numeric recomputation is documented in the individual study packages; review by another agent is a useful check, not an external scientific replication.

The following remain unverified:

1. **Historical availability.** IEM records initialization and forecast-valid times, not each run's historical receipt/publication time. Runtime + six hours is an assumption. Original source corrections, rule versions, deleted listings, and market-candle publication latency are not fully certified. A candle end is not a last-quote-update timestamp.
2. **Generalization and inferential assumptions.** One year per city and two test quarters do not establish indefinite persistence. The block-bootstrap approximation, seasonal stability, selection history, and conditional coverage limit inference.
3. **AI-specific value.** AI assisted research and code; deterministic models supplied these forecasts. No claim that an LLM outperformed the market is supported.
4. **Economics.** No fees, fills, position sizing, capital risk, capacity, or total research costs were evaluated as a trading policy. A forecasting gain need not produce positive executable expected value or profit.

An operational collection issue is retained in the Miami collection audit: subsecond rate spacing could not be certified exactly from the Windows clock readings used by the collector. The proposed high-resolution-clock change did not execute before collection finished. No source response or historical timestamp was altered to hide this issue; the audit reports the observed gaps. This does not establish a score advantage or repair the separate historical-availability limitation.

## Decision and next evidence

{'ADVANCE only to designing a fresh prospective forecasting confirmation of the promising candidate. Its numerical historical pass does not remove the timing limitation or authorize trading.' if passed else 'REVISE the research direction; this batch provides no basis to advance to trading or engine development. Do not keep altering methods until these exposed tests pass.'}

The initial two-study evaluation ends here under its stopping rules. A third candidate or changed horizon requires a distinct rationale, a new frozen evidence plan, and fresh confirmation. A stronger forecasting claim requires contemporaneous recording of source values, receipt times, and market rules before decisions, with untouched future outcomes. [Next evidence requirements](../docs/NEXT_EVIDENCE_REQUIREMENTS.md) defines what must be resolved; it is not an active recurring collection or a frozen third study.

[D0006](../docs/decisions/D0006-two-study-evidence-decision.md) records the evidence decision, failed criteria, exposure history, and retained scope.

The repository and production evaluation engine remain deferred. No paid service, trade, account change, or scheduled job was used. The founding document conflicts, mathematical definitions, scope amendments, and current decision state are preserved alongside this report.

## Sources and audit files

- [EXP-0001 package](EXP-0001/README.md): complete NYC protocol, responses, locks, scores, figures, and independent arithmetic review.
- [EXP-0002 package](EXP-0002/README.md): complete Miami protocol, source timing clarification, responses, locks, scores, and reviews.
- [Research state](../RESEARCH_STATE.md), [founding-document audit](../docs/ORIGIN_REVIEW.md), and [delegated authority](../docs/decisions/D0003-delegated-research-authority.md).
- [Kalshi historical API](https://docs.kalshi.com/getting_started/historical_data) and [historical candle schema](https://docs.kalshi.com/api-reference/historical/get-historical-market-candlesticks) describe the archival endpoints and timestamp fields. The studies use the retained raw responses as their data record.
- [IEM MOS archive](https://mesonet.agron.iastate.edu/mos/) describes forecast archiving and exact-runtime access. [NOAA's 06Z/18Z MOS specification](https://www.weather.gov/media/mdl/mdltpb05-04.pdf) documents the daytime-maximum horizon. [NOAA's MOS timing discussion](https://www.weather.gov/media/mdl/pub/Ghirardelli_Glahn_MDLsLAMP_2010.pdf) supports an ordinary lag discussion, not the actual publication time of every study run.

See the file manifests for exact SHA-256 values. Raw response retrieval dates describe this research session; they must not be confused with historical information availability.
'''
report = """> Repository publication note — 2026-09-20 UTC: [D0007](../docs/decisions/D0007-repository-handoff.md) authorizes this documentation/evidence repository. The scientific report below preserves the completed studies; earlier repository-deferral wording describes the study period. Production-engine work remains deferred. See [HANDOFF.md](../HANDOFF.md).

""" + report
(DEST/"RESEARCH_REPORT.md").write_text(report,encoding="utf-8")
print(json.dumps({"report":str(DEST/"RESEARCH_REPORT.md"),"chart":str(DEST/"two-study-summary.png"),"second_screen_pass":passed}))
