# Contributing to Among-Check Core

**Tagline:** Find imposters among codebase.

Thank you for helping build the agent swarm. This project is designed for both **human contributors** and **coding agents**.

---

## For coding agents

Read these in order:

1. [AGENTS.md](AGENTS.md)
2. [docs/architecture.md](docs/architecture.md)
3. [docs/scanner-catalog.md](docs/scanner-catalog.md)

Editor-specific entry points:

- **Cursor:** `.cursor/rules/`, `.cursor/mcp.json`
- **Claude Code:** `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`
- **Agent identities:** `skills/<agent>/SKILL.md` — see [skills/README.md](skills/README.md)

---

## For humans

### Development setup (after Phase 0 scaffold)

```bash
pnpm install
pnpm build
pnpm test
```

### Security audit archive

Every scan commits TOON files under `audits/`. See [docs/audit-archive.md](docs/audit-archive.md). Agents should read `audits/latest.toon` before security work.

### Adding a scanner

1. Open or file a [scanner request](.github/ISSUE_TEMPLATE/scanner_request.md)
2. Add the ID to `docs/scanner-catalog.md`
3. Implement per [architecture.md §13](docs/architecture.md#13-extension-adding-a-new-scanner)
4. Open a PR using the [pull request template](.github/pull_request_template.md)

### Commit style

- `feat(scanner): add config.missing-hsts`
- `feat(core): orchestrator timeout handling`
- `fix(mcp): correct scan tool schema`
- `docs: update scanner catalog`

---

## Code of conduct

- Non-destructive security research only on systems you own or have permission to test
- Never commit secrets, tokens, or customer data
- Redact sensitive values in reports and fixtures

---

## Questions

Open a [feature request](.github/ISSUE_TEMPLATE/feature_request.md) or [bug report](.github/ISSUE_TEMPLATE/bug_report.md).
