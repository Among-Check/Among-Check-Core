# Documentation

**Among-Check Core** — *Find imposters among codebase.*

---

## Core documents

| Document | Audience | Purpose |
|----------|----------|---------|
| [overview.md](./overview.md) | Everyone | Product capabilities and philosophy |
| [architecture.md](./architecture.md) | Engineers & agents | **Technical source of truth** — §1–§19 |
| [swarm-runtime.md](./swarm-runtime.md) | Engineers & agents | Multi-agent orchestration (Hub, Sandbox, Anchors, Markers, Gate) |
| [sandbox.md](./sandbox.md) | Engineers & agents | **Docker isolation** — all probe execution |
| [agent-skills.md](./agent-skills.md) | Coding agents | Swarm agent roster and skill invoke guide |
| [scanner-catalog.md](./scanner-catalog.md) | Implementers | Stable scanner IDs and implementation status |
| [audit-archive.md](./audit-archive.md) | Engineers & agents | TOON audit archive format, redaction, CI |

---

## Architecture sections quick-ref

| § | Topic |
|---|-------|
| §1 | System context + diagram |
| §2 | Repository layout |
| §3 | Core domain model (types, scanner contract, registry, orchestrator) |
| §4 | Agent swarm execution model + roster + severity rubric |
| §5 | Notable scanner designs (tenant, webhook, browser) |
| §6 | Entry surfaces (CLI, MCP, HTTP API) |
| §7 | AI-ready fix prompts |
| §8 | Shared utilities |
| §9 | Testing strategy |
| §10 | Implementation phases (Phase 0 → R5) |
| §11 | Naming conventions |
| §12 | Security & ethics constraints |
| §13 | Adding a new scanner |
| §14 | Audit archive (TOON version control) |
| §15 | Agent skills |
| §16 | Swarm runtime (Markers, Sweeps, Anchors, Gate) |
| §17 | Docker sandbox |
| §18 | External skills catalog (769 playbooks) |
| §19 | Related documents |

---

## Live agent files

| File | Purpose |
|------|---------|
| [../audits/latest.toon](../audits/latest.toon) | Latest security audit (read before any security work) |
| [../markers/index.toon](../markers/index.toon) | Open work queue |
| [../.among-check/hub.toon](../.among-check/hub.toon) | Hub runtime config |
| [../skills/registry.toon](../skills/registry.toon) | Machine-readable agent roster |

---

## Agent entry points

| Tool | Location |
|------|----------|
| All agents | [AGENTS.md](../AGENTS.md) |
| Claude Code | [CLAUDE.md](../CLAUDE.md), [.claude/commands/](../.claude/commands/) |
| Cursor | [.cursor/rules/](../.cursor/rules/), [.cursor/mcp.json](../.cursor/mcp.json) |
| Contributing | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Docker | [docker/README.md](../docker/README.md) |

---

## Implementation status

Documentation, agent skills (769 playbooks), and Docker sandbox are in place. Application code follows **Phase 0** in [architecture.md §10](./architecture.md#10-implementation-phases).
