# Independent arithmetic review — EXP-0002

Prepared: 2026-09-19T21:11:00.208384+00:00.

**Point-score cross-check passed.** All recomputed raw-market, normalized-market, weather-mixture, uniform-comparator Brier scores and paired gains agree with the recorded results within 1e-12. Maximum absolute difference: **8.3266726846886741e-17**.

The independent calculation used the saved, fixed configuration **bias +1 degree Fahrenheit, standard deviation 1.5 degrees Fahrenheit, weather weight 0.5**. It read every eligible event from `prepared-events.json`, recomputed normalized market probabilities from raw midpoint vectors, constructed the discretized-normal probabilities using standard-library `math.erf` and the registered half-degree continuity correction, and averaged losses with `math.fsum`. It did not import `analyze.py`, SciPy, or NumPy for scoring. No parameter was refitted and no events, filters, horizons, or methods were changed.

| Split | Events | Raw-market Brier | Normalized-market Brier | Candidate Brier | Uniform Brier | Paired gain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| train | 113 | 0.121128318584071 | 0.120462744116265 | 0.114466187839453 | 0.138888888888889 | 0.00599655627681244 |
| validation | 58 | 0.0945308189655172 | 0.0952401415726102 | 0.104007825233527 | 0.138888888888889 | -0.00876768366091711 |
| test_a | 88 | 0.106679403409091 | 0.107078028333895 | 0.108790608847976 | 0.138888888888889 | -0.00171258051408061 |
| test_b | 62 | 0.101929838709677 | 0.10181347597393 | 0.0993411031260142 | 0.138888888888889 | 0.0024723728479158 |
| test_pooled | 150 | 0.10471625 | 0.104902013358443 | 0.104884813149565 | 0.138888888888889 | 1.72002088779061e-05 |

Training and validation means were also checked against `fit-lock.json`. Event counts and fixed-configuration agreement were verified. Detailed values, differences, and input hashes are retained in `numeric-crosscheck.json`.

## Interpretation and limits

This verifies numerical scoring and aggregation from the prepared inputs. It is separate from the pretest code/synthetic review in `pretest-review.json`, and it does not turn an inconclusive or failed screen into evidence of edge. The study still fails its registered screen: Test B has 62 eligible dates out of 91 (about 68.13%, below the 70% minimum), and neither quarter has the required positive lower bound above the scientific hurdle.

The review does not independently certify source truth, labels, original market rule versions, actual historical weather publication, missingness assumptions, fitted-parameter optimality, bootstrap coverage, future persistence, executable transactions, or economic viability. Bootstrap intervals were not recomputed. Historical MOS publication timing remains assumed; the study is exploratory and was selected after EXP-0001. Arithmetic agreement is not an empirical advantage claim.

Only new review artifacts were written; the frozen protocol, inputs, analysis code, fit lock, and results were not altered.
