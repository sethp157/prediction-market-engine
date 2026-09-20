# Founding-document review — Q1 only

Record: REVIEW-0001. Prepared: 2026-09-17 UTC (2026-09-16 America/Chicago).
Status: analysis complete; AMEND-01 through AMEND-04 APPROVED and APPLIED in charter revision 2.2 on 2026-09-17 UTC. The original Q1 review and its proposed wording are retained below as rationale. [D0001](decisions/D0001-primary-research-claim.md) records the user's exact approval and Q2-only scope. The prior Q1 package remains a historical snapshot.

## Assessment and intended objective

The four starting documents provide a strong basis for bounded Q1 research. They are not yet a complete, executable evaluation specification, and should not be described as one. Their main procedural conflict is whether Q1 must finalize choices that the same charter explicitly assigns to later questions. Resolve that conflict through the user's decision, not an agent's silent interpretation.

The intended ultimate objective is to determine whether a specified AI-assisted method can produce repeatable, economically meaningful out-of-sample prediction-market value under honest information timing and feasible execution. The immediate objective is to choose a precise research claim and identify what is needed to test it. Learning, an attractive software project, model confidence, a profitable anecdote, and raw disagreement with prices do not meet the viability objective. The evaluation engine is a later instrument for testing claims, not the current deliverable.

This review distinguishes the user's current request from instructions inside the ZIP. The current request authorizes reviewing these documents and following their Q1-only first task. Scaffold examples, future experiment templates, and live-pilot discussions are reference material, not current authorization. The package's statement about a prior viability-first selection is context supplied by the package; it is not evidence of any approved research gate. No prior approval transcript was supplied.

## What is already robust

- AGENTS.md separates recommendations, approval, evidence, and durable knowledge; prohibits fabricated findings and implicit gate approval.
- Charter sections 1, Q5, and Q6 distinguish exploration from confirmation, source timing from AI contamination, and independent events from repeated forecasts.
- AGENTS.md requires preserved null results, exposed-holdout tracking, versioning, and amendments to frozen protocols.
- PROJECT_CONTEXT.md keeps learning secondary to viability and leaves budgets and economic significance explicitly unresolved.
- The charter and AGENTS.md require a separate approved live pilot and make the large repository scaffold conditional on actual research needs.

## Conflicts, ambiguities, and completeness gaps

Severity here concerns research validity, not evidence that a market opportunity exists.

| ID | Finding and source | Consequence | Proposed treatment |
| --- | --- | --- | --- |
| R01 — blocking procedural conflict | Charter Q1 required decision/Gate 1 demands a primary benchmark and minimum effect size; section 14.6 explicitly defers final benchmark, market, effect, and protocol choices. PROJECT_CONTEXT open constraints and the original RESEARCH_STATE agree with deferral. | Literal closure either jumps ahead or cannot occur. | AMEND-01: distinguish Q1 claim framing from final claim specification. User approval is required for the proposed interpretation. |
| R02 — scope ambiguity | Charter purpose asks whether edge exists, without bounding the method search or target population. | Failure of one procedure could be misreported as proof that no prediction-market edge exists; success in a selected sample could be generalized too far. | D0001 bounds any empirical claim to a versioned method, population, time/horizon policy, and protocol. A finite search/resource envelope is a Q9 dependency. |
| R03 — units hazard | Charter Q2's proposed additive decomposition subtracts costs from an undefined forecast advantage. | Scores, probabilities, and money cannot be subtracted without a justified conversion. | AMEND-02 labels this conceptual, not a valid accounting identity. Derivation remains Q2 work. |
| R04 — illustrative EV hazard | Charter section 2.2 subtracts entry cost, fees, spread/slippage, and a model-uncertainty penalty from a probability. It already says the formula is illustrative; AGENTS.md already warns against double-counting spread. | Use would require compatible payout normalization, mutually exclusive cost components, and separation of a risk adjustment from expected cash profit. | AMEND-02 adds a caveat, without deriving a payoff or selecting costs. Record Q2/Q7 dependencies. |
| R05 — invalidation ambiguity | Q9 lists a nonpositive held-out point estimate and disappearance across alternative prompts or market classes as possible kill conditions; AGENTS.md and charter section 7.5 distinguish insufficient evidence from rejection. | Sampling noise could be called disproof; failure outside the claimed population could incorrectly invalidate a narrow claim. | AMEND-03 makes the examples diagnostic only; later rules must distinguish statistical conclusions, feasibility decisions, and scope. |
| R06 — reproducibility tension | Charter section 4.3 invariant 10 says results must be reproducible from repository state; AGENTS.md permits disclosure when exact model-output replay is unavailable. | A stochastic or retired model might make verbatim regeneration impossible despite an auditable result. | AMEND-04 distinguishes stored-run audit and deterministic recomputation from model-output regeneration. |
| R07 — unbound estimands | The initial score examples do not bind population, forecast horizon, repeated-event weighting, missing forecasts, abstentions, or invalid/void outcomes. | Selective coverage, censoring, or repeated forecasts could change what is being measured. | Record these as unresolved parameters in D0001. Definitions and rules belong to Q4–Q7; no defaults are chosen now. |
| R08 — effect and inference ambiguity | Practical effect, statistical detectability, interval construction, multiplicity, and stopping are not yet specified. | A statistically detectable score gain could be economically irrelevant; an underpowered test could be called a failure. | D0001 separates forecast relevance, monetary relevance, and detectable effect. Protocol choices remain Q6/Q9/Q10. |
| R09 — attribution and persistence | Whole-system improvement, AI-specific contribution, and repeated future performance are different claims. | Success of a hybrid method could be attributed to the AI alone, or a pooled average could hide regime dependence. | D0001 states separate candidate claims and lists ablation and replication evidence requirements without designing either. |
| R10 — resources and provenance | Research time, budgets, access, retention, and review limits remain undecided. Source revisions are dated 2026-09-17; this session is also September 17 UTC but September 16 locally. | Unstated defaults could permit unbounded search or produce misleading records. | Keep resource limits unresolved and dates explicit. The date difference alone is not a conflict. No paid work is authorized. |
| R11 — scoring priority ambiguity | Section 2.3 introduces both Brier score and log loss as primary scoring rules; Q1 asks for a primary dependent variable. D0001 proposes Brier primary and log loss supporting. | An implicit co-primary requirement could conflict with the proposed single primary claim or allow post-hoc metric selection. | AMEND-01 clarifies nomination of one primary loss; any later co-primary role requires an approved inference and multiplicity specification. |
| R12 — decision-template omission | Section 12's template has a single Decision field despite the separate recommendation and user-approval requirements elsewhere. | A filled template could be mistaken for user approval. | D0001 adds proposal status, recommendation, user decision/date/instruction, and exact scope fields. Governance already requires this separation; no new approval rule is introduced. |
| R13 — registration terminology | Section 7.6 calls every experiment preregistered, while sections 1 and 8 distinguish mutable exploratory plans from frozen confirmatory protocols. | A registered exploratory plan could be overstated as frozen confirmation. | Follow the explicit distinction in sections 1 and 8. This is a minor terminology issue; no experiment is being registered now. |

R01 was blocking advancement and is now addressed by the approved AMEND-01. R03–R06 motivated the approved wording repairs that prevent misuse of existing examples; those repairs do not themselves answer Q2–Q10. R07–R10 are expected downstream incompleteness, not reasons to manufacture answers in Q1.

## Exact proposed amendments

These changes were proposed during Q1 and are now enacted in charter revision 2.2 under the approval in D0001. The original source hashes below describe the supplied ZIP, not the updated deliverable. AGENTS.md and PROJECT_CONTEXT.md also have routine resume/context updates reflecting the user's approved Q2 scope and deferred repository setup. No empirical evidence needs reclassification because no experiments have run.

### AMEND-01 — Q1 approval and final specification

Replace Q1's “Required decision” and Gate 1 text with:

> Q1 chooses a candidate primary claim, candidate dependent variable, intended comparator role, secondary claim priorities, and the meaning and units of the minimum worthwhile effect. It identifies every unresolved parameter, its later question, and the evidence needed to bind it. Final benchmark construction, market and horizon selection, numerical effect thresholds, and evaluation protocol remain subject to their later questions.
>
> Gate 1 is a user decision approving or revising this claim framing and its dependency register. Q1 approval does not mean that a fully specified empirical hypothesis has been approved or tested. Only an explicit user instruction authorizes the next named question.
>
> Before a confirmatory protocol is frozen, reconcile the original Q1 claim with all later approved choices in a linked final specification. No material placeholders may remain. Changes to the objective or target claim require a new user decision; changes after freezing also require a protocol amendment and an evidence-impact assessment.

Add to section 14.6:

> At the first Q1 decision, evidence consists of documented intent, mathematical coherence, explicit limits, and a complete dependency map. Evidence that the claim is true is not a prerequisite for choosing to investigate it. Experimental readiness remains a separate later approval.

Replace section 2.3's introductory sentence “Primary probabilistic scoring rules should include:” with:

> Candidate probabilistic scoring rules include Brier score and log loss. Q1 nominates a primary dependent variable. Additional losses may be supporting diagnostics; a later co-primary role requires an explicitly approved inference and multiplicity specification. Metric roles must be frozen before confirmatory outcomes are examined.

This resolves the circular dependency while preserving the requirement for a precise, falsifiable claim before confirmation. It does not silently weaken Gate 1.

### AMEND-02 — dimensional and economic caveats

Immediately before Q2's “Potential decomposition,” add:

> The following decomposition is a conceptual checklist, not a dimensionally valid equality. Forecast-score improvement, probability disagreement, and cash profit have different units. Any operational relationship must be derived from an explicit payoff, decision policy, and execution model under Q2.

Append to section 2.2's existing illustrative-formula caveat:

> Subtracting a price from a probability presumes an explicitly normalized binary payoff and compatible units. Fees, spread, and slippage must be defined without overlap; an executable entry price may already contain some of these effects. A conservative uncertainty adjustment is a decision adjustment, not automatically an expected cash expense. Expected cash profit and any risk-adjusted decision quantity must be separately named and defined before use.

### AMEND-03 — invalidation and inconclusive evidence

Immediately after Q9's example conditions, add:

> These examples are candidate diagnostics, not adopted rejection or stopping rules. A nonpositive sample estimate alone need not rule out a worthwhile population effect. Failure to establish an effect is not automatically evidence against it. Any future rule must specify uncertainty, dependence, multiplicity, stopping, and the claim's population and scope. Failure in a different population or for a different method need not invalidate the original narrow claim. A practical decision to stop research can be justified by cost or infeasibility without proving universal absence of edge.

### AMEND-04 — auditability and replay

Replace evaluation-engine invariant 10 with:

> Results must be auditable from versioned repository records, lawfully retained data or a documented access manifest, and stored run inputs and outputs. Deterministic evaluation must be reproducible from those recorded inputs. Exact regeneration of a model output is a separate property: record the model, settings, prompts, tools, timestamps, and limitations, and disclose when regeneration is unavailable. Do not call a run reproducible if the necessary evidence cannot be inspected.

## Evidence boundaries

The conflict findings are verified by comparing the supplied documents. The mathematical statements in D0001 are derivations, conditional on their declared setup. Proposed claim and amendment choices are recommendations. The empirical existence, size, durability, and exploitability of any edge remain untested.

This review does not certify future datasets, benchmark quality, lawful access, model contamination, execution, calibration, or statistical power. Those require later evidence under approved scope. No venue facts or fee schedules were used; no market outcomes or holdouts were retrieved.

## Source manifest

Source archive: `C:\Users\sethp\Downloads\prediction-market-starter.zip`.
The original ZIP was read and left unchanged; its four files were extracted to a working source copy.

| Source | SHA-256 of supplied bytes |
| --- | --- |
| prediction-market-starter.zip | `F69F6BE597F2556F7DCAB9575C7F2D511D6BDFD50B3BE74781990BB1BA7A2501` |
| AGENTS.md | `7B56DD3AE5F1BC77DC238DE938384F39C665194EDEE7978D6BC4FBB351117622` |
| prediction_market_research_charter_v2.md | `C5CC57069CCCA000ACABD65D2233E33F469B99FFD2827769FA4B450309A24607` |
| PROJECT_CONTEXT.md | `18932943749DF1AD1A7B81B43F2D8382C1E5A538C8BB7822D1F6C0FFE2F4BD55` |
| RESEARCH_STATE.md before this session | `774C55FEDF2D04F7C762CE0606DF646ED01BA95B60300EDCE954F82A0DB2465E` |

Current governing documents: [AGENTS.md](../AGENTS.md), [charter revision 2.2](../prediction_market_research_charter_v2.md), and [PROJECT_CONTEXT.md](../PROJECT_CONTEXT.md). The current [RESEARCH_STATE.md](../RESEARCH_STATE.md) records progress; all original input files remain recoverable from the unchanged source ZIP.

The approved Q1 framing, candidate hypotheses, evidence requirements, and later-question dependencies are in [D0001](decisions/D0001-primary-research-claim.md).
