# Immutable evidence archive

The documentation is directly browsable in GitHub. Large data and manifest files are delivered as numbered ZIP parts because the connected upload service limits individual request size. Their original uncompressed bytes and relative paths are preserved.

From the repository root, run in PowerShell 7:

```powershell
pwsh -File audit/Restore-Evidence.ps1
```

The script verifies every part, the complete archive, and every payload file against SHA-256 records. It restores missing files to their original paths and refuses to overwrite a differing existing file. It uses no network, credentials, or paid services. Restored files are ignored by Git; the committed archive is the portable source of those bytes.

Then follow the study READMEs. Restoration and replay do not create fresh validation evidence. This utility packages research data; it is not the proposed evaluation engine.

`ARCHIVE.json` records the part order, byte counts, complete archive hash, and payload count. The ZIP contains `__PAYLOAD_MANIFEST__.json` with each restored file's original path, size, and hash. `PACKAGE_MANIFEST.json` at the repository root describes the committed delivery files, not the optional restored working files. The earlier full-tree manifest is retained inside the archive under `docs/history/pre-archive-delivery/`.
