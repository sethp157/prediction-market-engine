# EXP-0001 amendment and exposure log

## A1 — pre-exposure audit clarifications (2026-09-18)

Status: adopted under D0003 delegation before any study performance was calculated or inspected. Collection is in progress. The originally frozen D0004 text/hash is retained unchanged.

- The estimand concerns protocol-eligible archived event-days. The calendar coverage minimum does not establish missing-at-random omissions or performance on excluded days. Report exclusions and conditional scope explicitly.
- If any of the fixed 10,000 bootstrap replicates contains no eligible observations, report that interval as unavailable and the corresponding primary criterion inconclusive; do not silently discard replicates or select a different block length. Report finite-replicate counts.
- Validate every available raw input against its request-manifest SHA-256 and expected URL before analysis. Verify metadata pagination and the derived study subset against those raw pages. An unprovenanced cache file blocks analysis rather than being trusted.
- The manifest's retrieved_at_utc is the request-start timestamp, not response completion. Neither proves that a reconstructed historical observation was available live at its nominal time. Historical-availability limitations remain explicit.
- Bind the analysis, imported collector/cutoff code, prepared inputs, coverage calendar, frozen protocol, this amendment, freeze record, and request manifest by SHA-256 at fit lock, then verify them before test evaluation. Report per-split returned and excluded counts, with separate missing, nonbinary, void, and inconsistent outcome reasons. Nullable/malformed timestamps count as integrity exclusions rather than crashing or being assumed valid; non-final status cannot certify a final outcome. These implement the original integrity requirements.

Rationale: independent review found reporting/provenance edge cases; these changes were made without seeing any study score, selecting a model, or unblinding test performance. They do not alter universe, horizon, candidate family, scoring, thresholds, exclusions, or split dates.
