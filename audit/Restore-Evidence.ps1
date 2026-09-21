# Restore the immutable evidence from the committed archive parts. No network.
$ErrorActionPreference = 'Stop'
$repoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$rootPrefix = $repoRoot.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar
function Resolve-EvidencePath([string]$relative) {
    if ([IO.Path]::IsPathRooted($relative)) { throw "Absolute archive path: $relative" }
    $full = [IO.Path]::GetFullPath((Join-Path $repoRoot $relative))
    if (-not $full.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase) -or $relative -match '(^|[\\/])\.git([\\/]|$)') {
        throw "Archive path outside the evidence workspace: $relative"
    }
    return $full
}
function Get-BytesHash([byte[]]$bytes) {
    $algorithm = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($algorithm.ComputeHash($bytes)).Replace('-', '').ToLowerInvariant() }
    finally { $algorithm.Dispose() }
}
$record = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'ARCHIVE.json') -Raw | ConvertFrom-Json
$memory = [IO.MemoryStream]::new()
try {
    foreach ($part in $record.parts) {
        $bytes = [IO.File]::ReadAllBytes((Resolve-EvidencePath $part.file))
        if ($bytes.Length -ne $part.bytes -or (Get-BytesHash $bytes) -ne $part.sha256) { throw "Part integrity failure: $($part.file)" }
        $memory.Write($bytes, 0, $bytes.Length)
    }
    if ($memory.Length -ne $record.archive_bytes -or (Get-BytesHash $memory.ToArray()) -ne $record.archive_sha256) { throw 'Complete archive integrity failure' }
    $memory.Position = 0
    $archive = [IO.Compression.ZipArchive]::new($memory, [IO.Compression.ZipArchiveMode]::Read, $true)
    try {
        $manifestEntry = $archive.GetEntry('__PAYLOAD_MANIFEST__.json')
        if ($null -eq $manifestEntry) { throw 'Payload manifest missing' }
        $reader = [IO.StreamReader]::new($manifestEntry.Open())
        try { $files = @($reader.ReadToEnd() | ConvertFrom-Json) } finally { $reader.Dispose() }
        if ($files.Count -ne $record.payload_file_count -or $archive.Entries.Count -ne ($files.Count + 1)) { throw 'Payload inventory mismatch' }
        # Validate existing destinations before writing anything. Never overwrite.
        foreach ($file in $files) {
            $destination = Resolve-EvidencePath $file.file
            if (Test-Path -LiteralPath $destination) {
                if ((Get-Item -LiteralPath $destination).Length -ne $file.bytes -or (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant() -ne $file.sha256) {
                    throw "Existing file differs; preserve it and use a fresh clone: $($file.file)"
                }
            }
        }
        $restored = 0; $alreadyPresent = 0
        foreach ($file in $files) {
            $entry = $archive.GetEntry($file.file)
            if ($null -eq $entry -or $entry.Length -ne $file.bytes) { throw "Missing or malformed payload entry: $($file.file)" }
            $buffer = [IO.MemoryStream]::new()
            $inputStream = $entry.Open()
            try { $inputStream.CopyTo($buffer); $content = $buffer.ToArray() } finally { $inputStream.Dispose(); $buffer.Dispose() }
            if ((Get-BytesHash $content) -ne $file.sha256) { throw "Payload hash mismatch: $($file.file)" }
            $destination = Resolve-EvidencePath $file.file
            if (Test-Path -LiteralPath $destination) { $alreadyPresent++; continue }
            [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination)) | Out-Null
            $outputStream = [IO.File]::Open($destination, [IO.FileMode]::CreateNew)
            try { $outputStream.Write($content, 0, $content.Length) } finally { $outputStream.Dispose() }
            $restored++
        }
        [pscustomobject]@{archive_verified=$true;payload_files_verified=$files.Count;restored=$restored;already_present=$alreadyPresent} | ConvertTo-Json
    } finally { $archive.Dispose() }
} finally { $memory.Dispose() }
