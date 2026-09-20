# Independent arithmetic review — EXP-0001

An independent reviewer recomputed raw-market, normalized-market, and fixed-candidate Brier scores and paired means from `prepared-events.json`, using the beta in `fit-lock.json`, and compared the results with `results.json`. This check occurred after test exposure and did not select another method, parameter, filter, or sample.

The independent calculation used Python standard-library arithmetic with `math.fsum`; it did not call `analyze.py`, its scoring function, or NumPy reductions. Normalized probabilities and the beta-power transformation were recomputed from each saved raw midpoint vector. Every saved eligible event was retained. Event counts and beta consistency were checked, and training/validation means were also compared with the fit lock.

**Result: all comparisons agreed within 1e-12.** The maximum absolute difference was **2.7755575615628914e-17** (approximately 2.78e-17), consistent with floating-point summation order. The locked beta was **1.25**.

| Split | Eligible events | Raw-market Brier | Normalized-market Brier | Candidate Brier | Paired gain |
| --- | ---: | ---: | ---: | ---: | ---: |
| Train | 118 | 0.11155473163841807 | 0.11140912858822687 | 0.11063809542626601 | 0.0007710331619608489 |
| Validation | 59 | 0.10986186440677966 | 0.10979930888511990 | 0.10831769888475494 | 0.0014816100003649790 |
| Test A | 90 | 0.12058439814814816 | 0.12059363503264323 | 0.12020656380536740 | 0.0003870712272758302 |
| Test B | 90 | 0.11359759259259260 | 0.11368603550226884 | 0.11330756838655635 | 0.0003784671157124921 |
| Tests pooled | 180 | 0.11709099537037036 | 0.11713983526745603 | 0.11675706609596188 | 0.0003827691714941612 |

Paired gain is the mean of each event's normalized-market loss minus candidate loss. Positive values favor the candidate. The small positive point estimates do not overturn the registered NOT_ESTABLISHED conclusion.

## Scope and limits

This verifies scoring and aggregation from the supplied prepared inputs. It does not independently certify the exchange archive, labels, historical information availability, missingness assumptions, fitted-parameter optimality, bootstrap coverage, future persistence, executable fills, or economic viability. Bootstrap intervals were not recomputed in this cross-check. No additional search or empirical result was introduced, and no original study files were edited.

Before test exposure, the reviewer separately inspected the analysis code and protocol/amendment documents for train-only fitting, timestamp filters, categorical normalization, grouping, provenance checks, locked dependencies, exclusion reporting, and unavailable-bootstrap handling. That code review is recorded in `pretest-review.json`; it is distinct from this post-exposure numerical check.

The updated `presentation/validation-summary.png` was visually inspected during packaging. Its title, normalized-market/candidate legend, hurdle legend, axes, and qualification of the 5th/95th percentile bounds are readable. Visual QA is not statistical validation.
