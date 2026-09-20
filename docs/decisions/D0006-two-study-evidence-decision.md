# D0006 — Initial two-study evidence decision

Recorded 2026-09-19 UTC. Agent decision under [D0003](D0003-delegated-research-authority.md), after both frozen historical evaluations. This is a research decision, not a new user approval or a claim of economic viability.

## Decision

**REVISE the research direction; STOP this two-study evaluation as specified. Neither candidate established its registered forecasting claim. Do not advance to trading or production-engine development.**

The completed result is an auditable historical comparison, including inconclusive and adverse evidence. The desired positive, validated edge has not been obtained. No further family, horizon change, threshold relaxation, date extension, or favorable-quarter substitution is permitted inside these studies.

## Evidence

| Study | Held-out sample | Pooled market loss | Pooled candidate loss | Paired gain | Registered result |
| --- | ---: | ---: | ---: | ---: | --- |
| EXP-0001: NYC market calibration, beta=1.25 | 180 eligible days / 181 expected | 0.1171398353 | 0.1167570661 | 0.0003827692 | Coverage passed; both quarterly lower bounds failed the 0.001 hurdle |
| EXP-0002: Miami weather plus market, bias +1 F, dispersion 1.5 F, weather weight 0.5 | 150 / 181 | 0.1049020134 | 0.1048848131 | 0.0000172002 | Quarterly gain did not replicate; lower bounds failed; second-quarter coverage failed |

The unit is mean binary Brier loss per event-day, averaging across the complete bins and then equally across days. It is not money. The two cities share calendar periods; do not pool their counts as independent replication.

NYC quarter gains were 0.0003870712 and 0.0003784671. Their approximate one-sided 95% lower bounds were -0.0015649569 and -0.0010104411. Both quarter point estimates were below the hurdle, and the bounds include no gain. The study is inconclusive about a worthwhile advantage, not proof that none can exist.

Miami quarter gains were -0.0017125805 and 0.0024723728. Their approximate one-sided 97.5% lower bounds were -0.0062635009 and -0.0035430768. Its second test quarter retained 62/91 days (68.13%), below the predeclared 70% minimum. The positive second-quarter estimate cannot replace the failed replication or coverage requirements. Training improved by 0.0059965563, but validation worsened by 0.0087676837; the configuration was not changed after those later scores.

The primary uncertainty procedure was the frozen 14-day circular calendar-block percentile bootstrap with 10,000 resamples and fixed seeds. Its assumptions and approximation remain limitations. The 7-day sensitivity is descriptive. The second study was selected after the first result, and its stricter bound does not establish a program-wide 5% error guarantee.

## Evidence quality and material limitations

The source hashes, exact request URLs, chronological splits, training-only selection, locked dependencies, coverage rules, and independent pretest review are recorded in each study package. Arithmetic checks are documented separately; passing arithmetic and code checks does not make a forecasting hypothesis pass.

The Miami archive supplied every requested MOS response, and the analysis found all 365 required forecasts valid. Its archived market rules explicitly identify Miami International Airport and the National Weather Service Climatological Report (Daily). The missing market quote windows, not missing MOS forecasts, account for most exclusions. Excluded dates remain in the coverage ledger; their performance is unknown under this protocol.

MOS initialization/valid times are verified fields, while historical publication at runtime + six hours is an assumption. The daytime-maximum predictor and market settlement target are not identical by definition. Both studies also retain limits on original rule versions, deleted listings, actual quote freshness, and candle publication latency.

The Miami collector completed during an interruption. A proposed high-resolution-clock fix was not applied; it must not be described as completed. Recorded minimum request-start gaps were approximately 0.2482 seconds for Kalshi and 0.9968 seconds for IEM, so exact compliance with the declared subsecond rate ceilings cannot be certified and a small operational deviation is possible. Raw data and timing records are preserved. This issue does not alter the scores or cure historical information-timing uncertainty.

No historical LLM event forecasts, simulated executions, live fills, fees, capital policy, or net-profit accounting were evaluated. No AI-specific uplift, executable advantage, or economic viability is established.

## Durable claims and exposure

- **SUPPORTED:** These two fixed candidates did not meet their declared research screens on the retained archived data.
- **SUPPORTED:** The scripts and retained data provide an auditable comparison within their declared scope; independent checks are recorded, with their limits.
- **NOT ESTABLISHED:** A worthwhile, repeatable forecasting advantage for either candidate.
- **UNTESTED:** AI-specific improvement, executable expected profit, risk-adjusted performance, and whole-project viability.
- **UNVERIFIED ASSUMPTIONS:** Exact historical source availability and nominal bootstrap coverage under the relevant dependence/stability conditions.

EXP-0001 test scores were exposed at 2026-09-19T03:03:40.784147+00:00. EXP-0002 test scores were exposed at 2026-09-19T21:09:39.252974+00:00. Both full July 2025–June 2026 populations are now development/exposed evidence for any revised procedure. Neither may be relabeled an untouched holdout.

## Next permitted work

Present the combined report and retain the audit package. Clarify or explain findings within current delegation. A new empirical study needs a distinct scientific rationale, a new frozen design, and fresh confirmation; it should not be launched merely to obtain a positive result. The [next evidence requirements](../NEXT_EVIDENCE_REQUIREMENTS.md) identify the unresolved target, receipt, power, grouping, coverage, and economic requirements. They are not a third-study registration or active collection schedule.

Repository and production-engine deferral remains. Any future recurring collection, paid commitment, account activity, or trading lies outside the present authorization. No such work is running.

See the [combined report](../../research/RESEARCH_REPORT.md), [EXP-0001 package](../../research/EXP-0001/README.md), [EXP-0002 package](../../research/EXP-0002/README.md), and [current research state](../../RESEARCH_STATE.md).
