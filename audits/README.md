# Security audit archive

This directory is **version-controlled audit history** for Among-Check scans, stored in **[TOON](https://toonformat.dev/)** (Token-Oriented Object Notation) for efficient agent consumption.

## Files

| File | Purpose |
|------|---------|
| `latest.toon` | Most recent scan — **read this first** |
| `index.toon` | Manifest of all runs |
| `history/<iso-timestamp>/report.toon` | Full report per run |
| `history/<iso-timestamp>/findings.toon` | Tabular findings only |
| `history/<iso-timestamp>/delta.toon` | New / resolved findings vs previous run |

## For coding agents

1. Open `latest.toon` before changing security-sensitive code.
2. After fixes, expect a new commit: `chore(security): among-check audit …`
3. Check `delta.toon` for regressions (`new[]`) and fixes (`resolved[]`).

See [docs/audit-archive.md](../docs/audit-archive.md).
