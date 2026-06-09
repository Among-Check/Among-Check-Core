# Claude Code — Among-Check Core

**Tagline:** Find imposters among codebase.

You are working on **Among-Check Core**, a security scanner agent swarm.

## Start here

- [AGENTS.md](AGENTS.md) — universal agent rules
- [docs/swarm-runtime.md](docs/swarm-runtime.md) — Commander attach, Markers, Anchors, Gate
- [docs/sandbox.md](docs/sandbox.md) — Docker isolation (all tool execution runs inside container)
- [docs/architecture.md](docs/architecture.md) — technical source of truth §1–§19
- [docs/scanner-catalog.md](docs/scanner-catalog.md) — scanner IDs
- [audits/latest.toon](audits/latest.toon) — latest TOON security audit
- [docs/audit-archive.md](docs/audit-archive.md) — audit version control
- [skills/README.md](skills/README.md) — agent identities (invoke before implementing scanners)

## Your role

Implement scanners, orchestrator plumbing, CLI, and MCP tools per the architecture doc. Each finding must ship with an actionable **AI-ready fix prompt**.

## Commands (once scaffold exists)

```bash
pnpm install
pnpm build
pnpm test
pnpm among-check scan --url https://example.com
```

## Multi-agent work

Start every session with **`/commander`** — read `markers/index.toon` and `.among-check/hub.toon` before delegating to scouts.

## Do not

- Micromanage scouts without Commander attach
- Mix codebases in one Sandbox
- Invent repository structure not in `docs/architecture.md`
- Add destructive exploit payloads
- Skip registry registration for new scanners
- Create commits unless the user asks

## Philosophy

An **imposter** is something that looks secure but is not (fake auth, unsigned webhooks, permissive RLS). Find and report them with evidence and fixes.
