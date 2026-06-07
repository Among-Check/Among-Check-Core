---
description: Scaffold the next Among-Check implementation phase per architecture.md
---

Scaffold the Among-Check Core monorepo per `docs/architecture.md` §10.

Phase to implement: $ARGUMENTS (default: Phase 0 if omitted)

For Phase 0:
- pnpm workspace, tsconfig.base.json, Vitest, ESLint
- packages/core (types, registry, orchestrator stub)
- packages/shared (logger, http stub)
- packages/cli (`scan`, `list-scanners`)
- packages/agents barrel (empty register)
- packages/mcp stub

Do not skip ahead to feature scanners unless the user explicitly requests a later phase.
