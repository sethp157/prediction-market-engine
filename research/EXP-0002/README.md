# EXP-0002 audit bundle

Read the [combined research report](../RESEARCH_REPORT.md), [independent arithmetic review](independent-arithmetic-review.md), and [collection audit](collection-audit.md).

The weather-plus-market family did **not establish** its registered replicated forecasting claim. Test A's point gain was negative, Test B's was positive but uncertain, and Test B coverage was 62/91 (68.13%), below the fixed 70% minimum. Historical per-run weather publication timing remains assumed. This is exploratory historical research, not demonstrated economic viability or AI-specific improvement.

## Contents

- `protocol.md`, `protocol-freeze.json`, `clarifications.md`: original fixed design and pre-exposure interpretation of timing, inference, and research history.
- `collect.py`, `analyze.py`: one-off deterministic collection and evaluation scripts. No repository or production engine was created.
- `raw/`: one copy of 2,563 archived responses: 2,190 market candle responses, 365 MOS responses, seven paginated market-metadata responses, and one historical cutoff response. Pagination pages necessarily include some outside-window listing records; dedicated feasibility probes are excluded.
- `request-manifest.jsonl`, `collection-summary.json`, `collection-audit.md`: exact source URLs, request/response times, response hashes and sizes, inventory, and independent collection-audit limits. The audit does not certify precise host-rate ceilings from the recorded wall-clock timestamps.
- `markets-study.json`, `mos-study.json`, `prepared-events.json`, `coverage.json`: source selections/request map, eligible event vectors, and full calendar accounting.
- `fit-lock.json`: training-only fixed configuration, all 125 training-grid losses, training/validation summaries, coverage, and dependency hashes.
- `results.json`, `per-event-results.csv`, `coverage.csv`: frozen evaluation, event-level scores, and retained exclusions.
- `pretest-review.json`: independent code/synthetic review, bound to the exact analysis script.
- `numeric-crosscheck.json`, `independent-arithmetic-review.md`, `independent_numeric_check.py`: post-exposure independent point-score arithmetic audit. The standalone checker reads inputs and prints comparisons; it writes nothing and does not refit.
- `environment.json`, `requirements-reproduction.txt`: interpreter and direct package versions observed during audit/packaging in the study's Python environment, including SciPy.
- `package-manifest.json`: packaged-file byte counts and SHA-256 hashes, excluding itself. It is an integrity inventory, not external timestamp certification.

No `__pycache__`, probes, or collector lock file is included. All copied raw hashes and fit-lock dependencies were checked, and the original working-study files were left unchanged.

## Independent point-score check

The verified interpreter was Windows Python 3.12.2 at:

```text
C:\Users\sethp\AppData\Local\Programs\Python\Python312\python.exe
```

Run the read-only checker from any directory:

```powershell
$studyPython = 'C:\Users\sethp\AppData\Local\Programs\Python\Python312\python.exe'
& $studyPython 'C:\Users\sethp\Documents\Codex\2026-09-16\create-an-image-of-2\outputs\prediction-market-starter\research\EXP-0002\independent_numeric_check.py'
```

This uses standard-library `math.erf` and `math.fsum`, without SciPy/NumPy scoring calls. The recorded maximum point-metric difference was 8.326672684688674e-17 against a 1e-12 tolerance. This is arithmetic agreement, not a new scientific result. It does not recompute bootstrap intervals or verify actual historical publication timing.

## Full numerical replay in a separate copy

Direct dependency versions were NumPy 1.26.4, SciPy 1.13.0, Requests 2.32.3, tzdata 2024.1, and Matplotlib 3.8.4 (for the separately packaged combined presentation). The requirements file can be installed in a separate Python 3.12 environment if needed; full transitive dependencies were not independently locked. Neither network collection nor installation is required to inspect the saved evidence.

`analyze.py prepare` refuses an existing fit or result, and `evaluate` refuses existing results. **Do not remove files from this delivered evidence bundle to bypass those guards.** Replay only in a newly created copy. These commands abort if the replay directory already exists and remove only the generated fit/results files from the new copy:

```powershell
$studySource = 'C:\Users\sethp\Documents\Codex\2026-09-16\create-an-image-of-2\outputs\prediction-market-starter\research\EXP-0002'
$studyReplay = 'C:\Users\sethp\Documents\Codex\2026-09-16\create-an-image-of-2\work\EXP-0002-replay'
$studyPython = 'C:\Users\sethp\AppData\Local\Programs\Python\Python312\python.exe'
if (Test-Path -LiteralPath $studyReplay) { throw 'Choose a new, unused replay directory.' }
Copy-Item -LiteralPath $studySource -Destination $studyReplay -Recurse
Remove-Item -LiteralPath (Join-Path $studyReplay 'fit-lock.json'), (Join-Path $studyReplay 'results.json')
Set-Location -LiteralPath $studyReplay
& $studyPython analyze.py selfcheck
& $studyPython analyze.py prepare
& $studyPython analyze.py evaluate
& $studyPython independent_numeric_check.py
```

Use saved raw inputs; do not run `collect.py` for replay. Recollecting historical data could retrieve a different archive version. The copied original pretest review certifies the original script review; it does not make these exposed test outcomes untouched again.

Replay is a calculation check, **not another experiment, fresh confirmation, or permission to tune**. Fit/result timestamps and file hashes may differ even when scientific values match. Preserve the delivered original files when comparing. Do not change filters, population, forecast horizon, parameter grid, source product, score, threshold, or bootstrap rule to improve the result.

## Claim boundaries

Effects concern eligible archived Miami event-days. Coverage does not imply random missingness. MOS daytime-high and market climate-day targets differ, and runtime + six hours is assumed availability, not an observed historical receipt time. Both temporal uncertainty and source provenance have the limitations described in the protocol, clarification, and collection audit. This second study was selected after the first study's result; no program-wide family-wise error guarantee has been established. No fill, fee, capital-risk, or realized trading-profit model was tested. Further confirmation requires a separate prospective protocol with contemporaneous source receipt records.
