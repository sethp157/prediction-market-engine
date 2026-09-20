# EXP-0001 audit bundle

Start with [the research report](presentation/research-report.md), [the summary chart](presentation/validation-summary.png), and [the independent arithmetic review](independent-arithmetic-review.md).

The fixed calibration did **not establish** the registered replicated forecasting claim. This is historical forecasting research, with no trading or demonstrated economic viability. Test outcomes are exposed; this bundle must not be treated as untouched confirmation for a revised method.

## Contents and evidence status

- `protocol.md`, `protocol-freeze.json`, `amendments.md`: original frozen study and pre-exposure clarification.
- `pretest-review.json`: recorded pre-test implementation review and exposure status.
- `collect.py`, `analyze.py`, `present.py`: one-off collection, analysis, and presentation scripts; no production engine or repository setup.
- `raw/`: one copy of 2,201 original responses: 2,190 study candle responses, 10 paginated metadata responses, and the archive cutoff response.
- `request-manifest.jsonl`: source URLs, request-start timestamps, and original raw SHA-256 hashes. Metadata pages necessarily include listing records outside the study dates because they prove pagination and source selection; dedicated feasibility/probe files are omitted.
- `markets-study.json`, `prepared-events.json`, `coverage.json`: derived study records, eligible event vectors, and complete calendar coverage.
- `fit-lock.json`, `results.json`, `coverage.csv`, `per-event-results.csv`: locked fit, all frozen evaluation outputs, exclusions, and event-level results.
- `presentation/`: report and two rendered figures.
- `environment.json`: unchanged original recorded execution environment. `reproduction-environment.json` additionally identifies the verified interpreter and timezone package.
- `requirements-reproduction.txt`: direct dependency versions used by the original study.
- `package-manifest.json`: SHA-256 and byte count for every packaged file except the manifest itself. It is an integrity inventory, not an independent timestamp certificate.

All copied files were checked byte-for-byte against their working-study sources. The original analysis, prepared events, coverage, imported collector, protocol, amendment, freeze record, and request manifest were also checked against the fit lock before packaging. The original working study was not changed. No cached bytecode, feasibility probes, or duplicate raw directory is included.

## Reproduction environment

Original execution used Windows Python **3.12.2** through `py -3`, resolving to:

```text
C:\Users\sethp\AppData\Local\Programs\Python\Python312\python.exe
```

Direct dependency versions: NumPy 1.26.4, Matplotlib 3.8.4, Requests 2.32.3, and tzdata 2024.1. Timezone data supplies America/New_York on Windows. Use `requirements-reproduction.txt` if installing those versions into a separate Python 3.12 environment. Installation and network collection are not needed to inspect the saved evidence. Transitive dependencies were not fully locked; `environment.json` records the original operating system and package versions.

## Inspect or replay safely

`analyze.py evaluate` deliberately refuses to run when `results.json` already exists. It also checks the locked script, prepared data, and dependency hashes. **Do not remove or overwrite anything in this delivered evidence bundle to bypass that guard.**

For numerical replay, first make a new separate copy. The following PowerShell commands use the actual original interpreter and a new directory under the task's `work` folder. They abort if that replay directory already exists. They remove only generated fit/results files inside the new copy; the original bundle remains intact.

```powershell
$studySource = 'C:\Users\sethp\Documents\Codex\2026-09-16\create-an-image-of-2\outputs\prediction-market-starter\research\EXP-0001'
$studyReplay = 'C:\Users\sethp\Documents\Codex\2026-09-16\create-an-image-of-2\work\EXP-0001-replay'
$studyPython = 'C:\Users\sethp\AppData\Local\Programs\Python\Python312\python.exe'
if (Test-Path -LiteralPath $studyReplay) { throw 'Choose a new, unused replay directory.' }
Copy-Item -LiteralPath $studySource -Destination $studyReplay -Recurse
Remove-Item -LiteralPath (Join-Path $studyReplay 'fit-lock.json'), (Join-Path $studyReplay 'results.json')
Set-Location -LiteralPath $studyReplay
& $studyPython analyze.py selfcheck
& $studyPython analyze.py prepare
& $studyPython analyze.py evaluate
& $studyPython present.py
```

The replay reads the saved raw inputs; do **not** run `collect.py` for this check. `prepare` reconstructs coverage and eligible events, checks raw hashes/URLs and the frozen protocol, fits only on training data, prints training/validation performance, and writes a new fit lock. `evaluate` applies that fit once to the saved test events and writes the same defined statistics. `present.py` regenerates figures/report and the local environment record.

Replay is an arithmetic/reproducibility check, **not new scientific evidence, a fresh test, or another opportunity to choose parameters**. Execution timestamps and derived file hashes may change even when numerical outputs agree. Preserve the original saved artifacts and their hashes when comparing. The original pretest-review record copied into a replay folder remains a historical record; it does not describe a new unexposed test.

Do not change the population, filters, horizon, beta grid, score, thresholds, or statistical procedure to improve the result. A revised scientific method requires a separate protocol and fresh confirmation. Results describe protocol-eligible archived event-days; archive completeness, historical availability, live execution, fees, and profitability remain unvalidated.
