# D0002 — What “edge” means

**Adoption addendum, 2026-09-18:** ADOPTED by the agent under the user's delegated continuation authority in [D0003](D0003-delegated-research-authority.md). The proposed definitions below are now the working framework. The prior pending-approval fields are historical; the user delegated onward research rather than reviewing each definition individually. No economic claim is established. The Q3-only stop below is superseded within AMEND-05's bounded scope.

Prepared: 2026-09-17 UTC (2026-09-16 America/Chicago).
Reviewed and finalized for the user's decision: 2026-09-17 UTC (2026-09-17 America/Chicago).
Scope: Q2 research and definitions only. Record status: PROPOSED.

| Authority field | Status |
| --- | --- |
| Entry authorization | User approved the recommendation in [D0001](D0001-primary-research-claim.md): “okya begin on your recomneded we will build repo later” |
| Agent recommendation | ADVANCE after user approval of the definitions and scope below |
| User Q2 decision / date | PENDING / none |
| Gates approved | Q1 framing only; Q2 has not been closed |
| Empirical edge established | None |
| Next scope proposed | Q3 benchmark research only, if the user authorizes it |
| Repository / engine | Deferred by the user; this is a research document, not a software specification |

## Question, recommendation, and why it matters

Q2 asks for the mathematical and operational meaning of edge. Use qualified terms, with the following proposed convention:

**Forecast edge** means positive expected improvement in the approved forecast loss over a declared benchmark. **Economic edge** means positive net expectancy of a feasible, fully specified policy under a declared opportunity population, accounting unit, horizon, and cost convention. **Economically worthwhile edge** exceeds an additional predeclared economic hurdle. Acceptable risk and repeatability require separate evidence.

Call calculations from an assumed or fitted model **estimated executable EV**. Call a difference between two forecast probabilities **disagreement**. Neither label is evidence that economic edge exists. Avoid an unqualified claim of “edge” that changes meaning between these quantities.

This convention preserves D0001's forecast-first direction while keeping economic viability as the ultimate objective. It does not select a strategy, benchmark construction, market universe, trading threshold, or evaluation protocol. Approval would settle the language and accounting framework; it would not establish profitability or make the formulas operational without their missing inputs.

## Q2 decomposition

| ID | Necessary subquestion | Output here |
| --- | --- | --- |
| Q2.1 | Which different claims have been called edge? | Distinct forecast, disagreement, price-value, expectancy, realized-result, and viability quantities |
| Q2.2 | What are their units, conditioning, and denominators? | Defined notation and an explicit prohibition on subtracting incompatible quantities |
| Q2.3 | How does contract accounting produce a monetary result? | General signed-cash-flow identity and conditional binary examples |
| Q2.4 | How do execution and costs change the target? | Joint fill/outcome requirement, non-fill coverage, and cost-allocation rules |
| Q2.5 | How should estimates, uncertainty adjustments, and observations be separated? | Distinct true-law targets, model estimates, decision adjustments, and realized results |
| Q2.6 | What extra claims does viability require? | Practical magnitude, risk/funding feasibility, capacity, total resource costs, and persistence |
| Q2.7 | What evidence would justify or contradict each claim? | Evidence requirements and conditional interpretations; no selected test or numerical threshold |
| Q2.8 | What must later questions supply? | Unresolved input/dependency register, with no downstream choices made |

## Definitions: quantities that must stay separate

Reuse D0001's notation: u is an eligible forecast opportunity, Y_u its binary outcome, m_u the method probability, b_u a benchmark probability, and P the as-yet unspecified target distribution. Both forecasts refer to the same outcome and declared decision time. None is assumed to equal the event's unknown conditional probability.

| Term | Mathematical target or observation | Units and limit |
| --- | --- | --- |
| Forecast edge | theta_F = E_P[(b_u - Y_u)^2 - (m_u - Y_u)^2] > 0 | Dimensionless squared-probability score units. The worthwhile candidate remains theta_F > delta_F, with delta_F unselected. |
| Forecast disagreement | Delta_u = m_u - b_u | Probability difference; directly computable once forecasts exist, but not proof of mispricing. |
| Estimated price-value advantage | Estimated expected contract payoff minus a specified reference price, on a common valuation basis | Currency per contract. Excludes any charges not explicitly included and does not establish executability. |
| Conditional executable EV | Expected net cash result under the joint outcome/execution law, conditional on decision-time information and a declared policy | Currency per declared episode/opportunity. The target differs from a model estimate of it. |
| Economic edge | theta_E^pi = E_Q[N_v^pi] > 0 | Positive target-law net expectancy under a declared feasible policy, population, accounting unit, and cost scope. |
| Economically worthwhile effect | theta_E^pi > delta_E | Same units as theta_E^pi. delta_E is an additional practical hurdle, not an expense or an invented numerical target. |
| Realized net result | An observed N_v^pi under recorded accounting rules | Currency. A winning trade or positive sample total is not the same as positive expectancy. |
| Economic viability | Sufficient scoped evidence of worthwhile net value, feasible resources/capacity, acceptable risk, and repeatability | A multi-part research conclusion, not one score or a synonym for theta_E^pi > 0. |

The forecast-gain definition is inherited from Q1; Q2 does not change its primary metric. Log loss and calibration remain possible supporting diagnostics, with their eventual roles subject to the later protocol.

A quoted price is a trading quantity. Interpreting it as an aggregate belief requires assumptions, and an aggregate belief need not equal the true event probability. Theory also provides conditions under which prices equal or closely approximate mean beliefs; it does not justify assuming prices are generally wrong. [Wolfers and Zitzewitz (2006), sections 2–3](https://fraser.stlouisfed.org/title/working-papers-federal-reserve-bank-san-francisco-7038/interpreting-prediction-market-prices-probabilities-639221/fulltext). The concrete benchmark mapping remains Q3.

## General monetary accounting — DER-02

For the following identity, let v denote a complete accounting episode with zero opening and terminal inventory. An episode may contain multiple transactions or none. This is a derivation device, not the chosen experimental unit. A later protocol may use a different unit with explicitly reconciled inventory accounting.

| Symbol | Meaning | Units / timing |
| --- | --- | --- |
| pi | Complete prospective action policy, including abstention, order attempts, exits, and contingencies | No policy selected; its actions may depend only on legitimately available information |
| t_v, I_v | Episode's decision/valuation origin and declared information available there | Timestamp and information set; concrete rules deferred |
| X_v,l^pi at tau_v,l | Signed trading or contractual cash flow: acquisition outflow, sale proceeds, settlement/refund receipt, or obligation payment | Currency; sign gives direction |
| C_v,j^pi at sigma_v,j | A separate charge not embedded in X; rebates may be negative charges | Currency; no cash item may appear twice |
| d(t,s) | Declared factor converting a cash flow at s to the common valuation basis t | Dimensionless; convention unselected. A nominal undiscounted presentation uses d = 1 and must say so. |
| O_v^pi | Operating/inference costs allocated to the episode, on the same valuation basis | Currency; policy for shared/fixed costs remains unselected |
| Pi_v^trade, N_v^pi | Result after trading charges, and result additionally net of O | Currency per episode; this document states the cost scope whenever using “net” |
| P-star, P-hat | Unknown target joint law and a proposed fitted/assumed law for all relevant random quantities | Includes outcomes, fills, sizes, prices, charges, and times |
| Q | Target distribution over economic accounting units and their outcomes | Not necessarily the forecasting distribution P; population/weights remain unselected |

Define:

\[
\Pi_v^{trade}
=\sum_l d(t_v,\tau_{v,l})X_{v,l}^{\pi}
-\sum_j d(t_v,\sigma_{v,j})C_{v,j}^{\pi},
\qquad
N_v^{\pi}=\Pi_v^{trade}-O_v^{\pi}.
\]

This identity records where money goes; it does not predict fills or validate prices. Deposits and withdrawals of the owner's capital are not earnings. All items require one consistent currency and valuation convention. Currency conversion, taxes if relevant to a later chosen viability scope, financing, and settlement adjustments must be declared rather than silently omitted or assumed to be zero.

For an episode with opening or terminal inventory, cash flows alone are insufficient: add a consistent inventory valuation/accounting rule before making a total-result claim. An unliquidated mark is not realized cash profit. Early exits require actual or modeled exit transactions; they cannot reuse a hold-to-resolution payoff without adjustment.

A complete episode also has no unaccounted residual receivables, collateral, financing balances, or other assets and obligations. Principal funding and collateral movements must be distinguished from earnings and expenses and reconciled consistently; no capital inflow counts as earned profit and no outstanding liability may be omitted. Cash-flow sums must be well-defined and finite, or use an explicitly justified convergence rule. Finite-expectancy claims additionally require integrability under the relevant law.

Fixed research expenditure must remain visible at the project level. If it is allocated across episodes in O, the allocation must reconcile to the total rather than disappearing through unlimited amortization. If it is not allocated in O, it must be deducted once in a separate project-viability calculation. The amortization horizon and treatment of sunk versus prospective costs remain open. Future forecasting expenses, failed attempts, and non-filled orders can incur costs even when trading cash flow is zero.

### Target expectancy versus model estimate

For an integrable net result under the relevant law, define:

\[
\mu_v^{\pi}
=\mathbb E_{P^\star}[N_v^\pi\mid I_v],
\qquad
\widehat\mu_v^{\pi}
=\mathbb E_{\widehat P}[N_v^\pi\mid I_v].
\]

The first is the conditional target; the second is a model calculation. Substituting a forecast into an accounting identity yields the second, not proof about the first. A finite-mean claim requires the corresponding expectation of |N| to be finite. Estimation and inference must address the joint execution/outcome law, not only an event probability.

## Binary contracts — conditional derivations, not a chosen strategy

The following special cases establish the meaning of the arithmetic. They assume a completed purchase of q > 0 contracts held through final resolution, exactly two exhaustive states Y in {0,1}, a payoff scale U > 0 in currency per contract, and no voids, partial settlement, default, early exit, discounting, or financing. Actual contracts must be checked before these simplifications can be used.

Let E describe the execution condition, including fixed quantity q and actual purchase price a. Define p_E = Pr(Y=1 | I_v, E). Let f_e be the total separate entry charge and f_1/f_0 the total separate terminal charges in states Y=1/Y=0. These are total currency amounts for q contracts, potentially nonlinear in q, and do not include costs already embedded in a. The special-case f terms below are fixed given execution condition and settlement state; otherwise they must remain inside an expectation.

For a YES contract paying UY with actual price a_Y:

\[
\Pi_Y=q(UY-a_Y)-f_e^Y-Yf_1^Y-(1-Y)f_0^Y,
\]

\[
\mathbb E[\Pi_Y\mid I_v,E]
=q(Up_E-a_Y)-f_e^Y-p_Ef_1^Y-(1-p_E)f_0^Y.
\]

For a NO contract paying U(1-Y) with its own actual price a_N:

\[
\mathbb E[\Pi_N\mid I_v,E]
=q\{U(1-p_E)-a_N\}-f_e^N-p_Ef_1^N-(1-p_E)f_0^N.
\]

These are results after the listed trading charges, before any additional operating allocation O. The Y-indexed fees refer to the event state, including for NO. Execution condition E must be specific to the side and transaction; it need not yield the same p_E for YES and NO executions.

There is no assumption that a_N = U - a_Y. Buying NO is not automatically equivalent to selling YES: selling requires its own inventory, collateral, liabilities, fees, and execution accounting. Inserting an appropriately conditioned estimated p_E gives an estimated result. Inserting the original unconditional forecast instead requires additional justification when execution is informative.

With U = 1 and no other adjustments, expected payoff minus price can numerically resemble “probability minus price.” Without the payout normalization and declared costs, that shortcut is dimensionally incomplete. The charter's illustrative EV expression must not be treated as a validated formula.

## Execution changes the population — DER-03

Consider only a hypothetical fixed-size order at fixed filled price a; temporarily omit fees, operating costs, and discounting. Let F be the binary fill indicator, p = Pr(Y=1 | I_v), and r = Pr(F=1 | I_v). The payoff contribution is Fq(UY-a), with zero trading payoff when no fill occurs. If r > 0:

\[
\mathbb E[Fq(UY-a)\mid I_v]
=rq\{U\Pr(Y=1\mid I_v,F=1)-a\}.
\]

Equivalently, including the zero-fill case:

\[
\mathbb E[Fq(UY-a)\mid I_v]
=q\{r(Up-a)+U\operatorname{Cov}(F,Y\mid I_v)\}.
\]

The equality follows by expanding E[FY | I_v] into its mean-product and conditional covariance. It shows why “fill probability times unconditional EV” is not generally valid. The covariance term has no assumed sign. Partial quantities, price movement, and nonlinear fees require the full joint calculation rather than products of separate averages. A positive quoted calculation does not establish that the order will fill, at that price, in the intended size, under representative conditions.

**Synthetic arithmetic check only:** with U = q = 1, a = 0.50, p = 0.60, r = 0.50, and Pr(Y=1 | F=1,I_v) = 0.40, unconditional plug-in value is +0.10 per completed contract, but the proposed order's expected cash contribution is 0.50(0.40 - 0.50) = -0.05. This is a coherent hypothetical joint distribution: the non-fill conditional event probability can be 0.80. No empirical frequency, order type, or strategy is proposed.

Market-microstructure theory motivates treating observed prices and realizable returns separately, including information-related spreads; it does not validate this project's execution model. [Glosten and Milgrom (1985), author-institution abstract](https://business.columbia.edu/faculty/research/bid-ask-and-transaction-prices-specialist-market-heterogeneously-informed-traders).

## Costs and uncertainty: count each item once

| Item | Proposed accounting treatment | What remains unresolved |
| --- | --- | --- |
| Acquisition or exit price | Actual transaction cash flow, or an explicitly labeled modeled execution price | Achievability, timestamps, order size, depth, latency, and exit assumptions |
| Spread and slippage | If contained in the execution price, do not subtract them again. If using a reference-price decomposition, reconcile it to the same execution cash flow. | Reference price and decomposition convention; no benchmark selected here |
| Fees/rebates | Count separately only if absent from recorded cash flows; allow state/size/price dependence | Actual dated fee rules and whether quotes/receipts are gross or net |
| Financing, discounting, alternative use of capital | Declare economic roles and reconcile the valuation basis; do not charge the same effect twice under different labels | Funding, currency/time basis, opportunity-cost comparator, and hurdle policy |
| Inference/data/research/operations | Show expenses at the episode and/or project level, allocated once | Budget, fixed-cost treatment, amortization, and treatment of sunk versus prospective expense |
| Uncertainty adjustment | Report separately as a decision quantity; it is not automatically a cash expense or an expectation | Construction, calibration/coverage, risk meaning, and amount |

For a separately defined monetary adjustment lambda_v >= 0, a possible decision quantity is:

\[
J_v=\widehat\mu_v^\pi-\lambda_v.
\]

This does not define J as true EV, a confidence bound, or a risk-adjusted utility. Each interpretation would require a justified construction in Q7 and the later protocol. No lambda or rule to act on J is selected. A practical hurdle delta_E similarly expresses a requirement; it is not an incurred expense.

## From transactions to economic claims

Let Q specify the economic accounting population and let every eligible unit v have a policy result N_v^pi, including abstention, failure, and no-fill cases. Define:

\[
\theta_E^\pi=\mathbb E_Q[N_v^\pi],
\qquad
H_{0,E}:\theta_E^\pi\le\delta_E
\quad\text{versus}\quad
H_{1,E}:\theta_E^\pi>\delta_E.
\]

Break-even concerns zero; the worthwhile-effect claim uses an additional nonnegative practical hurdle delta_E whose value is unselected. State which level of costs is included before calling a result net. If not all program costs are in N, positive theta_E supports at most that narrower claim, not all-in project viability.

Policy selection and coverage are part of the claim. An average over completed profitable-looking transactions cannot silently replace an average over all eligible opportunities. Likewise, per-contract expectancy, per-episode profit, profit per calendar period, return on capital, and value per capital-time are different denominators. No denominator or sizing rule is chosen here. Repeated and related outcomes affect inference and risk even though expectation is additive for integrable cash flows without an independence assumption.

If a later claim is that AI improves economic performance, it needs a matched comparison with a separately defined policy pi_0:

\[
\theta_{inc}=\mathbb E_Q[N_v^{\pi}-N_v^{\pi_0}].
\]

Positive absolute net expectancy is not evidence that theta_inc > 0. The comparator policy, resource matching, and attribution design remain unselected. This dependency does not authorize Q3 benchmark selection now.

A positive mean also does not establish acceptable downside, funding feasibility, sufficient capacity, or useful returns for the required time. A positive expectation under one Q does not imply the same under future conditions. Risk metrics, capital constraints, replication design, and economic thresholds remain Q9/Q10 and protocol dependencies.

## Evidence needed before any substantive edge claim

| ID | Evidence requirement | Claim it enables / limitation |
| --- | --- | --- |
| Q2-E01 | Matched, valid out-of-sample forecasts and outcomes; predeclared population, weighting, metric, effect hurdle, and inference | Forecast advantage only; does not establish economic value |
| Q2-E02 | Exact dated payoff, resolution, cancellation/void/default, fee, access, and retention rules from applicable primary sources | Instantiation of monetary accounting; venue-specific facts remain unverified |
| Q2-E03 | Quotes and depths with timestamps; legitimate latency; attempted quantities, fills/partial fills/non-fills, cancellations, exits, and execution conditions | Credible transaction feasibility and joint execution/outcome assessment; a quote is not proof of a fill |
| Q2-E04 | Actual or explicitly simulated cash-flow records with cost reconciliation, coverage, outcomes, and all failures retained | Recomputable net results; distinguish observed transactions from model assumptions |
| Q2-E05 | Forecast/EV model versions, information timing, contamination assessment, exposure records, dependence and uncertainty methods | Interpretable estimates and evidence against model/execution misspecification |
| Q2-E06 | Declared target unit, full operating/research costs, resource and risk constraints, capacity, delta_E, and replication requirements | Worthwhile, feasible, persistent economic value; still requires an approved evaluation protocol and actual evidence |

Evidence status must remain distinct from research decisions. Under a future valid uncertainty procedure for theta_E with interval [L_E,U_E], L_E > delta_E could support the scoped worthwhile-effect claim, U_E <= delta_E could count against it, and overlap is inconclusive. This is inherited evidence logic, not a chosen test, confidence level, sample size, or stopping rule. A profitability claim requires the statistical and economic criteria to be declared before evaluation, as Gate 2 requires.

Contrary evidence could include reliable net-effect estimates below the declared hurdle, validated execution/cost evidence that removes the estimated surplus, or inability to make the policy feasible within its declared scope. Leakage, selective exclusions, invalid fill assumptions, or reused confirmatory data instead undermine the validity of the intended evidence; they do not prove universal absence of opportunity. A single winning or losing sample does not settle the target expectation.

## Unresolved quantities and later-question dependencies

| Owner | Required decisions / undefined inputs | Q2 boundary |
| --- | --- | --- |
| Q3 | Concrete market benchmark b; probability/price mapping; decision-time matching; reference price if a cost decomposition needs one | None selected; no midpoint, last trade, closing quote, or other construction adopted |
| Q4 | Eligible contracts and population P/Q; horizon and resolution policy; U; settlement exceptions; feasibility/capacity scope | Binary examples are conditional illustrations, not a market choice |
| Q5 | I_v and timing; source access, revision and retention rules | No source taxonomy, feed, or account selected |
| Q6 | Sampling/weights; fill/outcome model; dependence; partitions; model randomness; contamination; uncertainty/multiplicity; registration and inference | No experiment, fill simulator, test, or numerical sample requirement designed |
| Q7 | Construction and validation of forecasts, uncertainty, and any lambda/J interpretation | No forecast schema or confidence conversion adopted |
| Q8 | Procedure/version boundaries for M; deterministic accounting versus model responsibilities | No software boundary design, repository initialization, or engine build; Q8 does not select a trading policy |
| Q9 | Risk/resource limits, acceptable failure, search budget, funding feasibility, and stopping | No capital, loss, time, or spending limit invented |
| Q10 | Final delta_F/delta_E; evidence standard; repetition across periods; advancement and project-viability criteria; reconciliation of the full policy pi before any separately approved economic experiment | No numerical threshold, risk normalization, policy selection, or authorization for experimentation |

Cross-cutting unresolved accounting choices include valuation time and discounting, currency conversion, tax scope if applicable, funding and opportunity-cost treatment, operating-cost allocation, and opening/terminal inventory treatment. Their definitions must be coherent before use; no preferred values or venue rules are assumed.

## Evidence gathered and limitations

| ID | Source / kind | What was verified | Limit |
| --- | --- | --- | --- |
| Q2-S01 | [Wolfers and Zitzewitz (2006), FRBSF Working Paper 2006-11, April 16 draft](https://fraser.stlouisfed.org/title/working-papers-federal-reserve-bank-san-francisco-7038/interpreting-prediction-market-prices-probabilities-639221/fulltext); primary paper in Federal Reserve archive, accessed 2026-09-17 UTC | Their model gives sufficient conditions for prices to equal mean beliefs and examines departures; in many modeled cases prices approximate those beliefs | Not a validation of any actual benchmark or a proof that aggregate beliefs are accurate |
| Q2-S02 | [Glosten and Milgrom (1985), Bid, Ask, and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders](https://business.columbia.edu/faculty/research/bid-ask-and-transaction-prices-specialist-market-heterogeneously-informed-traders); primary author-institution abstract, accessed 2026-09-17 UTC | A theoretical specialist market can have information-related spreads even with a risk-neutral specialist earning zero expected profits | Abstract-level verification; not evidence about any present prediction-market fee, depth, or execution process |
| DER-02 | Signed cash-flow identity and conditional binary derivations in this document | Internal mathematical accounting under stated assumptions | Does not establish real contract details or feasibility |
| DER-03 | Conditional-expectation/covariance derivation and invented arithmetic example | Execution-conditioned outcomes can change expected cash value | No market data or empirical experiment; no frequency or covariance estimated |
| D0001 / SRC-01 | Prior proper-scoring source and Q1 derivation, linked in D0001 | Forecast-loss meaning and distinction from a profitable purchase | No new validation of the proposed method |

No venue fee schedule or market outcome dataset was collected. The methodological sources provide reasons for these distinctions, not evidence that a tradable advantage exists.

Assumptions still requiring verification are feasibility of an eligible population and valid benchmark, legitimate contemporaneous information, auditable outputs, executable transactions, reliable settlement, adequate data and resources, and coherent total costs. Failure of any may require revision or stopping under a later approved rule. None is asserted as an established empirical fact.

## Alternatives considered

| Alternative | Assessment |
| --- | --- |
| Call model–market disagreement edge | Easy to compute but does not establish either side's accuracy, net value, or executable terms; reject as the project's terminology. |
| Use forecast-score gain as a synonym for economic edge | Mixes score and monetary units; preserve forecast edge as a separate first claim. |
| Treat plug-in EV as established economic edge | Makes the forecast/execution assumptions validate themselves; label it estimated EV. |
| Subtract an arbitrary uncertainty penalty as if it were a fee | Blurs cash accounting and a decision preference; report a separately justified adjustment. |
| Use realized profit alone | Observable but sensitive to chance, coverage, dependence, scale, and accounting; report it as evidence under a later valid protocol. |
| Define economic edge with net policy expectancy and separate viability requirements | Recommended; binds claims to a declared scope while preserving honest uncertainty and economic relevance. |

## Proposed decision and exact scope

**Recommendation: ADVANCE**, subject to the user's Q2 decision. Approve the qualified definitions, cash-flow framework, separation of target/estimate/adjustment/realization, complete-opportunity coverage requirement, and cost reconciliation principles above. Keep the particular binary formulas conditional on their explicit assumptions.

Gate 2 prevents unsupported profitability claims; it does not require profitable results before we can approve definitions. Closing Q2 would approve this framework with its explicit dependencies, not a fully instantiated contract model or a final statistical/economic criterion. Those must be supplied and approved before experiments or substantive profitability claims.

**What approval and explicit continuation would unlock:** Q3 research to select and justify the benchmark, with its own proposed decision and stop point.

**What remains outside scope:** solving Q4–Q10 early, selecting a deployed strategy or policy, running empirical experiments or paper trading, paid commitments, live actions, repository setup, and engine development. The user's repository deferral remains in force.

The user can approve this proposal and Q3-only continuation, request revisions, or stop. No Q2 decision has been made on the user's behalf.
