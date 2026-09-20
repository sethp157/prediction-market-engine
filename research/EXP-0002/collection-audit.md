# EXP-0002 collection audit

Completed 2026-09-19, after the archive collection finished at 12:16:51.904830 UTC. This audit examines transport, provenance, request construction, expected-date coverage, and station wording. It does not calculate forecast scores or inspect settlement results. A later root-agent evaluation is a separate step.

Collection is complete: 365 of 365 exact prior-day 06Z KMIA/GFS requests and 2,190 of 2,190 market-candle requests returned HTTP 200 JSON objects. The 2,563 recorded response files comprise 365 MOS responses, 2,190 candle responses, seven market-metadata pages, and one historical-cutoff response. All 365 expected event dates, 2025-07-01 through 2026-06-30 inclusive, are represented in market metadata. All expected MOS and candle files exist. These are collection counts; they do not establish that every event satisfies forecast, quote, or settlement eligibility checks.

`Collector.verify_cache()` passed for all 2,563 responses, checking recorded byte lengths, SHA-256 hashes, file containment, manifest completeness, and UTC request-start fields. A separate reconstruction matched all 2,563 exact request URLs, including metadata cursor pagination, market-candle bounds, and MOS station/runtime/model queries, with no unexpected or missing manifest files. The frozen protocol hash also passed. Successful response files and the original request manifest were preserved.

All 2,190 archived primary market rules name **Miami International Airport** and the **National Weather Service's Climatological Report (Daily)**. The wording specifies the highest temperature recorded at that airport for the named target day. It is consistent with the predeclared Miami airport predictor choice. This station check does not equate the MOS 07:00–19:00 local-standard-time daytime maximum with the settlement report's full-day maximum; that target difference remains a study limitation.

## Request timing limitation and operational record

The executed collector uses a per-host lock, held through each GET, and `time.monotonic()` with intended minimum start intervals of 0.26 seconds for Kalshi and 1.01 seconds for IEM. A process-level OS lock prevents concurrent collectors from writing these files.

The actual **recorded wall-clock** minimum consecutive request-start gaps were:

| Host | Recorded responses | Minimum recorded gap |
| --- | ---: | ---: |
| external-api.kalshi.com | 2,198 | 0.24817609786987305 seconds |
| mesonet.agron.iastate.edu | 365 | 0.996772050857544 seconds |

These gaps are below 0.25 and 1.00 seconds, respectively. Consequently, strict compliance with the protocol's exact subsecond host ceilings cannot be certified from this record. A local diagnostic, without network requests, found differences between Windows monotonic and wall-clock elapsed measurements: 30 requested 0.26-second sleeps produced minimum measured gaps of 0.25 seconds monotonic and 0.2601029872894287 seconds wall-clock, with maximum absolute difference 0.010740041732788086 seconds. Clock resolution, clock behavior, and scheduling may contribute; this diagnostic does not prove what the server observed. Conservatively retain a possible rate-control deviation rather than asserting exact compliance.

A switch to `time.perf_counter()` with larger margins was proposed during the run but **was never executed**. Collection completed during the interruption. The collector was not stopped, restarted, changed, or rerun in response, and no source responses were redownloaded or timestamps rewritten. The collector file audited here has SHA-256 `c14bc0a43ca66afca189bea3b8657507db1f11e5fb45977026de7e4e81fa4bd8`.

`retrieved_at_utc` is an alias of `request_started_at_utc`; `response_received_at_utc` is recorded separately. These are this research run's retrieval timestamps, not historical MOS publication times. The archive's missing per-run historical receipt/publication evidence remains unresolved. HTTP 200 and file-integrity checks also do not substitute for analysis-layer validation of MOS station, model, runtime, horizon, numeric range, and missing/sentinel values.
