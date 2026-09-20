# EXP-0002 — Pre-exposure interpretation clarifications

Prepared / timestamp corrected: 2026-09-19 12:04:59 UTC (2026-09-19 America/Chicago).
Provenance note: an earlier draft mistakenly reused a clock reading from before an interruption. This correction records the current preparation session rather than backdating the file. The substantive review and all numerical criteria are unchanged; no EXP-0002 test data were inspected.
Status: independent protocol review; incorporate this record in the fit/evaluation dependency lock before EXP-0002 test exposure. The reviewer inspected the protocol and methodological source documentation, not EXP-0002 market outcomes or test results.

This record preserves the frozen D0005 protocol. It changes no population, source, horizon, candidate grid, fitting rule, exclusion, bootstrap rule, numerical hurdle, or pass criterion. It clarifies the permissible interpretation of those choices.

## Error rates and multiple studies

The second study uses the frozen 2.5th-percentile lower bounds, a more stringent numerical screen than EXP-0001's original 5th-percentile lower bounds. This is **not a demonstrated family-wise 5% error guarantee across the research program**.

EXP-0001 used its original 0.05 rule. Observing that it failed does not retroactively change that rule to 0.025, erase its opportunity for a false positive, or make its error allowance available again. D0005's reference to allocating alpha = 0.025 must be read only as specifying the second study's numerical stringency, not a valid retrospective allocation across both studies. Report both attempts and the adaptive choice to undertake a new study after the first result. No program-wide error bound is established here.

Within EXP-0002, requiring both quarter-specific lower bounds to exceed the hurdle is an intersection-union screen: a 0.025 single-study error interpretation would require valid constituent one-sided inference. It does not require independence of the quarters, and it does not establish simultaneous 97.5% coverage of both bounds. The frozen calendar-block percentile bootstrap provides approximate inference conditional on its dependence and stability assumptions, not guaranteed nominal coverage. Neither stricter percentiles nor the descriptive block-length sensitivity repair those assumptions.

The 125 training combinations are one frozen model-selection procedure followed by fixed held-out evaluation. They are not 125 separate test-set searches. This does not remove the separate, broader issue of choosing this study after examining EXP-0001.

## Research history and authority

EXP-0001 remains stopped under its original frozen rule, with its inconclusive result retained. EXP-0002 is a separately documented research-cycle extension under D0003, selected after that result; it is not an amendment that rescues, repeats, or relabels the first test. The new rationale is the addition of an external weather predictor. The changed city and model family must remain visible in the research history.

A new city supplies previously uninspected city-specific outcomes; it does not by itself prove statistical independence from the first city's weather, market conditions, or shared calendar period. Neither study justifies a claim about other cities, venues, horizons, or all prediction markets. This two-study exercise ends under its declared stopping rules even if neither study is promising.

## Availability, target, and coverage limits

The external data are an IEM archive of NOAA GFS MOS forecasts. Initialization and forecast-valid timestamps have different meanings from actual historical publication or receipt timestamps. The protocol's runtime + 6 hours is an **assumed availability time**, not an observed per-run publication record. Label that field accordingly. A favourable score cannot establish that the archived value was available, in that form, before the historical decision.

The [IEM archive documentation](https://mesonet.agron.iastate.edu/mos/) describes realtime processing and exact-runtime retrieval, but this does not certify each archived run's historical arrival or absence of later correction. [NOAA's 0600/1800 UTC MOS specification](https://www.weather.gov/media/mdl/mdltpb05-04.pdf), section 3, identifies the +42-hour value from a 0600 cycle as the following daytime maximum and defines daytime using local standard time. That supports the predictor's interpretation, not equality with a market's full-day settlement target.

The fitted bias and dispersion may help predict the distinct settlement outcome; good performance would not prove that the two temperature targets are identical. Confirm and report the actual market resolution station from rules rather than assuming the city name establishes station identity.

Reported effects concern protocol-eligible archived event-days, conditional on the market and MOS coverage requirements. A coverage threshold does not establish missing-at-random exclusions or performance on omitted dates. Show expected-date counts, separate source availability, and overlapping exclusion reasons.

## Required reporting language

If the frozen screen passes, an appropriate conclusion is:

> The fixed model passed the predeclared numerical forecasting screen on eligible Miami historical event-days in both test quarters. This is promising exploratory historical evidence. Historical per-run weather publication timing remains assumed, bootstrap inference is approximate, and the study was selected after an inconclusive first attempt. The result is not fully validated contemporaneous forecasting, AI-specific improvement, executable profit, or project viability.

If it fails, report the actual direction, magnitude, uncertainty, failed criterion, and coverage without substituting pooled performance or a sensitivity result for the primary rule. Do not call an inconclusive test proof that the effect is absent.

Regardless of score, the next evidentiary step for stronger confirmation is a separately specified prospective evaluation that records each source value and its actual receipt time before the decision. No result authorizes trading, spending, repository setup, or a production engine.
