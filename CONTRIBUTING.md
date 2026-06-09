# Contributing to Among-Check Core

**Tagline:** Find imposters among codebase.

This project is designed for both **human contributors** and **coding agents**.

---

## For coding agents

Read in order before making any change:

1. [AGENTS.md](AGENTS.md) — universal agent rules
2. [docs/swarm-runtime.md](docs/swarm-runtime.md) — Commander attach, Markers, Anchors, Gate
3. [docs/architecture.md](docs/architecture.md) — technical source of truth (§1–§19)
4. [docs/scanner-catalog.md](docs/scanner-catalog.md) — scanner IDs
5. [docs/sandbox.md](docs/sandbox.md) — Docker isolation (required for probe execution)

Editor-specific entry points:

- **Cursor:** `.cursor/rules/`, `.cursor/mcp.json` — skills live in `skills/`
- **Claude Code:** `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/` — start with `/commander`
- **Agent identities:** `skills/<agent>/SKILL.md` — see [skills/README.md](skills/README.md)

---

## For humans

### Development setup

```bash
# 1. Install dependencies (after Phase 0 scaffold)
pnpm install
pnpm build
pnpm test

# 2. Build the Docker sandbox image
docker build -f docker/scanner.Dockerfile -t among-check-scanner .

# 3. Run a scan (all probes execute inside the sandbox)
docker run --rm --read-only --tmpfs /tmp:rw,size=256m \
  --cap-drop ALL --security-opt no-new-privileges \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --url https://example.com
```

See [docs/sandbox.md](docs/sandbox.md) for full Docker run options and CI integration.

### Security audit archive

Every scan commits TOON files under `audits/`. See [docs/audit-archive.md](docs/audit-archive.md). Read `audits/latest.toon` before any security work.

### Adding a scanner

1. Open or file a [scanner request](.github/ISSUE_TEMPLATE/scanner_request.md)
2. Add the ID to [docs/scanner-catalog.md](docs/scanner-catalog.md)
3. Read the owning agent's `skills/<agent>/SKILL.md` — check its `## External skills` table for relevant playbooks
4. Implement per [architecture.md §13](docs/architecture.md#13-adding-a-new-scanner)
5. Open a PR using the [pull request template](.github/pull_request_template.md)

### Adding a Marker (task)

```bash
# From hub root after Commander attach
among-check marker create --title "Fix supply.leaked-aws-key" --assignee Orange
# or copy markers/open/marker-example.toon and commit
```

### Commit style

```
feat(scanner): add config.missing-hsts
feat(core): orchestrator timeout handling
feat(runtime): marker sync-audit command
fix(mcp): correct scan tool schema
docs: update scanner catalog
chore(security): among-check audit 2026-06-10T... (3 findings)
```

---

## Code of conduct

- Non-destructive security research only on systems you own or have permission to test
- Never commit secrets, tokens, or customer data
- Redact sensitive values in reports and fixtures
- All tool execution inside Docker sandbox

---

## Questions

Open a [feature request](.github/ISSUE_TEMPLATE/feature_request.md) or [bug report](.github/ISSUE_TEMPLATE/bug_report.md).
