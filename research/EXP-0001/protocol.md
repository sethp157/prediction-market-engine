# D0004 / EXP-0001 — Frozen initial validation study

Status: AGENT DECISION under D0003 delegation. Written and frozen before retrieval/inspection of study outcomes on 2026-09-18 UTC; machine-readable freeze timestamp and SHA-256 accompany this file. Any later correction is an appended amendment with exposure status.

## Question and scope

Does one training-fitted temperature transformation improve out-of-time mean binary Brier loss over a coherent market-probability benchmark for NYC daily-high-temperature bracket events? This is one bounded historical calibration study, not an LLM event-forecast test, a trading backtest, or proof of economic viability. Classify as retrospective out-of-time validation conditional on the archived data, not preregistered prospective confirmation. The protocol is frozen locally, not registered with an independent timestamping service.

The feasibility probes were limited to API schema, the current KXHIGHNY series, and the event KXHIGHNY-26JUL18, which is outside the study window. Its labels were returned in raw metadata but not printed or used for method selection. No study outcome has been inspected at freeze. The unused shrink-to-0.5/binary-logit formulations were considered mathematically and rejected before outcomes because a complete categorical vector is available; they are not empirical trials.

## Decisions Q3–Q10

| Gate | Agent decision and rationale | Limits |
| --- | --- | --- |
| Q3 benchmark | At noon America/New_York on the day before each target date, use archived YES bid/ask midpoints, normalized across the complete exhaustive event. Raw midpoints and uniform 1/K are required secondary comparators. | Market midpoint is a forecasting reference, not an executable purchase price. No closing-price benchmark. Normalization ensures sum one but is not assumed to improve score. |
| Q4 universe | KXHIGHNY daily Central Park NYC temperature bracket events, target dates 2025-07-01 through 2026-06-30 inclusive. | One city/class; no generalization to all markets. Selection based on recurrence, observable clock, and available schema, not results. |
| Q5 information | Only archived pre-cutoff bid/ask closes and event structure/date enter forecasts; training labels enter parameter fitting only. Metadata and final results are separate roles. | Retrospective rule revisions and archive completeness cannot be fully certified; report these limitations. No news, historical LLM answers, final quote, settlement value, or future prices as features. |
| Q6 evaluation | Chronological fixed train/validation/test-A/test-B; group all bins within a date; calendar-block uncertainty; no retuning on validation/test. | Historical recalibration evidence; not a clean prospective AI test. |
| Q7 forecast/uncertainty | Store event ID, target/cutoff/source timestamps, complete bin vector, probabilities, chosen beta, version/hash, and coverage/exclusion reason. Uncertainty applies to paired score differences. | No model self-confidence and no assertion of calibrated event-probability intervals. |
| Q8 responsibilities | AI specifies/reviews interpretation; one-off deterministic scripts retrieve, calculate, audit, and plot. | Repository and production evaluation engine remain deferred. No AI-specific causal contribution claim. |
| Q9 stop rules | One population, one horizon, one family/grid. Stop this study after the frozen test, or report infeasibility if coverage/integrity fails. Preserve nulls and failures. | Do not change city/horizon/grid or extend time until significance appears. No paid work or trading. |
| Q10 advancement | Defined reporting criteria below. A pass may justify further prospective research only. | Paper/live trading, economic viability, and automation are not unlocked by a forecast-score pass. |

## Population, snapshots, and outcome integrity

- Enumerate all archived markets in series KXHIGHNY using cursor pagination; calendar dates in ticker identify the target day. Enumerate every expected calendar date in the window, including dates with no API record. Do not select by volume, profit, eventual winning bin, or terminal price.
- Use the historical archive because this entire window precedes the retrieved settlement cutoff of 2026-07-20. If an in-window event is not archived, report it missing; do not silently borrow a terminal live price.
- For each event, require exactly one low-tail and high-tail bin, integer endpoints, and contiguous mutually exclusive interior integer-temperature intervals. Require all returned bins to have been created/open by the snapshot cutoff and a rule mentioning Central Park and the National Weather Service. This validates the archived bin structure, not historical completeness of deleted listings or original rule versions.
- Forecast decision time is noon local time the day before the ticker's target date. Use historical America/New_York daylight-saving rules. For each bin take the latest minute candle ending no later than decision minus 60 seconds and no earlier than decision minus 30 minutes. The extra minute is a declared publication-lag allowance, not proof of historical availability.
- Require both quote closes finite in [0,1], bid <= ask, and a nonempty midpoint vector with positive total. No maximum spread filter, liquidity filter, endpoint clipping, or outcome-dependent quote exclusion. Exclude the whole event if any required bin lacks a valid snapshot.
- A candle's end is not a last-quote-update timestamp; actual quote freshness, displayed depth and executable fills are not certified. Report candle age and spread descriptively.
- Require final binary yes/no labels, exactly one yes per event, and settlement after the forecast decision. Report void, nonbinary, inconsistent, missing, and unsettled outcomes separately instead of treating them as losses or erasing them.
- Training labels must have settled before the first validation forecast cutoff. Exclude late training settlements by this prespecified rule and count them.
- Save raw responses with retrieval time, URL, and SHA-256; a manifest identifies metadata, candles, failures, and analysis inputs. No API credentials are required. Data are retained locally for this user's audit, not published as a third-party data service.

## Fixed temporal split and fitting

| Split | Target dates | Use |
| --- | --- | --- |
| Train | 2025-07-01 to 2025-10-31 | Select beta once |
| Validation | 2025-11-01 to 2025-12-31 | Report fixed-model performance and operational checks; no retuning |
| Test A | 2026-01-01 to 2026-03-31 | First untouched out-of-time evaluation |
| Test B | 2026-04-01 to 2026-06-30 | Second untouched out-of-time evaluation, same fixed beta |

For event g and its K_g bins, b_gk is the bid/ask midpoint, r_gk = b_gk / sum_j b_gj, and:

\[
m_{gk}(\beta)=\frac{r_{gk}^{\beta}}{\sum_j r_{gj}^{\beta}},
\qquad
\beta\in\{0.5,0.75,1,1.25,1.5,1.75,2\}.
\]

Use 0^beta = 0 for beta > 0. Choose beta with lowest training equal-event mean Brier loss; exact numerical ties within 1e-12 choose closest to 1, then lower beta. Beta = 1 is the identity benchmark. Do not refit, expand the grid, or substitute another model after any later split is inspected. The grid is one training-selected model family, not seven separate test-set searches.

\[
L_g(p)=\frac{1}{K_g}\sum_k(p_{gk}-Y_{gk})^2,
\qquad D_g=L_g(r)-L_g(m),
\qquad\widehat\theta=\frac{1}{G}\sum_gD_g.
\]

Every valid event-day receives equal weight. Individual bins are never independent samples. Report K distribution. A lower loss is better and positive D favors the candidate. Uniform 1/K and raw midpoints are diagnostic comparators, not substitutes for the primary normalized benchmark.

## Evidence standard and finite stopping

Freeze a provisional scientific screening hurdle delta_F = 0.001 mean-binary-Brier units. This is an agent-selected research hurdle, not the user's monetary preference or an economically meaningful dollar conversion.

For each test quarter, use a circular moving-calendar-block bootstrap on its calendar-day array, with excluded dates represented as missing, 14-day blocks, 10,000 repetitions, NumPy generator seed 20260918 (Test B seed 20260919; pooled seed 20260920). Resample blocks until the original quarter length, truncate, and take the mean over nonmissing eligible events. Report percentile 5th and 95th bounds: one-sided 95% marginal bounds, not a simultaneous 95% interval. Treat their coverage as approximate and dependence/stationarity-assumption-dependent. A prespecified 7-day block sensitivity is descriptive only and cannot rescue a failed primary result.

Operational minimum: at least 90 eligible training events, 120 pooled test events, 50 in each test quarter, and >=70% calendar-date coverage in each test quarter. These are minimum evidence/coverage checks, not a power guarantee. List expected, returned, valid, and excluded counts per split. A failure makes the study exploratory/inconclusive for its strict claim; do not adjust the window or exclusions to pass.

Label **promising replicated historical forecasting evidence** only if all minimums/integrity checks pass and each test quarter's primary one-sided lower bound exceeds delta_F. Requiring both quarters to pass is an intersection-union rule, conditional on valid constituent inference; there is no claim that the two marginal bounds are jointly 95%. Also report validation and pooled scores, all train-grid results, and both test quarters whether they pass or fail.

If a quarter's upper bound is <= delta_F, report evidence against the specified worthwhile effect in that quarter. Otherwise report inconclusive when the primary pass condition fails. If beta = 1, report no fitted improvement. No optional stopping, new horizons, alternate cities, or additional calibration family after the test. An economically promising finding would need a separate later protocol using credible fills/costs/risk; this study does not supply it.

## Validation and deliverables

Before unblinding tests, independently review the analysis implementation against this manifest. Check timestamp filtering, normalization/identity, one-hot outcomes, grouping, fit isolation, coverage accounting, and bootstrap structure. Fix implementation defects by logged amendment before test exposure when possible; if outcomes inform a fix, label the test exposed and weaken the claim rather than pretending it is untouched.

Deliver: a concise research report with plots/tables, per-event results/coverage, train-grid scores, uncertainty output, raw-data/hash provenance, and one-off reproduction scripts. Preserve the protocol and all failures. No web app, database, Git repository, recurring job, or trading interface will be created.

Primary-source API references checked 2026-09-18: [archive routing](https://docs.kalshi.com/getting_started/historical_data), [historical markets](https://docs.kalshi.com/api-reference/historical/get-historical-markets), [historical candles](https://docs.kalshi.com/api-reference/historical/get-historical-market-candlesticks). These establish documented fields and routing, not market completeness or profitability.
