# Audit Archive — TOON Version Control

**Tagline:** Find imposters among codebase.

Every Among-Check run **persists a security audit to git** in **[TOON](https://toonformat.dev/)** (Token-Oriented Object Notation). Coding agents read this history to understand what was already found, what was fixed, and what regressed — without burning tokens on full JSON dumps.

---

## Why TOON

| Concern | TOON benefit |
|---------|----------------|
| Agent context | ~40% fewer tokens vs JSON for uniform finding lists |
| Structure | Explicit `[N]{fields}:` headers help models parse reliably |
| Git diffs | Line-oriented text diffs cleanly in PRs |
| Round-trip | Lossless encode/decode to JSON (`ScanReport`) |

Use the [`@toon-format/toon`](https://github.com/toon-format/toon) package with **strict mode** on decode.

---

## Where audits live

Audits are written to the **git root of the scan target** (the app under test), not inside `packages/`:

```
<target-repo>/
└── audits/
    ├── README.md           # Human + agent guide (committed)
    ├── index.toon          # Manifest: all runs, newest first
    ├── latest.toon         # Copy of most recent full report (agent default)
    └── history/
        └── 2025-06-08T12-30-45Z/
            ├── report.toon       # Full ScanReport in TOON
            ├── findings.toon     # Tabular findings only (fast agent read)
            ├── delta.toon        # Diff vs previous run (optional)
            └── commit.json       # Git commit sha after archive (metadata)
```

Among-Check Core **dogfoods** the same layout at repo root (`audits/`) when scanning itself.

---

## When commits happen

After every successful scan (CLI, MCP, CI, or API), the **audit archiver** pipeline runs:

1. Encode `ScanReport` → TOON
2. Write files under `audits/`
3. Update `index.toon` and `latest.toon`
4. Compute `delta.toon` against previous `latest.toon` (if exists)
5. **Git commit** with conventional message (default **on**)

```
chore(security): among-check audit 2025-06-08T12:30:45Z (3 findings)
```

### Opt-out

```bash
among-check scan --repo . --no-audit-commit
# or
AMONG_CHECK_AUDIT_COMMIT=false
```

---

## TOON schemas

### `findings.toon` (tabular — primary agent read)

```toon
scanId: ac_20250608_123045
finishedAt: 2025-06-08T12:30:12Z
durationMs: 27000
target:
  repoPath: .
stats:
  total: 3
  bySeverity:
    critical: 0
    high: 1
    medium: 2
    low: 0
    info: 0
findings[3]{id,severity,category,location,title}:
  config.missing-hsts,high,configuration,https://example.com/,Missing Strict-Transport-Security
  vuln.open-redirect,medium,vulnerability,/api/redirect,User-controlled redirect target
  supply.leaked-token,medium,supply-chain,src/config.ts:42,Possible API token in source
```

### `index.toon` (manifest)

```toon
project: among-check-core
updatedAt: 2025-06-08T12:30:12Z
runs[2]{scanId,finishedAt,findings,high,critical}:
  ac_20250608_123045,2025-06-08T12:30:12Z,3,1,0
  ac_20250607_090000,2025-06-07T09:00:00Z,5,2,0
```

### `delta.toon` (regression signal)

```toon
previousScanId: ac_20250607_090000
currentScanId: ac_20250608_123045
new[1]{id,severity,location}:
  vuln.open-redirect,medium,/api/redirect
resolved[2]{id,location}:
  config.missing-hsts,https://example.com/
  supply.leaked-token,src/config.ts:42
unchanged: 0
```

---

## Agent workflow

Coding agents **should read before implementing security fixes**:

1. `audits/latest.toon` — current state
2. `audits/history/<timestamp>/delta.toon` — what changed since last run
3. Individual finding `aiFixPrompt` in `report.toon` (full detail)

After fixing issues, re-run scan; a new commit lands in `audits/history/` and agents verify `resolved[]` in `delta.toon`.

### MCP tool

`among_check_read_audit` — returns `latest.toon` + `delta.toon` as MCP resources (implement in Phase 4).

---

## Redaction rules (before write/commit)

- Replace secret values in evidence with `***`
- Truncate request/response bodies to 2 KB
- Never store raw `TestActor` bearer tokens in TOON files
- Hash stable target URLs if they contain query secrets (`urlHash` field)

---

## CI integration

`.github/workflows/audit.yml` (in consumer repos) should:

1. Run `among-check scan --repo .`
2. Fail on critical/high (exit code `1`)
3. Push audit commit to same PR branch (or open bot PR with `audits/` only)

Among-Check Core CI validates archiver unit tests and golden TOON fixtures.

---

## Related

- [architecture.md §14](./architecture.md#14-audit-archive-toon-version-control) — implementation interfaces
- [AGENTS.md](../AGENTS.md) — agent rules for reading `audits/`
