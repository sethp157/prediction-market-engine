# Research state

Updated 2026-09-20 UTC (2026-09-19 America/Chicago). Repository setup and handoff are authorized by [D0007](docs/decisions/D0007-repository-handoff.md); start with [HANDOFF.md](HANDOFF.md). The user canceled the proposed diagnosis before findings. Initial two-study evaluation **complete**; scientific conclusions remain in the [combined report](research/RESEARCH_REPORT.md) and [D0006](docs/decisions/D0006-two-study-evidence-decision.md). Prior states are preserved in docs/history and are not current scope instructions.

## Current position and authority

| Field | Status |
| --- | --- |
| Current phase | Documentation/evidence repository setup and agent handoff; no transition to trading or production-engine development |
| Evidence conclusion | Neither candidate established its registered forecasting claim |
| Scientific decision | REVISE research direction; STOP this initial two-study evaluation under its frozen stopping rules |
| Q1 | Framing and four amendments approved directly by user in D0001 |
| Q2 | Definitions adopted under delegated authority in D0003 |
| Q3–Q10 | Operationalized for the two studies in D0004/D0005; economic and prospective requirements remain open |
| Current charter | Revision 2.4: D0007 repository authorization plus existing AMEND-05 research delegation |
| Forecasting advantage | Not established; positive point estimates do not satisfy validation criteria |
| Economic viability / AI-specific uplift | Not tested or established |
| Repository / production evaluation engine | Repository established at sethp157/prediction-market-engine for handoff; production engine not built and remains deferred |
| Live, paid, or recurring activity | None performed or active |

The user's instruction “can we proceed until you have promising reslts that are validated and presentabke” is recorded in [D0003](docs/decisions/D0003-delegated-research-authority.md). It authorizes bounded free research, necessary one-off calculations, review, and reporting without repeated question-level approvals. D0007 is the latest instruction: repository setup and handoff replace the diagnosis task and supersede “we will build repo later” for repository setup only. Production-engine development remains deferred. No Q2 approval is pending.

The user did not individually choose the cities, thresholds, grid, or statistical method. These are documented agent decisions under delegation. A desire for positive results does not authorize suppressing failures, relaxing frozen criteria, or extending a test until it passes.

## Completed findings

| Study | Frozen candidate | Pooled eligible test days | Market Brier | Candidate Brier | Paired gain | Result |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| EXP-0001 / NYC | Market-only exponent beta=1.25 | 180/181 | 0.1171398353 | 0.1167570661 | 0.0003827692 | Inconclusive; both quarterly lower bounds fail 0.001 |
| EXP-0002 / Miami | Bias +1 F, dispersion 1.5 F, 50% weather / 50% market | 150/181 | 0.1049020134 | 0.1048848131 | 0.0000172002 | No replicated gain; quarterly bounds fail; second-quarter coverage fails |

Loss is averaged across the complete bins and then equally across event-days. Gain is market loss minus candidate loss, not money. The populations share calendar dates; do not combine these counts as independent replications.

NYC test-quarter gains were 0.0003870712 and 0.0003784671. Approximate one-sided 95% lower bounds were -0.0015649569 and -0.0010104411. Both estimates were below the scientific hurdle, with uncertainty crossing zero. Minimum coverage passed.

Miami gains were -0.0017125805 and 0.0024723728. Approximate one-sided 97.5% lower bounds were -0.0062635009 and -0.0035430768. The later quarter retained 62/91 days (68.13%), below the preset 70% minimum. Its positive point estimate cannot replace the failed quarterly replication and coverage requirements. All 365 requested MOS predictors passed the declared source-content checks; most exclusions came from market quote windows.

Both analyses used the frozen 14-day circular calendar-block bootstrap, 10,000 resamples, and fixed seeds. Seven-day sensitivity results are retained but did not decide success. The inference is approximate and assumption-dependent. The stricter second-study screen does not provide a program-wide 5% error guarantee.

## Validation and provenance

- EXP-0001: 2,201 raw response files verified; 357 eligible events across all splits. Independent point-score recomputation agreed to maximum absolute error 2.78e-17.
- EXP-0002: 2,563 raw responses verified, comprising seven metadata pages, one cutoff response, 2,190 candle responses, and 365 MOS responses; 321 eligible events. Independent stdlib erf/fsum score recomputation agreed to 8.33e-17.
- Protocols were locally frozen before study outcome retrieval; exact source URLs and hashes, coverage ledgers, fit locks, pretest reviews, all training-grid scores, results, and reproduction scripts are retained in the [NYC](research/EXP-0001/README.md) and [Miami](research/EXP-0002/README.md) packages.
- NYC protocol SHA256: DCA4B858076C254585E2F0E28399826555AB56A0BD3029F941C64B19BE26FD30. Miami: D7672BF369CF297CFA4B87B92BE8396A05C09E4E81B2CC6E16B0C3FA395DF098. Exact freeze records accompany the studies; local records are not independent public timestamp registrations.
- Miami's [pre-exposure clarification](docs/decisions/EXP-0002-clarifications.md) records multiplicity and timing limits without changing numerical criteria. Pretest code review passed before scoring, and no selected parameter was refitted on validation or test data.
- The Miami [collection audit](research/EXP-0002/collection-audit.md) confirms all archived rules name Miami International Airport and the National Weather Service Climatological Report (Daily). It preserves a possible small request-rate deviation: recorded minimum gaps were about 0.2482s and 0.9968s, and exact ceiling compliance cannot be certified from the clock readings. A proposed clock fix never executed before collection completed; no raw data were rewritten or redownloaded.

Arithmetic and implementation checks support the accuracy of the reported comparisons. They do not establish the forecasting hypothesis, historical publication timing, nominal statistical coverage, executable profit, or external replication.

## Decision register

| ID | Subject | Current status |
| --- | --- | --- |
| [D0001](docs/decisions/D0001-primary-research-claim.md) | Q1 forecast-first framing and AMEND-01–04 | APPROVED directly by user; applied |
| [D0002](docs/decisions/D0002-meaning-of-edge.md) | Forecast/economic definitions and monetary accounting | ADOPTED under D0003 delegation; original proposal retained as history |
| [D0003](docs/decisions/D0003-delegated-research-authority.md) | AMEND-05 continued bounded research | Effective authority; no repeated question-level approval required within scope |
| [D0004](docs/decisions/D0004-initial-validation-protocol.md) | EXP-0001 frozen design | Completed, inconclusive; pre-exposure amendment retained |
| [D0005](docs/decisions/D0005-external-weather-study.md) | EXP-0002 frozen design | Completed, screen failed; exploratory historical classification retained |
| [D0006](docs/decisions/D0006-two-study-evidence-decision.md) | Evidence synthesis and stopping decision | REVISE direction; stop this batch; no advancement to trading/build |
| [D0007](docs/decisions/D0007-repository-handoff.md) | Latest direct repository/handoff instruction | Repository setup authorized; diagnosis canceled before findings; production engine deferred |

## Exposure ledger and stopping boundary

| Data | Exposure / use |
| --- | --- |
| NYC July 2025–June 2026 | Train/validation used as declared; final tests scored 2026-09-19T03:03:40.784147+00:00 |
| Miami July 2025–June 2026 | Protocol frozen 2026-09-19T03:09:56.6142833Z after NYC result; train-only fit locked 2026-09-19T21:09:09.289488+00:00; tests scored 2026-09-19T21:09:39.252974+00:00 |
| Feasibility probes | July 2026 events outside study windows; schema/source feasibility only; raw metadata returned labels but these were not used to select a model by performance |
| Future confirmation | None collected; no prospective or recurring job active |

Both study populations are now exposed development evidence for any revised procedure. Do not call a revised forecast's performance on them untouched validation. No third family or date extension is permitted within this initial two-study evaluation.

## Knowledge log

| ID | Statement | Kind / status | Evidence and limitations |
| --- | --- | --- | --- |
| OBS-001 | Founding documents contained conflicting Q1 completion/dependency requirements and other specification gaps | SUPPORTED document finding; core conflicts resolved | [Founding audit](docs/ORIGIN_REVIEW.md), approved amendments and current charter |
| CLM-001/002 | Paired Brier improvement measures a declared forecast-loss difference but need not imply profitable execution | SUPPORTED mathematical claims under stated setup | D0001/D0002 derivations; do not validate empirical assumptions |
| CLM-003 | Adaptive holdout use can undermine generalization claims | SUPPORTED methodological concern | D0001 and exposure ledger; repeated tests cannot be hidden |
| CLM-004/005 | Fill conditioning and complete, nonoverlapping cash-flow accounting matter for expected profit | SUPPORTED mathematical/accounting claims | D0002; market-specific values remain unestimated |
| OBS-002 | Neither fixed candidate met its registered historical reporting rule | SUPPORTED empirical observation | D0006 and exact retained results; scope limited to eligible archived populations |
| H-F-NYC | NYC transformation supplies a worthwhile replicated forecasting gain | NOT ESTABLISHED; inconclusive | Small positive estimates and bounds crossing zero/hurdle; not proof of universal absence |
| H-F-MIA | Fixed weather mixture supplies a worthwhile replicated forecasting gain | NOT ESTABLISHED | Mixed quarterly results, uncertain estimates, failed coverage; historical availability also assumed |
| ASSUMP-MOS | Prior-day 06Z MOS is available by runtime + six hours | UNVERIFIED per-run availability assumption | Source timing literature is not a historical receipt ledger; score cannot verify it |
| H-ECON | A repeatable, economically worthwhile executable edge exists | UNTESTED / NOT ESTABLISHED | No fills, fees, capital/risk, total-cost, or worthwhile monetary threshold evidence |
| H-AI | An AI model adds predictive value over the market | UNTESTED | AI designed/reviewed deterministic methods; no LLM event-forecast comparison |

## Remaining evidence and next permitted action

Finish or maintain the repository handoff and respond to the next concrete user direction. No diagnosis or third study is active. Retain the completed scientific no-advancement decision. A future research cycle needs a distinct rationale and fresh evidence plan, not continuation solely to seek significance. [Next evidence requirements](docs/NEXT_EVIDENCE_REQUIREMENTS.md) is a concrete checklist, not a frozen third study or instruction to start jobs.

Stronger forecasting confirmation requires current rule/provider/station checks, actual contemporaneous receipt records, a fully frozen candidate/benchmark, fresh outcomes, justified power or precision, fixed stopping and coverage rules, and appropriate dependence/multiplicity treatment. Retrospective deleted listings, original rule versions, quote freshness and publication timing remain limited here.

Economic claims additionally require executable prices and joint fill/outcome evidence; actual fees and costs without double counting; explicit capital, risk, capacity and accounting conventions; and a worthwhile monetary hurdle. These dependencies are recorded, not resolved by the historical forecast tests.

No further user decision is required for the authorized repository/documentation handoff. Recurring work, paid commitments, production-engine implementation, or trading remain outside current scope. No such work is running. No separate agent task is automatically created by the handoff.

## Files and session close

Repository delivery uses directly browsable documentation plus a [verified archive](audit/README.md) for large evidence files. Run `pwsh -File audit/Restore-Evidence.ps1` before full audit or replay. The root package manifest covers committed delivery files; study manifests cover the restored scientific files. Archive packaging changes storage only, not results or source bytes. Native Git initially used a saved account without write access; the authorized connected GitHub app is used for publication.

The original ZIP at C:\Users\sethp\Downloads\prediction-market-starter.zip and extracted original documents remain unchanged. Original ZIP SHA256: F69F6BE597F2556F7DCAB9575C7F2D511D6BDFD50B3BE74781990BB1BA7A2501. Historic Q1/Q2 ZIPs remain in the original workspace; all current documentation and extracted original documents are included here. This repository contains governing documents, decisions, report, charts, raw evidence, reproduction instructions, and manifests. No production evaluation engine was created. Pre-repository governing documents and the earlier package manifest are retained under docs/history/pre-repository-handoff; frozen study bytes remain unchanged.
