# Markers — git-backed task tracker

**Markers** are atomic work units for the Among-Check fix swarm. They live in git so scouts always read the current source of truth — not stale chat context.

## Layout

| Path | Purpose |
|------|---------|
| `index.toon` | Manifest of all markers, newest first |
| `open/` | Active markers awaiting work |
| `closed/` | Completed or cancelled markers |

## For coding agents

1. **Commander attach first** — do not pick markers ad hoc without reading `index.toon`
2. Read `audits/latest.toon` when a marker has `source: audit`
3. Work only in your assigned **Anchor** worktree branch
4. Close marker only after acceptance criteria pass and Gate approves (if enabled)

## Creating markers

- **From audit:** Commander runs `among-check marker sync-audit` (planned) after scan
- **Manual:** `among-check marker create --title "..." --assignee Blue` (planned)
- **Humans:** copy `markers/open/marker-example.toon` and commit

See [docs/swarm-runtime.md](../docs/swarm-runtime.md).
