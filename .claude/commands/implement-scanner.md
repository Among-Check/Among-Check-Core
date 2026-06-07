---
description: Implement a new Among-Check security scanner from the catalog
---

Implement a scanner for Among-Check Core.

1. Read `docs/architecture.md` (Scanner contract, §5 notable designs, §13 extension guide).
2. Confirm or add the scanner ID in `docs/scanner-catalog.md`.
3. Create `packages/agents/{category}/{name}.scanner.ts` and unit test.
4. Register in `packages/agents/src/index.ts`.
5. Use `buildAiFixPrompt()` for every finding.
6. Run tests for the agents package.

Scanner to implement: $ARGUMENTS

If no argument provided, ask which catalog ID to implement.
