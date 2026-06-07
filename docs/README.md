# Documentation

**Among-Check Core** — *Find imposters among codebase.*

| Document | Audience | Purpose |
|----------|----------|---------|
| [overview.md](./overview.md) | Everyone | Product capabilities and philosophy |
| [architecture.md](./architecture.md) | Engineers & coding agents | Technical design, interfaces, phases |
| [scanner-catalog.md](./scanner-catalog.md) | Implementers | Stable scanner IDs and status |
| [audit-archive.md](./audit-archive.md) | Engineers & agents | TOON audit archive in git |
| [../audits/latest.toon](../audits/latest.toon) | Coding agents | Latest committed security audit |

## Agent entry points

| Tool | Location |
|------|----------|
| Universal | [AGENTS.md](../AGENTS.md) |
| Claude Code | [CLAUDE.md](../CLAUDE.md), [.claude/](../.claude/) |
| Cursor | [.cursor/rules/](../.cursor/rules/), [.cursor/mcp.json](../.cursor/mcp.json) |
| Contributing | [CONTRIBUTING.md](../CONTRIBUTING.md) |

## Implementation status

Documentation and agent scaffolding are in place. Application code follows **Phase 0** in [architecture.md §10](./architecture.md#10-implementation-phases-agents-follow-in-order).
