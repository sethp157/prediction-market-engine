# Repository migration integrity audit

Recorded: 2026-09-20T16:34:40.1199506Z.

Status: PASSED for the copied studies and preserved pre-handoff snapshots.

This was a read-only hash and inventory audit using native PowerShell Get-FileHash and ConvertFrom-Json. No analysis, model fitting, outcome scoring, parameter search, or network operation was performed. Only this audit record was added.

| Study | Files compared with original | Manifest entries verified | Raw response files | Locked dependency hashes |
| --- | ---: | ---: | ---: | ---: |
| EXP-0001 | 2225 | 2224 | 2201 | 6 |
| EXP-0002 | 2587 | 2586 | 2563 | 9 |

Both complete study inventories match the original delivered package. Every copied file, including each per-study manifest, has the same SHA-256 as its source. Every manifest-listed size/hash matches the repository copy. Frozen protocol bytes, analysis/prepared-input hashes, and all fit-lock dependency hashes remain valid. EXP-0002 also retains all three hashes binding its independent numerical audit to its original inputs.

## Preserved study hashes

### EXP-0001

- Per-study manifest: `e5ceca64ca2556f110fea0da158c347a3f6a9070fbfb376a1a5a201ca24deb7b`
- Frozen protocol: `dca4b858076c254585e2f0e28399826555ab56a0bd3029f941c64b19be26fd30`
- Analysis script: `2c02bf72e594652ad23803b89f4de820de61a4dbf21ad57dcd60c31554d7d79c`
- Recorded results: `079ff64d288d86f168908beff7e1d37d6a6c7947ee0cf46912b86aaba71140f2`

### EXP-0002

- Per-study manifest: `fee7718858ad6209d8064e3fc9c7868806e984fb77d997ad1b4287e9b207684b`
- Frozen protocol: `d7672bf369cf297cfa4b87b92be8396a05c09e4e81b2cc6e16b0c3fa395df098`
- Analysis script: `9078bdcbea90cebd1abec9e2f6e8acc2f3f3f302604f3c893ef0757483e9c82a`
- Recorded results: `5bd73d12263ccd577c16221016b44745f4a7763e3a522d6f841a31ead6118a95`

## History and line endings

Seven pre-handoff records were checked byte-for-byte against the original package: the four governing documents, root README, former root PACKAGE_MANIFEST.json, and former docs/final-document-review.json. They are preserved under docs/history/pre-repository-handoff. Their scope is the earlier package, not newly edited repository governance.

The repository .gitattributes contains `* -text`, preserving file bytes rather than applying Git text line-ending conversion. This matters for the frozen CSV, JSON, Python, Markdown, and raw-response hashes. No claim about a future checkout or remote object has been made by this working-tree audit.

## Limits and remaining handoff check

The current root PACKAGE_MANIFEST.json was not certified by this audit: governing documentation is being updated, and the root inventory must be rebuilt and checked after those edits. Historical root-manifest and review hashes must not be presented as a review of the revised current state.

Study README reproduction instructions retain the original absolute Windows paths and exact environments as historical provenance. Repository-level instructions may provide portable paths without changing the frozen study files. Replaying exposed data remains an arithmetic check, not fresh evidence.

No study scripts were executed or rewritten, and no new scientific results were produced. The earlier numerical reviews are preserved; this audit verifies their inputs remain identical rather than repeating their calculations. Source truth, historical availability, statistical assumptions, economic viability, and data rights are outside this hash check.

No commit SHA, push, remote publication, fresh-clone verification, or evaluation-engine implementation is asserted here.

## Archive delivery verification

Large payload files are stored in checksum-verified archive parts because the connected GitHub app limits request size. The archive contains 4,774 files at their original relative paths. The restoration utility verified every part, the complete ZIP, and all 4,774 payload file hashes against the existing originals; all matched. It restored zero files during this check because the originals were already present. This preserves the earlier 4,812-file scientific import check and changes delivery layout only. Root PACKAGE_MANIFEST.json covers committed delivery files; original scientific manifests apply after restoration.