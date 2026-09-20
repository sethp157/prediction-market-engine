# Next evidence requirements — prospective confirmation

Prepared: 2026-09-19 12:09:29 UTC.
Status: evidence checklist, not a frozen protocol, registered third study, or instruction to start collection.

The two historical studies can identify limitations and, if their rules are met, a candidate worth further investigation. They do not supply prospective confirmation. Complete and report both studies before selecting any next candidate. A failed or inconclusive batch may justify stopping; this checklist does not require another experiment or a positive result.

The actual candidate, eligible contracts, timing, effect hurdle, statistical design, and study duration remain unselected. They must be reconciled with the historical findings and current source/contract feasibility before a new protocol is frozen. Do not copy historical parameters into a new study merely because they are already implemented.

## 1. Verify the target and its current rules

Before declaring a prospective outcome, obtain the applicable primary venue rules and retain their content, retrieval time, URL, and version or content hash. Verify:

- The exact settlement provider and authoritative publication. Do not assume a current contract still uses the provider used by historical contracts.
- The named station/location and measurement identifier; a city label alone does not establish station identity.
- The measured quantity, units, rounding conventions, daily measurement window, timezone, daylight-saving or local-standard-time treatment, and bin boundaries.
- Resolution timing, preliminary versus revised measurements, corrections, disputes, cancellations, voids, defaults, and any rule-change process.
- The public access and retention conditions needed to preserve an auditable record.

Store the rules applicable at prediction time and any subsequent changes separately. Predefine how changes affect eligibility and claim scope without selecting a rule after its impact on scores is known. If the target changes materially, revise the candidate before collection or treat the affected evidence according to the frozen amendment policy.

A weather forecast may legitimately predict a differently defined settlement quantity. State that difference explicitly; do not claim target equivalence from a common city name or a successful fit.

**Required artifact:** versioned target/rules specification, source/station mapping, and unresolved-feasibility register.

## 2. Capture actual information availability

For every source value, record the source/model identifier, initialization time, forecast-valid time or interval, exact retrieval request, request-start time, response-completion/receipt time, response status, original bytes or permitted audit record, and a content hash. Retain revisions as separate versions.

Initialization time and forecast-valid time are not publication or receipt times. Use values actually received before their legitimate use in generating the forecast. An assumed publication lag cannot substitute for this record. Specify clock synchronization, timestamp precision, timezone, and what happens when clocks or retrievals fail.

For the market comparator, retain the contemporaneous event/bin listing and the actual quote fields used, quote timestamps where provided, receipt times, and the chosen mapping to probabilities. Record source freshness limitations. A quote is a forecasting input, not proof that a trade could fill.

Record forecast-generation start and completion, the information cutoff, decision time, method version, source versions, and the complete output vector. Match the candidate and benchmark to the same target and declared opportunity. Data arriving after the permitted cutoff must not enter that prediction.

**Required artifact:** append-only receipt, input, and forecast records with hashes and explicit timestamp semantics. Distinguish locally timestamped records from independently timestamped registration; do not claim stronger tamper resistance or historical availability than the records establish.

## 3. Freeze the candidate before fresh outcomes

Select and freeze a complete forecasting procedure: source product and station, timing/horizon, admissible inputs, transformations, fitted parameters, probability construction, fallback/abstention behaviour, and exact code/configuration versions. Record its training-data provenance and the historical selection process that led to it.

Freeze the primary benchmark, primary loss, event weighting, minimum worthwhile forecasting effect, supporting metrics, and decision rules before the prospective evaluation outcomes exist. Supporting metrics must not replace a failed primary rule. A scientific score hurdle is not a monetary viability threshold.

The prospective evaluation must use new outcomes. Previously exposed historical cases may inform development and planning, but cannot be relabeled untouched confirmation. If a material method change uses prospective results, those results become development evidence for the revised method; obtain new confirmation.

**Required artifact:** linked hypothesis and frozen protocol, candidate/benchmark versions, data-exposure ledger, and a dated freeze record.

## 4. Fix eligibility, grouping, coverage, and the endpoint

Define eligibility using information available at the decision, with a complete calendar or other prospective opportunity register. Preserve scheduled opportunities with no available contract, missing source data, invalid quotes, late or failed forecasts, abstentions, and non-resolving outcomes. Record overlapping failure reasons.

Specify whether the primary claim concerns all scheduled opportunities, successful forecast coverage, or another declared population. Define denominators and how exclusions affect the estimand. Coverage alone does not justify a missing-at-random assumption. Outcome-driven exclusions are prohibited.

Group all bins of one event, repeated forecasts of that event, and relevant related events. Justify treatment of shared weather systems, dates, stations, and market dependencies; neither a different city nor another forecast row guarantees independence.

Choose a fixed calendar endpoint or another fully prespecified stopping design before evaluation. Define late-settlement handling and a reporting cutoff. Do not extend the sample because a result is nearly significant, exclude difficult dates after their outcomes, or stop early after a favourable run.

**Required artifact:** opportunity register, grouping/weighting rules, coverage/missingness rules, resolution policy, and fixed stopping/reporting specification.

## 5. Justify uncertainty and required evidence

Specify the population effect, null/alternative, practical hurdle, error standard, confidence-bound construction, dependence assumptions, multiplicity treatment, and any replication claim. Choose these together rather than treating a nominal confidence level as proof of valid coverage.

Determine duration and required observations from a documented power or precision analysis that accounts for dependence, coverage loss, settlement delay, and plausible effect/variance ranges. Do not invent a numerical sample target here. Historical estimates used for planning carry selection uncertainty and may overstate the effect of the selected candidate.

If repeatability is claimed, predeclare the relevant validation periods or groups and their success requirements. A pooled average cannot establish a stronger claim about every component. Explain which conclusions remain possible if coverage or effective sample size is inadequate.

Disclose both historical attempts and the selection of the next study. Do not retroactively allocate error allowances or advertise a research-program-wide error guarantee without a design that supports it.

**Required artifact:** statistical analysis plan, power/precision rationale, declared inference limitations, and explicit supported/inconclusive/contrary/invalid evidence rules.

## 6. Prevent outcome-driven adaptation during collection

Separate operational monitoring from performance inspection. Operational checks may verify receipt, schema, timestamps, forecast production, and coverage. Do not repeatedly inspect accumulating outcomes, paired score gains, intervals, or pass/fail status unless a valid sequential design was explicitly frozen in advance.

Preserve all registered forecasts, failures, amendments, and exposed results. Record what prompted every change and when outcomes became accessible. An implementation defect requires an exposure assessment; a repaired calculation must not be represented as if its decision rule were selected without knowledge of the results.

Before evaluation, independently review code and source/protocol conformance. At the fixed endpoint, recompute deterministic results from retained inputs, reconcile counts, report every prescribed metric and replication block, and disclose deviations.

**Required artifact:** monitoring boundaries, amendment/exposure log, independent review, reproducibility record, and complete final report.

## 7. Keep economic confirmation separate

Even a successful prospective forecast comparison would establish only its scoped forecasting claim. Economic evidence additionally requires a separate, explicit policy; actual payoff/rule accounting; credible execution and joint fill/outcome evidence; spread/fees/slippage without duplication; operating/research expenses; capacity; funding and capital-time conventions; risk constraints; and an economically worthwhile hurdle.

Observed or modeled forecast improvement is not executable profit. A simulated transaction result must retain its assumptions and cannot be presented as achieved live performance. This checklist does not authorize a trading policy, paper-trading validation program, account activity, or live orders.

**Required artifact before any economic claim:** a separately justified economic protocol and evidence sufficient for its accounting, feasibility, uncertainty, and risk claims.

## Scope and decision authority

[D0003 / AMEND-05](decisions/D0003-delegated-research-authority.md) permits documented agent research decisions within the user's delegated scope; no separate approval is needed merely to discuss or resolve another Level-1 research question. A further bounded study requires a new rationale and fresh evidence plan rather than continuation solely to obtain a positive result.

This document does not launch a job or build a repository or evaluation engine. Unattended recurring collection, paid commitments, account changes, or trading remain outside the delegation and require a separate explicit user request or authorization for the concrete activity. Do not create a recurring task from this checklist. Repository setup is now authorized by [D0007](decisions/D0007-repository-handoff.md); production-engine development remains deferred. The current task is handoff, not prospective collection or the canceled diagnosis.

Once both historical studies and source feasibility have been assessed, record whether the next justified action is prospective study design, additional bounded feasibility work, or stopping. Report unresolved evidence honestly; do not ask for broad future permissions before a concrete need exists.

