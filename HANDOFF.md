# Agent handoff

Updated: 2026-09-19 23:59:51 UTC. Start with this file and the four governing documents.

## Latest task and authority

The user replaced the proposed diagnosis with repository setup and handoff:

> Actaully scratch that, set up the repo here: [https://github.com/sethp157/prediction-market-engine](https://github.com/sethp157/prediction-market-engine) document everything accordingly ready for handoff to antoher agent. add all current documentation

[D0007](docs/decisions/D0007-repository-handoff.md) records this instruction. Repository setup and importing the current documentation/evidence are authorized. The earlier repository deferral is superseded for that work. The repository's name does not authorize building the evaluation engine.

Production-engine development, trading, paid commitments, account activity, and recurring collection remain outside the current task. Do not create another agent task or resume a research job merely because this is a handoff.

**Diagnosis / DIAG1 was not completed.** It was interrupted before diagnostic findings, and the latest instruction replaced that work. There is no completed diagnostic conclusion, revised method, or third-study result to inherit.

## Read in this order

1. [AGENTS.md](AGENTS.md), [charter](prediction_market_research_charter_v2.md), [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), and [RESEARCH_STATE.md](RESEARCH_STATE.md).
2. [Combined research report](research/RESEARCH_REPORT.md) and [D0006 evidence decision](docs/decisions/D0006-two-study-evidence-decision.md).
3. [D0003 delegated authority](docs/decisions/D0003-delegated-research-authority.md), [D0007 latest task](docs/decisions/D0007-repository-handoff.md), and the relevant study's protocol before interpreting its results.

Files under docs/original and docs/history preserve prior states. They are evidence of the history, not current instructions. Frozen study records describe what was decided and run at the time; do not rewrite them to match a later objective.

## Evidence at handoff

Neither candidate established its registered replicated forecasting claim. This is a completed negative/inconclusive research batch, not evidence of economic viability.

| Study | Fixed candidate | Test coverage | Pooled paired Brier gain | Outcome |
| --- | --- | --- | ---: | --- |
| EXP-0001 / NYC | Market-probability exponent beta = 1.25 | 180/181 eligible days | 0.0003827692 | Both quarterly lower bounds failed the 0.001 hurdle; sample/coverage minimums passed |
| EXP-0002 / Miami | Bias +1 F, dispersion 1.5 F, 50% MOS weather / 50% market | 150/181 eligible days | 0.0000172002 | Both quarterly bounds failed; Test B coverage was 62/91 = 68.13%, below 70% |

Gain means normalized-market Brier loss minus candidate Brier loss, averaged equally across eligible event-days. It is not a return or monetary profit. Individual brackets are not independent event outcomes.

Miami's quarterly gains had opposite signs. Its favourable second-quarter estimate cannot replace the failed quarterly replication and coverage criteria. NYC's small positive estimates were uncertain. Do not reinterpret either result as a validated edge or as proof that all possible advantages are absent.

The original objective remains repeatable economic viability. AI-specific predictive contribution, executable fills, fees, capital/risk, capacity, and total-cost viability were not tested.

## Exposed data and fixed stopping boundary

Both studies covered target dates July 2025–June 2026:

- Training: July–October 2025; validation: November–December 2025.
- Test A: January–March 2026; Test B: April–June 2026.
- NYC tests were scored at 2026-09-19T03:03:40.784147+00:00.
- Miami tests were scored at 2026-09-19T21:09:39.252974+00:00.

These populations are now exposed development evidence for any changed method. Numerical replay is not fresh confirmation. No third family, altered horizon, or date extension belongs to the completed batch. The canceled diagnosis does not reopen these tests.

## Material limitations to retain

- Miami used archived NOAA GFS MOS forecasts. Runtime + six hours was an availability assumption, not a historical per-run receipt record. Its daytime-high predictor differs from the settlement-day target.
- Archived Miami rules name Miami International Airport and the National Weather Service daily climatological report. Verify current provider, station, and rule versions before any future work; do not assume today's contracts are unchanged.
- Original rule revisions, deleted listings, actual quote freshness, and candle publication latency are not fully certified.
- Effects concern eligible archived days; coverage does not establish random missingness.
- Calendar-block bootstrap inference is approximate. The stricter second-study screen does not provide a program-wide 5% error guarantee.
- Miami was selected after NYC's result. Both cities share calendar periods; do not claim their samples are independent.
- The Miami collection audit preserves a possible small request-rate deviation. A proposed clock change was not executed.
- Review by another agent and numerical agreement are audit checks, not external scientific replication.

## Evidence paths and reproduction

**Restore the archived data first:** run `pwsh -File audit/Restore-Evidence.ps1` from this repository root. [audit/README.md](audit/README.md) explains the numbered archive parts, SHA-256 verification, and refusal to overwrite differing files. Large raw responses, prepared inputs, and source manifests are stored in that archive because of upload-size limits; their uncompressed bytes and paths are unchanged. The commands below assume restoration is complete.

- [EXP-0001 README](research/EXP-0001/README.md) and [EXP-0002 README](research/EXP-0002/README.md): inventories, dependency versions, provenance limits, and replay instructions.
- Each study's protocol.md, protocol-freeze.json, fit-lock.json, results.json, request-manifest.jsonl, coverage.csv, and per-event-results.csv are the primary audit records.
- Each raw/ directory contains the retained source responses. Preserve them and their hashes.
- Independent arithmetic reviews report maximum point-score differences of 2.78e-17 for NYC and 8.33e-17 for Miami.

For Miami's read-only point-score check, from this repository root using Python 3.12:

```powershell
python -B research/EXP-0002/independent_numeric_check.py
```

This checker does not recompute bootstrap intervals or verify historical publication timing. It does not refit or collect data.

For a full replay, follow the relevant study README in a **new separate copy**, using that copy's paths. Any historical absolute paths in those instructions identify the original workspace, not a required location for this clone. Use requirements-reproduction.txt and the recorded environment to select compatible dependencies. Do not delete fit/results files from the committed audit copy to bypass run guards.

Do not run collect.py to reproduce existing findings: it contacts sources and may retrieve changed archive data. A replay may change execution timestamps and derived hashes while reproducing the same numbers; retain the originals for comparison.

## Next agent's assignment

Orient from the files above, verify the latest requested scope, and preserve the completed research record. Explanation, handoff maintenance, and bounded integrity checks remain appropriate. There is no active third experiment, diagnosis, recurring job, or implementation task to resume.

Before new substantive research, identify a concrete question tied to fresh user direction or a specifically justified action still authorized by [D0003](docs/decisions/D0003-delegated-research-authority.md). Do not automatically revive the canceled diagnosis or search exposed data for a positive result. If the user asks for diagnosis later, label it exploratory and keep it separate from validation of a revised candidate.

[Next evidence requirements](docs/NEXT_EVIDENCE_REQUIREMENTS.md) is a prospective evidence checklist, not a frozen study or instruction to launch collection. No per-question approval ritual is required within existing delegated scope, but the latest task replacement and explicit limits remain controlling.
