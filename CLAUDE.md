# Claude Code — Among-Check Core

**Tagline:** Find imposters among codebase.

You are working on **Among-Check Core**, a security scanner agent swarm.

## Start here

- [AGENTS.md](AGENTS.md) — universal agent rules
- [docs/architecture.md](docs/architecture.md) — technical source of truth for codegen
- [docs/scanner-catalog.md](docs/scanner-catalog.md) — scanner IDs
- [audits/latest.toon](audits/latest.toon) — latest TOON security audit
- [docs/audit-archive.md](docs/audit-archive.md) — audit version control

## Your role

Implement scanners, orchestrator plumbing, CLI, and MCP tools per the architecture doc. Each finding must ship with an actionable **AI-ready fix prompt**.

## Commands (once scaffold exists)

```bash
pnpm install
pnpm build
pnpm test
pnpm among-check scan --url https://example.com
```

## Do not

- Invent repository structure not in `docs/architecture.md`
- Add destructive exploit payloads
- Skip registry registration for new scanners
- Create commits unless the user asks

## Philosophy

An **imposter** is something that looks secure but is not (fake auth, unsigned webhooks, permissive RLS). Find and report them with evidence and fixes.
