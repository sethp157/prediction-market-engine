# D0001 — Primary research claim (approved framing)

Prepared: 2026-09-17 UTC (2026-09-16 America/Chicago).
Scope: Q1 framing and authorized transition to Q2. Record status: APPROVED. Protocol status: NOT SPECIFIED / NOT FROZEN.

| Authority field | Value |
| --- | --- |
| Agent recommendation | ADVANCE on the limited terms below |
| User decision | APPROVED — Q1 framing, AMEND-01 through AMEND-04, and Q2-only continuation |
| User instruction / approval date | “okya begin on your recomneded we will build repo later” — recorded 2026-09-17 UTC (2026-09-16 America/Chicago) |
| Gates currently approved | Q1 claim framing only; no empirical claim or experiment approved |
| Next question permitted now | Q2 research and documentation, then its user decision gate |
| Implementation scope | Apply the approved charter clarifications; defer repository setup, software scaffold, and evaluation engine |

## Approval record

The user accepted the preceding recommendation to approve D0001 and its four amendments for Q2-only continuation, adding that the repository will be built later. This is the direct authorization for the transition; it is not inferred from a state summary. AMEND-01 through AMEND-04 have been applied in charter revision 2.2. Routine resume notes in AGENTS.md and PROJECT_CONTEXT.md were updated to reflect this instruction. No experiment or frozen protocol existed, so no empirical result requires reclassification.

The analytical proposal below is retained as the rationale for the approved framing. Its references to candidate hypotheses and unresolved quantities remain applicable. Approval does not establish that those hypotheses are true or bind later parameters.

## Question and proposed answer

What specific claim should we investigate first, while retaining economic viability as the ultimate objective?

**Recommendation:** First investigate whether a specified, versioned AI-assisted forecasting procedure improves expected forecast quality by more than a predeclared worthwhile amount relative to a matched, available-at-decision market benchmark in a bounded target population. Use paired Brier-loss improvement as the proposed primary dependent variable. Require separate later evidence of feasible net economic value and repeatability before describing the project as viable.

This approved framing chooses a research direction. It is not a claim that an edge exists. The benchmark role is accepted here; its construction is not selected. The method, market universe, horizons, effect thresholds, and evaluation protocol remain unbound. These are candidate mathematical hypotheses, not ready-to-run tests.

The approved recommendation includes the four wording amendments in [REVIEW-0001](../ORIGIN_REVIEW.md). In particular, AMEND-01 reconciles Q1's required benchmark/effect choices with section 14's instruction to defer them. The clarification is now applied; no unbound empirical parameter is being treated as settled.

## Why it matters

The founding objective is repeatable economic viability, not a particular income target or a software deliverable. A forecast-quality claim offers a measurable first question without inventing a trading policy. It is a chosen research pathway, not a theorem that aggregate forecast superiority is necessary or sufficient for every profitable strategy. Failure would bear on this method and claim in this population; it would not prove that all prediction-market opportunities are absent.

The whole versioned method is the object being tested. Improvement over a market benchmark would not, by itself, prove that the AI component caused that improvement. That stronger attribution requires a separate comparison.

## Q1 decomposition

| ID | Level-2 question | Proposed Q1 answer or required output |
| --- | --- | --- |
| Q1.1 | What is the ultimate objective and the first claim? | Economic viability is the objective; bounded market-relative forecast improvement is the proposed first claim. |
| Q1.2 | What exactly is being compared? | A complete versioned forecasting procedure M against a benchmark procedure B, matched on event and decision-time opportunity. Actual procedures remain undefined. |
| Q1.3 | Where and when must the claim hold? | A declared target population and horizon policy. No venue, market class, historical interval, or forecast frequency is selected. |
| Q1.4 | What is the dependent variable? | Proposed primary: paired Brier-loss gain D. Expected gain is the population quantity of interest; a sample score difference is its estimate. |
| Q1.5 | How much improvement matters? | Separate a positive forecast-relevance hurdle from a monetary viability hurdle and from the statistically detectable effect. No numbers are selected. |
| Q1.6 | What do economic value, attribution, and repeatability add? | Separate candidate secondary claims and evidence requirements; no substitution of one claim for another. |
| Q1.7 | What would support, contradict, or leave the claim unanswered? | Define conditional evidence interpretations and failure modes; leave inference and stopping rules to later questions. |
| Q1.8 | What closes this task and what remains blocked? | A user decision on claim framing and amendments, with explicit dependency ownership. Final empirical specification and all experiments remain later work. |

## Mathematical form

### Definitions and units

The following setup is conditional on an eligible binary outcome. It does not select binary markets as the actual universe; any broader outcome type would require a revised formulation before testing.

| Symbol | Definition | Units / unresolved aspects |
| --- | --- | --- |
| u, i(u), g(u) | An evaluation opportunity, its event, and its related-event group | Whether u is an event, event-time pair, or within-event aggregate is unresolved. Group membership is unresolved. |
| P | Target distribution over eligible evaluation opportunities and outcomes | Encodes population, sampling, horizon, and weighting; not yet specified. |
| t_u | Declared decision time | Timestamp with a declared timezone and precision, not yet operationalized. |
| a_u, r_u, s_u | Information cutoff, forecast-completion time, and benchmark observation time | Available information must precede its legitimate use; matching, latency, and stale-quote tolerances remain Q3/Q5/Q6 choices. |
| T_u, h_u | Target event time and forecast horizon h_u = T_u - t_u | Time units and event-time definition unresolved; settlement availability may occur after T_u. |
| Y_u | Resolved event indicator, 0 or 1 | Dimensionless. Label provenance, revisions, cancellations, ambiguity, and unresolved outcomes need rules. Opportunities for the same event share an outcome. |
| M, B | Complete versioned forecasting and benchmark procedures | M includes model, prompt, tools, sources, and postprocessing. B's market-price construction remains Q3. |
| I_u^M, I_u^B | Admissible information for each procedure at the declared time | Information policies unresolved; M may or may not use the market forecast, subject to Q5. No independent-information assumption is made. |
| m_u, b_u | M(I_u^M) and B(I_u^B), each in [0,1] | Dimensionless forecast probabilities for the same outcome and horizon. Neither is assumed to be truth. |
| D_u, theta_F | Per-opportunity Brier gain and its expectation under P | Squared-probability score units, dimensionless. |
| delta_F | Minimum worthwhile forecasting improvement | Score-unit hurdle with 0 < delta_F < 1 for this strict alternative; magnitude unselected. It is not a monetary hurdle. |
| pi, v, Q, N_v^pi | Future action policy, economic accounting unit, its target distribution, and net economic result under that policy | Entirely undefined operationally. N must use a common declared currency and accounting convention that treats entry, payoff, execution, and applicable operating costs consistently. |
| theta_E, delta_E | Expected net economic result under Q and minimum worthwhile economic result | Same eventual monetary units per accounting unit. Any capital/time or risk normalization requires an additional definition. |
| K, theta_F,k | A finite, nonempty collection of future validation blocks and the forecast effect in block k | Blocks, dependence, timing, and any different thresholds unselected. |

### H-F — proposed primary candidate

For the binary Brier loss, define:

\[
L(p,y)=(p-y)^2,
\qquad
D_u=L(b_u,Y_u)-L(m_u,Y_u),
\qquad
\theta_F=\mathbb E_{P}[D_u].
\]

Both probabilities lie in [0,1], so D lies in [-1,1]. Positive theta_F means the method has lower expected Brier loss than the benchmark over the specified distribution. It says nothing yet about executable transactions.

The proposed practically relevant claim is:

\[
H_{0,F}:\theta_F\le\delta_F
\qquad\text{versus}\qquad
H_{1,F}:\theta_F>\delta_F,
\qquad 0<\delta_F<1.
\]

This domain prevents a structurally impossible strict alternative at or above the maximum score gain; the eventual benchmark and population may impose a smaller achievable bound. It does not select the threshold. Whether expectations also average over method randomness or condition on a declared randomization convention remains a Q6/Q8 specification dependency.

The weaker claim of any average improvement is a separate candidate:

\[
H_{0,F0}:\theta_F\le0
\qquad\text{versus}\qquad
H_{1,F0}:\theta_F>0.
\]

Passing the zero-effect criterion after failing the worthwhile-effect criterion must not be presented as satisfying the latter. These are different claims, not interchangeable success rules.

For n recorded opportunities and predeclared nonnegative weights w_u with positive total weight, a candidate descriptive estimator is:

\[
\widehat\theta_F
=\frac{\sum_{u=1}^{n}w_uD_u}{\sum_{u=1}^{n}w_u}.
\]

The weights and inclusion rules must correspond to the target P. This expression does not assume independent observations and does not specify a valid uncertainty estimate. Repeated forecasts of the same event and related-event groups need explicit handling. Choosing weights, aggregation, intervals, or sample size is deferred.

Brier loss is proposed because its paired difference has a direct interpretation and finite bounds in this setup. Proper scoring measures probabilistic forecast quality in expectation; it does not guarantee any particular finite-sample result. [Gneiting and Raftery (2007), introduction and section 3](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf) provide the methodological foundation, using reward-oriented scores where this record uses losses.

### H-E — economic-value candidate, deferred

Define only the abstract target:

\[
\theta_E=\mathbb E_Q[N_v^\pi],
\qquad
H_{0,E}:\theta_E\le\delta_E
\quad\text{versus}\quad
H_{1,E}:\theta_E>\delta_E.
\]

N is a placeholder for a future validated net-result definition, not an implemented payoff equation. Zero can represent a break-even hurdle; an economically worthwhile hurdle may be higher. Neither value is adopted here. Positive net expectancy per contract can still be too small, too infrequent, too capital-intensive, or too risky to justify the total effort. Research and inference expenses must be visible when overall viability is assessed. The allocation, capital denominator, capacity, and horizon remain undefined.

The ordinary finite-expectation interpretation assumes \(\mathbb E_Q[|N_v^\pi|]<\infty\). That is a mathematical requirement to verify under a later economic model, not an established fact about a selected strategy.

A realized sample profit is an observation; it is not identical to expected net value or proof of persistence. The model's own estimated probability inserted into an EV formula also cannot validate that probability or establish positive true expectancy.

### H-R — repeatability candidate, deferred

For a later predeclared finite, nonempty set K of relevant validation blocks, one possible stringent claim is:

\[
H_{0,R}:\min_{k\in K}\theta_{F,k}\le\delta_F
\quad\text{versus}\quad
H_{1,R}:\min_{k\in K}\theta_{F,k}>\delta_F.
\]

This is one candidate meaning of repeatability, not the selected replication rule. It would require valid joint evidence across declared blocks. A pooled mean alone does not establish it. No claim of indefinite persistence, every regime, or every market class is proposed. Economic repeatability would require its own economic counterpart.

### H-A — optional AI-contribution candidate, deferred

Let m_u^+ and m_u^- be forecasts from future matched procedures with and without the component whose contribution is being tested. Define a candidate forecast contribution:

\[
\theta_A
=\mathbb E_P[L(m_u^-,Y_u)-L(m_u^+,Y_u)].
\]

A candidate null is theta_A <= 0 against theta_A > 0, or a later predeclared practical hurdle. No ablation is selected now. Comparability of information, resources, tuning, and timing would have to be established. H-F does not imply H-A, and forecast contribution does not by itself imply incremental economic contribution.

### DER-01 — why the score claim is narrower than viability

Conditional on a mathematical information set I under which m and b are fixed, let p = Pr(Y=1 | I). Expanding the binary squared loss gives:

\[
\mathbb E[(q-Y)^2\mid I]=(q-p)^2+p(1-p),
\]

where q is either forecast. Therefore:

\[
\mathbb E[D\mid I]=(b-p)^2-(m-p)^2.
\]

The irreducible outcome-variance term cancels. This establishes what the score comparison measures under the stated mathematical setup; p is generally unobserved and is not identified with either forecast. The information set here is a device for the derivation, not a proposed source policy.

**Synthetic logical check only:** suppose p = m = 0.51 and b = 0.50. Expected Brier gain is 0.0001. For a hypothetical claim paying one currency unit on success and zero otherwise, a purchase at an all-in cost of 0.52 has expected net result 0.51 - 0.52 = -0.01 currency units. Thus a score improvement need not make that purchase profitable. These invented numbers are not observations, effect recommendations, or a solution to Q2. No venue or strategy is selected.

## Minimum effects and undefined quantities

Three quantities must remain distinct:

| Quantity | What it answers | What must determine it later |
| --- | --- | --- |
| delta_F, worthwhile forecast effect | How much score improvement warrants continued interest in this forecasting approach? | Scientific/practical relevance, target distribution, attainable precision, and eventual relationship to the intended use. |
| delta_E, worthwhile economic effect | How much net value justifies costs, capital/time commitment, risk, and operational effort? | Actual payoff and execution model, scale/capacity, resource constraints, and user preferences. There is no universal conversion from Brier points to money. |
| MDE_F, minimum detectable forecast effect | What effect, relative to the declared null boundary, can a given design detect with its specified error rates and power? | Sample size, variance, dependence, testing rule, multiplicity, and power target. For the practical-effect null, distinguish the additional effect above delta_F from an absolute effect measured from zero. This is a design capability, not the user's minimum worthwhile benefit. |

Statistical significance, economic importance, and feasibility are separate. No numerical threshold, confidence level, test, power target, or required sample size is chosen in Q1.

The unresolved quantity register and question dependencies follow. Each row is a requirement for later work, not a decision answering that question.

| Dependency ID / owner | Undefined quantities and decisions | Evidence eventually required |
| --- | --- | --- |
| DEP-02 / Q2 | Operational meaning of economic edge; pi, v, N, delta_E; cost components, payoff normalization, and connection (if any) between forecast gain and money | Derived contract accounting with compatible units; dated primary venue rules and costs when a venue is relevant; double-counting checks; assumptions separated from observed execution. |
| DEP-03 / Q3 | Concrete B; market-probability construction; decision-time/horizon matching; quote age and latency; primary and secondary comparators | Point-in-time benchmark provenance and suitability. Closing prices are retrospective diagnostics unless legitimately available at the declared decision time. |
| DEP-04 / Q4 | Eligible population P/Q; venue/class, outcome type, h, event/settlement definitions, capacity scope | Justified eligibility and data feasibility; predefined handling of invalid, unresolved, disputed, and delisted events. No selection using favorable test outcomes. |
| DEP-05 / Q5 | I^M/I^B, a/r/s/t timing, market-price use by M, retrieval/revision rules, access and retention rights | Availability and retrieval records, revision identifiers, legal/access basis, and source provenance. Availability by decision time alone is insufficient if a forecast used information unavailable when it was produced. |
| DEP-06 / Q6 | u, g, weights, coverage, abstentions/failures, partitions, contamination assessment, inference, multiplicity, stopping, sample size, MDE_F | Registered design; untouched/prospective evaluation plan; related-event dependence and failure accounting; historical AI outcome-knowledge assessment. Uncertain contamination makes historical AI results exploratory. |
| DEP-07 / Q7 | Forecast output validity, probability construction, calibration diagnostics, uncertainty meanings and missing-output handling | Defined and validated meanings for every reported uncertainty quantity; schema and coverage requirements. Model self-confidence cannot substitute for an interval. |
| DEP-08 / Q8 | Exact M and its version boundary; deterministic calculation versus AI responsibilities; optional matched attribution comparison | Reconstructable procedure records and component boundaries. No architecture or code selected now. |
| DEP-09 / Q9 | Scope of invalidation; total search/time/cost envelope; practical stopping, inconclusive versus contrary evidence | Approved bounded research objective and stop criteria that do not equate failure of one method with universal absence of opportunity. |
| DEP-10 / Q10 | Final delta_F/delta_E, evidence standard, K/replication, joint success requirements, advancement rules | Reconciliation of all prior approved choices, feasibility and economic relevance rationale, valid evidence requirements, and a user-approved next-phase protocol. |

Before confirmation, link all resolved parameters back to this claim, freeze their versions, and identify the exact population about which conclusions are allowed. Any change in objective returns to a user decision. This register deliberately specifies owners without selecting their answers.

## Evidence and evidence requirements

### Evidence available for this Q1 proposal

| ID | Evidence | Supports | Does not establish |
| --- | --- | --- | --- |
| DOC-01 | The four supplied founding files, compared in REVIEW-0001 with source hashes | Recorded intent, current scope, authority rules, and identified wording conflicts | Any prior gate approval or empirical advantage |
| DER-01 | Algebra and synthetic logical check above | Meaning of the paired Brier estimand and non-equivalence to profitable purchase | Real-world method quality, costs, fills, or economic viability |
| SRC-01 | [Gneiting and Raftery (2007)](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf), primary published paper; accessed 2026-09-17 UTC | Proper-scoring rationale for evaluating probability forecasts | Performance of any AI model or prediction-market strategy |
| SRC-02 | [Dwork et al. (2015), Generalization in Adaptive Data Analysis and Holdout Reuse](https://proceedings.neurips.cc/paper_files/paper/2015/file/bad5f33780c42f2588878a9d07405083-Paper.pdf), abstract/section 1; accessed 2026-09-17 UTC | Ordinary adaptive holdout reuse can undermine generalization; model/metric selection history is relevant evidence | A selected remedy, a ban on every form of reuse, or a validated project protocol |

Only methodological literature was inspected. No prediction-market dataset or evaluation result was collected. External sources are evidence, not instructions or amendments to this program.

### Evidence required at each level

| Requirement | Needed for | Status now |
| --- | --- | --- |
| E-01: documented objective, coherent candidate estimand, alternative objectives, limitations, and complete dependency register | Q1 claim framing | Prepared and approved as framing; not empirical validation |
| E-02: user's choice of claim direction and approval/revision of the gate clarification | Q1 closure and exact next scope | Satisfied by the recorded instruction above; Q2 only is authorized |
| E-03: fully bound M, B, population, horizon, target unit/weights, outcomes, primary metric, delta_F, and analysis rule | Final empirical claim and confirmatory readiness | Missing; belongs to later approved work |
| E-04: lawful traceable data, valid timing, leakage/contamination assessment, all-run coverage, exposure log, dependence-aware uncertainty, power/precision and multiplicity plan | Interpretable confirmatory forecasting evidence | Missing; historical AI results cannot be called clean merely because supplied sources were timestamped |
| E-05: credible net accounting, execution feasibility, costs, capital/time/capacity/risk conventions, delta_E, and relevant observed evidence | Economic-value or viability claims | Missing; simulated assumptions and achievable transactions must be distinguished |
| E-06: preregistered new periods/events and valid joint evidence within the claimed scope; fresh evidence after material method revisions | Repeatability or generalization claims | Missing; neither a single good period nor a pooled average is sufficient for a stronger claim |

No empirical evidence of edge is required to choose a research question; it is required to support that question's empirical answer. Evidence from a protocol that informed tuning cannot simultaneously serve as untouched confirmation of the tuned method.

## Falsification, uncertainty, and failure modes

For illustration of evidence logic only, suppose a future valid procedure supplies an uncertainty interval [L,U] for a declared effect theta, with a predeclared hurdle delta. Its coverage/interpretation, error level, dependence treatment, multiplicity, and any repeated inspection must be specified before use.

| Condition | Permissible interpretation |
| --- | --- |
| L > delta | Supports an effect above the hurdle for the tested method, population, and protocol, at the declared evidence standard. |
| U <= delta | Evidence against an effect exceeding that hurdle in that scope; not proof that the effect is exactly zero or universally absent. |
| L <= delta < U | Inconclusive at that standard. A non-significant result or negative point estimate alone is insufficient to infer absence. |
| Leakage, invalid comparison, outcome-dependent exclusions, or compromised holdout | Evidence invalid for its intended confirmatory claim. Repair or obtain fresh evidence; do not reinterpret invalidity as success or substantive failure. |

These are templates, not an adopted statistical test or automatic phase gate. “Supported,” “inconclusive,” and “invalid” describe evidence; ADVANCE, REVISE, and STOP are user-controlled research decisions. Time or cost can justify stopping even when the empirical claim remains unresolved.

Main failure modes to prevent are post-hoc selection of successful markets/horizons/prompts; repeated-event pseudoreplication; undefined abstention coverage; selective loss of failed runs; stale or unmatched benchmarks; unavailable source revisions; AI outcome knowledge; tuning on confirmatory results; optimistic fills/costs; and generalization beyond the tested scope. Their controls are dependencies above, not designs completed in Q1.

## Alternatives considered

| Direction | Merits | Limitation / proposed disposition |
| --- | --- | --- |
| Market-relative Brier improvement first | Clear paired probabilistic target; separates method quality from execution assumptions | Recommended first claim, with economic evidence still mandatory for viability. |
| Log loss as the primary score | Another proper loss with different sensitivity to extreme errors | Candidate secondary diagnostic. Endpoint treatment, conventions, and inferential role remain unresolved; do not switch primaries after seeing results. |
| Net economic value first | Directly targets the ultimate objective | Requires earlier binding of policy, payoff, costs, execution, scale, and risk. Legitimate user alternative, but changes the proposed research ordering. |
| Realized or risk-adjusted profit first | Operationally meaningful once there is a defined policy and risk/accounting frame | Premature as an initial claim; denominators, uncertainty, risk preferences, and fair comparators are unbound. |
| Calibration alone | Useful probability-quality diagnostic | Does not establish benchmark superiority, informative discrimination, or net value; propose as later supporting analysis. |
| Specific AI contribution first | Directly addresses whether AI adds value | Requires a matched component comparison beyond whole-system versus market performance. Keep as optional secondary work. |

## Assumptions and unknowns

| ID | Statement | Status / consequence if false |
| --- | --- | --- |
| A-01 | A bounded, relevant outcome population can be defined and labeled honestly. | Unverified. If infeasible, revise scope or stop; do not selectively discard hard cases after outcomes. |
| A-02 | A matched decision-time benchmark can be obtained. | Unverified. Its absence blocks the proposed market-relative test. |
| A-03 | A versioned forecasting procedure and lawful, timely inputs can be recorded with adequate auditability. | Unverified. If not, claims must be weakened or evidence collection redesigned. |
| A-04 | Enough informative observations can be obtained within an acceptable resource envelope. | Unverified. Required precision, dependence, time, and budget remain unknown. |
| A-05 | A forecast-first pathway is the research priority the user wishes to pursue. | Confirmed by this approval; a preference, not an empirical assumption about all profitable strategies. |

The absence of current fee, market, model, or execution evidence is explicit. No venue, model API, subscription, research budget, or capital commitment has been selected.

## Approved decision, rationale, and exact scope

**User-approved decision: ADVANCE.** The user accepted this claim framing and AMEND-01 through AMEND-04. This chooses H-F with paired Brier loss as the candidate primary research direction, retains economic viability and repeatability as separate requirements, and authorizes Q2 research and documentation only.

The rationale is that this offers an interpretable first claim while preserving honest failure, economic relevance, and later operational choices. It also repairs the founding documents without treating a parameterized proposal as a frozen experiment.

**What this unlocks:** incorporating the four approved charter clarifications and conducting Q2 research and documentation. A later linked final specification remains required before confirmation. Stop at the Q2 decision before Q3.

**What remains prohibited:** resolving Q3–Q10 prematurely; building the evaluation engine or full scaffold; running experiments; collecting a prospective forecast series without its own approved protocol; selecting a deployed strategy; paid commitments; paper trading as strategy validation; live orders, deposits, credentials, or unattended execution. No resource or gate permission is implied by this proposal.

Historical suggested wording offered with the original proposal (the user's actual reply is recorded above):

> Approve D0001's forecast-first framing and AMEND-01 through AMEND-04. Apply those wording changes and begin Q2 only. Keep the benchmark construction, market universe, thresholds, and protocol unresolved until their gates. Do not build the evaluation engine.

The user chose to begin the recommendation and deferred repository creation. Future material changes to the objective require a new decision; no broader authority is inferred from this approval.
