# Neither candidate established the registered forecasting claim

Research report · 2026-09-19T21:11:54.334774+00:00 · two bounded historical forecasting studies

**No validated forecasting edge has been established by these two studies.** Neither candidate passed its registered replicated screen. This is a completed, auditable research result; it does not prove that every possible forecasting advantage is absent. Both attempts are retained, and the test data will not be reused to validate a revised model.

- **NYC:** pooled gain 0.000383; quarter gains 0.000387 and 0.000378. Minimum sample/coverage rule passed; both-quarter numerical screen failed. Test-quarter coverage was 100.0% and 98.9%.
- **Miami:** pooled gain 0.000017; quarter gains -0.001713 and 0.002472. Minimum sample/coverage rule failed; both-quarter numerical screen failed. Test-quarter coverage was 97.8% and 68.1%.

Miami's positive second-quarter estimate did not replicate in its first test quarter. Both Miami lower bounds were below zero, and its second-quarter coverage was 62/91 days (68.1%), below the frozen 70% minimum. The favorable second-quarter point estimate cannot establish the registered claim. NYC's two quarter estimates were positive but small and uncertain.

**Economic profitability, project viability, and an AI-specific forecasting contribution have not been tested or established.** The original ambition remains broader than what these studies can answer.

![Two-study comparison](two-study-summary.png)

## Results and the rule used to judge them

| Study / period | Eligible days | Market Brier | Candidate Brier | Gain | Lower | Upper |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| NYC / Jan–Mar | 90/90 | 0.120594 | 0.120207 | 0.000387 | -0.001565 | 0.002332 |
| NYC / Apr–Jun | 90/91 | 0.113686 | 0.113308 | 0.000378 | -0.001010 | 0.001708 |
| NYC / Pooled | 180/181 | 0.117140 | 0.116757 | 0.000383 | -0.000824 | 0.001594 |
| Miami / Jan–Mar | 88/90 | 0.107078 | 0.108791 | -0.001713 | -0.006264 | 0.002744 |
| Miami / Apr–Jun | 62/91 | 0.101813 | 0.099341 | 0.002472 | -0.003543 | 0.009093 |
| Miami / Pooled | 150/181 | 0.104902 | 0.104885 | 0.000017 | -0.003441 | 0.003825 |

Brier loss here is the mean squared probability error across an event's bins, then averaged equally across eligible event-days. Lower loss is better; gain = normalized-market loss minus candidate loss. These are score units, not returns or money. The pooled result is descriptive and cannot replace a failed quarter.

Both studies required at least 90 training days, 120 pooled test days, 50 days in each test quarter, and 70% quarter coverage. Both quarter-specific lower bounds had to exceed **0.001**. This hurdle is a provisional scientific screen, not the user's monetary definition of worthwhile effect.

NYC bounds are the 5th and 95th bootstrap percentiles (one-sided 95% marginal bounds). Miami bounds are the 2.5th and 97.5th percentiles (one-sided 97.5% marginal bounds). These are approximate, not exact or simultaneous coverage guarantees. Each used 10,000 circular calendar-block resamples with 14-day blocks, including missing dates. Dependence and stability assumptions remain. Seven-day sensitivity results are retained in each results.json and did not determine the decision. The stricter second-study screen does **not** establish a research-program-wide 5% error rate or retroactively change the first study's criterion.

## What was fixed before test exposure

Both populations cover daily high-temperature bracket events from July 2025 through June 2026. The decision time was noon America/New_York on the day before the target day. Each bin used its latest bid/ask minute candle with a reported end between 30 minutes and one minute before the decision. Midpoints were normalized to sum to one. These are forecast references; they are not executable trade prices.

Training used July–October 2025; validation November–December; Test A January–March 2026; Test B April–June. Training labels had to settle before the first validation forecast cutoff. Validation scores did not change the model. All bins for a date stayed together, and incomplete events were excluded under fixed rules. The six brackets on a day are not six independent event outcomes.

- **EXP-0001 / NYC:** raise each normalized market probability to a common exponent and renormalize. A training-only grid selected beta=1.25. No external weather information or historical LLM event forecasts were used.
- **EXP-0002 / Miami:** combine normalized market probabilities with a discretized normal temperature forecast. Training selected bias **1 F**, dispersion **1.5 F**, and weather weight **0.5** from the frozen 125-configuration family. Probability = (1 − weight) × market + weight × weather. Zero weight is exactly the market. All training-grid scores are retained.

For Miami, all 2,190 archived contract rules explicitly identify Miami International Airport and the National Weather Service Climatological Report (Daily). The external predictor is the archived NOAA GFS MOS KMIA 06Z run from the preceding day, using its +42-hour n_x value. For an integer bin [a,b], weather probability is Phi((b+0.5−F−bias)/dispersion) − Phi((a−0.5−F−bias)/dispersion), with infinite tails. The bins partition all integers; Phi is the standard normal CDF. This daytime-high predictor differs from the full settlement-day maximum. Treating it as a predictor does not assert identical targets.

Miami was chosen **after** the first study's inconclusive result. The new family adds external information and uses previously uninspected city-specific outcomes. Its study protocol was frozen before retrieving those outcomes. Both cities share calendar dates; a different city does not prove independence. Local hash freezes are auditable records, not independent public registrations.

## Coverage, missingness, and supporting comparisons

| Study / split | Expected | Market metadata | Market eligible without MOS | Valid MOS | Eligible |
| --- | ---: | ---: | ---: | ---: | ---: |
| NYC / train | 123 | 123 | 118 | not used | 118 |
| NYC / validation | 61 | 61 | 59 | not used | 59 |
| NYC / test_a | 90 | 90 | 90 | not used | 90 |
| NYC / test_b | 91 | 91 | 90 | not used | 90 |
| Miami / train | 123 | 123 | 113 | 123 | 113 |
| Miami / validation | 61 | 61 | 58 | 61 | 58 |
| Miami / test_a | 90 | 90 | 88 | 90 | 88 |
| Miami / test_b | 91 | 91 | 62 | 91 | 62 |

Market eligibility includes complete bins, valid quotes, rules, timestamps, and settlement integrity; it is distinct from metadata presence. MOS validity requires matching station, model, runtime, horizon, and a finite nonsentinel forecast. A successful HTTP response alone is insufficient.

Exclusion reason counts overlap:

- **NYC:** incomplete_quotes: 7; missing_candle_window: 7; training_label_not_available: 1; not_created_and_open_at_cutoff: 2; zero_or_missing_mass: 2.
- **Miami:** incomplete_quotes: 42; missing_candle_window: 42; training_label_not_available: 1; not_created_and_open_at_cutoff: 2; zero_or_missing_mass: 2; nonbinary_label: 1.

Effects apply to eligible archived days. Coverage thresholds do not show that missingness is random or establish performance on excluded dates. Per-date coverage and reasons are retained in each coverage.csv.

| Study / split | Eligible | Market loss | Candidate loss | Raw midpoint loss | Uniform loss |
| --- | ---: | ---: | ---: | ---: | ---: |
| NYC / train | 118 | 0.111409 | 0.110638 | 0.111555 | 0.138889 |
| NYC / validation | 59 | 0.109799 | 0.108318 | 0.109862 | 0.138889 |
| NYC / test_pooled | 180 | 0.117140 | 0.116757 | 0.117091 | 0.138889 |
| Miami / train | 113 | 0.120463 | 0.114466 | 0.121128 | 0.138889 |
| Miami / validation | 58 | 0.095240 | 0.104008 | 0.094531 | 0.138889 |
| Miami / test_pooled | 150 | 0.104902 | 0.104885 | 0.104716 | 0.138889 |

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

REVISE the research direction; this batch provides no basis to advance to trading or engine development. Do not keep altering methods until these exposed tests pass.

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
