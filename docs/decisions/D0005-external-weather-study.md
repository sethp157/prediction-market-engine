# D0005 / EXP-0002 — Weather information plus market forecasts

Status: registered second bounded study, agent decision under D0003 delegation. Frozen before this study's outcome retrieval. EXP-0001 is complete and inconclusive; it is not modified or hidden.

## Reason for a second study and inference limit

EXP-0001's market-only calibration produced a small, uncertain gain and failed its reporting rule. It supplied no new weather information. Test one new family that combines an archived NOAA GFS MOS point forecast with market probabilities, using a new, unexposed city. This is a separate study selected after the first result, not an untouched continuation of EXP-0001. Report both attempts together.

The IEM NOAA MOS archive exposes model initialization and forecast-valid timestamps but not historical per-run receipt/publication times. This study therefore has a material availability assumption and is **exploratory historical evidence**, even if its out-of-time scores pass. A score improvement cannot validate the timing assumption. Do not describe it as fully timestamp-validated, an AI-specific gain, executable profit, or project viability.

## Fixed population, timing, data, and split

Use KXHIGHMIA Miami daily-high-temperature events from 2025-07-01 through 2026-06-30. Require archived rules to mention Miami and the National Weather Service. Apply EXP-0001's complete-bin, final-one-hot settlement, pre-cutoff created/open, quote-validity, and whole-event exclusion rules. No NYC outcomes are reused. The initial Miami feasibility probe is a July 2026 event outside this period.

Decision time: noon America/New_York the day before the target date. Market snapshot: latest minute bid/ask candle ending in [decision minus 30 minutes, decision minus 60 seconds], for every bin. Normalize midpoints to an event vector r; raw midpoints and uniform probabilities are supporting diagnostics. Neither the midpoint nor normalization is an execution assumption.

External predictor: NOAA GFS MOS for KMIA from the 06:00 UTC cycle on the day before the target date. Fetch the exact station/runtime, never the latest-run default. Select the n_x value at runtime + 42 hours, representing the next day's daytime high forecast. Reject missing/sentinel values, mismatched runtime/station, or missing required horizon. Predeclare plausible numeric range -100 to 150 Fahrenheit only as a malformed-data guard, not an outcome selection.

The n_x target is a 07:00–19:00 local-standard-time daytime maximum, not necessarily the full climate-day maximum used by settlement. Treat it as a predictor, not the target itself. Bias and dispersion below may absorb some mismatch; no assertion of exact target equivalence is made.

Assume this 06Z MOS cycle is available at runtime + 6 hours, later than NOAA's approximately four-hour ordinary publication lag. Require that assumed time precede the decision. No per-run historical publication evidence proves this assumption; retain that limitation without euphemism.

Training: July–October 2025, with labels settled strictly before the first validation forecast cutoff. Validation: November–December 2025. Test A: January–March 2026. Test B: April–June 2026. Missing MOS excludes the entire event; report every expected date, available market/MOS counts, and overlapping exclusion reasons. The estimand is conditional on eligible archived event-days, not all dates or missing-at-random coverage.

## Frozen candidate family

Let F be the MOS predictor. For integer temperature bin [a,b] use a discretized normal distribution with mean F+c and standard deviation s, giving probability Phi((b+0.5-F-c)/s)-Phi((a-0.5-F-c)/s); tails extend to infinity. Bin integer ranges must partition all integers as in EXP-0001. All units here are degrees Fahrenheit. Let q be this complete probability vector.

Candidate m = (1-w)r + wq, where the finite training grid is:

- bias c in {-2,-1,0,1,2};
- standard deviation s in {1.5,2,3,4,5};
- mixture weight w in {0,0.25,0.5,0.75,1}.

Choose the triple minimizing training equal-event mean binary Brier loss. Ties within 1e-12 prefer lower w, then smaller absolute c, then larger s, then lower c. No refitting, grid expansion, horizon/city changes, or alternative weather products after later scores. Weight zero is exactly the market baseline. The 125 training combinations constitute one fixed trained family, not 125 test-set comparisons; all grid scores will be retained.

## Evidence criteria

Primary: paired Brier gain versus normalized market, equal weight per event-day. Retain delta_F = 0.001 as a provisional scientific screening hurdle, not a monetary threshold. Same minimums as EXP-0001: >=90 train events, >=120 pooled tests, >=50 each quarter, and >=70% calendar coverage in each quarter. Coverage is not a power guarantee.

Use EXP-0001's 14-day circular calendar-block bootstrap, 10,000 repetitions, including missing dates and making the interval unavailable if any replicate has no eligible days. Fix seeds 20260921 (Test A), 20260922 (Test B), 20260923 (pooled). Report 2.5th and 97.5th percentiles as one-sided 97.5% marginal bounds. Both test-quarter lower bounds must exceed delta_F to pass the numerical screen. This conservatively allocates alpha=0.025 to this second family; EXP-0001 already failed its looser original criterion. This does not overcome this study's unresolved source timing or dependence assumptions.

The 7-day sensitivity remains descriptive, never a replacement for the primary decision. A pooled positive score is insufficient for replication. Report adverse, null, and inconclusive results. Do not search a third family or extend dates within this initial two-study evaluation. New research must have a new rationale and fresh evidence plan.

## Execution, review, and reporting

Use only public GET requests with no credentials or paid API, at <=4 requests/second to Kalshi and <=1 request/second to IEM. Store each response, request-start time, exact URL, and SHA-256. Verify files/URLs and derived inputs. Freeze analysis/code/data dependencies at fit lock; independent review occurs before test exposure. Only training/validation are printed before the held-out evaluation.

One-off scripts and research artifacts are permitted; no repository, production engine, trading policy, orders, or recurring tasks. No research finding automatically authorizes trading. The final report must lead with the evidence's actual status, compare both study attempts, and explicitly state that prospective contemporaneous recording is required for stronger confirmation.

Primary sources verified 2026-09-18/19 UTC: [IEM MOS archive](https://mesonet.agron.iastate.edu/mos/), [NOAA MOS daytime-max specification](https://www.weather.gov/media/mdl/mdltpb05-04.pdf), [NOAA operational lag discussion](https://www.weather.gov/media/mdl/pub/Ghirardelli_Glahn_MDLsLAMP_2010.pdf), [IEM raw-text retention](https://mesonet.agron.iastate.edu/info/datasets/afos.html). The service's forecast JSON is primary-provider archive data, not observations or retrospective LLM answers.
