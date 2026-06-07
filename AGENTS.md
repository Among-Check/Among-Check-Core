# AGENTS.md — Among-Check Core

**Tagline:** Find imposters among codebase.

Instructions for **all coding agents** (Cursor, Claude Code, Copilot, etc.) working in this repository.

---

## Read first

1. [docs/architecture.md](docs/architecture.md) — **how to build** (layouts, interfaces, phases)
2. [docs/overview.md](docs/overview.md) — **what we build** (product intent)
3. [docs/scanner-catalog.md](docs/scanner-catalog.md) — scanner IDs (do not invent new IDs without updating catalog)
4. [audits/latest.toon](audits/latest.toon) — **current security audit** (TOON; read when fixing security issues)
5. [docs/audit-archive.md](docs/audit-archive.md) — TOON archive format and git commit behavior
6. [skills/README.md](skills/README.md) — **agent identities** (Commander, Red, Blue, …)
7. [docs/agent-skills.md](docs/agent-skills.md) — which skill to invoke per task

---

## Project summary

Among-Check Core is a TypeScript monorepo: an **agent swarm** of security scanners behind a shared orchestrator, CLI, and MCP server. Full scan target: **< 30 seconds**, **100+ checks**, every finding includes an **AI-ready fix prompt**. Every run **archives results to `audits/` in TOON** and **commits to git** by default so agents retain security history.

---

## Hard rules

- Follow the package layout in `docs/architecture.md` — no alternate structures
- Every scanner implements the `Scanner` interface and registers in `packages/agents/src/index.ts`
- Every `Finding` must include `aiFixPrompt` via `buildAiFixPrompt()`
- Scanner IDs must match `docs/scanner-catalog.md`
- Non-destructive probes only; redact secrets in evidence
- Minimal diffs — do not refactor unrelated code
- Do not commit credentials, `.env`, or real customer data
- Every scan must flow through `archiveScanReport()` — write TOON under `audits/`, update `latest.toon`, commit unless `archive.commit: false`
- Read `audits/latest.toon` and latest `delta.toon` before working on security fixes

---

## Implementation order

Follow **Phase 0 → 4** in [docs/architecture.md §10](docs/architecture.md#10-implementation-phases-agents-follow-in-order). Do not skip scaffold (Phase 0) to add feature scanners early.

---

## Code conventions

- **Language:** TypeScript (strict), Node 20+
- **Package manager:** pnpm workspaces
- **Tests:** Vitest, colocated `*.test.ts`
- **IDs:** kebab-case (`config.missing-hsts`)
- **Files:** `{name}.scanner.ts` under `packages/agents/{category}/`

---

## Agent identities

Each swarm member has a skill in `skills/<agent>/SKILL.md`:

| Codename | Skill | Scope |
|----------|-------|-------|
| Commander | `orchestrator` | Orchestrator, registry |
| Red | `agent-vuln` | `vuln.*` |
| Blue | `agent-config` | `config.*` |
| Green | `agent-infra` | `infra.*` |
| Orange | `agent-supply` | `supply.*` |
| Purple | `agent-tenant` | Tenant isolation |
| Yellow | `agent-webhook` | Webhook signatures |
| Cyan | `agent-browser` | Browser storage |
| White | `agent-audit` | TOON archive |
| Pink | `agent-fix` | AI fix prompts |

**Invoke the owning agent's skill** before implementing its scanners.

## When adding a scanner

1. Identify owning agent in [skills/registry.toon](skills/registry.toon)
2. Read that agent's `skills/<agent>/SKILL.md`
3. Add/update `docs/scanner-catalog.md`
4. Implement scanner + unit test
5. Register in agents barrel
6. Run tests for affected packages

---

## When unsure

- Prefer extending `packages/shared` over duplicating HTTP/git parsing
- Prefer `[]` (no findings) over throwing when target type does not apply
- Ask for human review before adding new external API dependencies
