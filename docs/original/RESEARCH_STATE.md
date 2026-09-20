# Research state

Updated: 2026-09-17

## Current position

| Field | Status |
| --- | --- |
| Phase | Phase 0 — problem definition |
| Active question | Q1: What exactly are we trying to prove? |
| Governing charter | [Charter, revision 2.1](prediction_market_research_charter_v2.md) |
| Confirmed priority | Test viability first; learning and portfolio value are secondary |
| Research gates approved | None |
| Experiments run | None |
| Datasets or test results exposed | None in this starter package |
| Code or execution authorized | Documentation and Q1 research only |

The priority above comes from the user's explicit selection during starter-package preparation. It does not close Q1 or approve a phase transition. These files are a starting protocol, not completed research.

## Next permitted action

Read all four governing files, identify any conflicts, and complete the Q1 analysis requested by charter section 14. Create `docs/decisions/D0001-primary-research-claim.md` only when preparing that proposal; use the charter's decision template.

Q1 should identify the candidate claim, dependent variable, population and horizon placeholders, falsification conditions, and dependencies. Propose a primary direction without claiming that later benchmark, effect-size, market-selection, or evaluation gates have been settled.

## Open questions

| ID | Question | Status |
| --- | --- | --- |
| Q1 | What specific, falsifiable claim should this program test first? | Active; unresolved |
| Q1-D1 | Which definitions and evidence needed to finalize that claim belong to later questions? | To identify during Q1 |

## Decision register

No research decision has been approved. For each future record, distinguish `PROPOSED` from `APPROVED` or `DECLINED`, record the agent's recommendation separately, and link the actual user approval. Supersede decisions explicitly when scope changes.

## Knowledge log

No empirical finding has been established. Add material entries with:

| ID | Statement | Kind and status | Evidence/derivation | Scope and limitations | Implication |
| --- | --- | --- | --- | --- | --- |

Use kinds such as claim, assumption, or observation. Status rules are in `AGENTS.md`. Do not turn unresolved assumptions into supported claims by copying them into this log.

## Session handoff

- Completed: starter documents prepared; viability-first priority recorded; gate authority and exploration rules clarified.
- Not completed: Q1 analysis, external evidence collection, data validation, experiments, implementation.
- Blockers: none for starting Q1. The user's decision will be needed to close it.
- Next action: prepare Q1 and its proposed decision record; stop before advancing to Q2.

## Starting prompt

> Read AGENTS.md, prediction_market_research_charter_v2.md, PROJECT_CONTEXT.md, and RESEARCH_STATE.md. Follow the charter's Q1-only first task. Identify conflicts, decompose Q1, define candidate mathematical hypotheses and undefined quantities, and prepare a proposed decision record with evidence requirements. Record dependencies on later questions without resolving them. Update RESEARCH_STATE.md and stop for my decision before Q2. Do not build the evaluation engine yet.
