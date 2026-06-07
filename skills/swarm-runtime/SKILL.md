---
name: swarm-runtime
description: >-
  Among-Check swarm runtime orchestration — Hub, Sandboxes, Anchors, Markers,
  Sweeps, and Gate. Use when coordinating multi-agent fix work, assigning tasks,
  or implementing runtime CLI/MCP in packages/core.
---

# Swarm Runtime

**Scope:** Fix-swarm coordination layer (not individual scanners).

## When to invoke

- Implementing `sandbox`, `anchor`, `marker`, `sweep`, `gate` CLI commands
- Designing git worktree persistence for coding agents
- Coordinating multiple scouts across long sessions
- Syncing `audits/delta.toon` → `markers/open/`

## Hierarchy (memorize)

```
Hub (.among-check/)
 └── Sandbox (one git repo)
      ├── Anchors (git worktrees + state.toon)
      ├── Markers (git-backed tasks)
      ├── Sweeps (batched marker assignments)
      └── Gate (verify-then-merge queue)
```

## Hard rules

1. **Commander attach** — humans and editors start here; scouts do not self-orchestrate
2. **One sandbox per repo** — strict isolation
3. **Markers in git** — never task-only-in-chat for multi-session work
4. **Anchors for persistence** — scout state survives restarts via worktree + `state.toon`
5. **Gate before main** — when `gateRequired: true`, no direct merges from scouts
6. **tmux for parallel scouts** — document multiplexer use for stable sessions

## Commander session checklist

1. Read `.among-check/hub.toon` and active sandbox
2. Read `markers/index.toon` and `audits/latest.toon`
3. Run `marker sync-audit` logic if new findings lack markers
4. Create or resume **Anchors** per assignee
5. Bundle markers into **Sweeps**; delegate to scout skills
6. On sweep complete → **Gate** enqueue → White re-scan

## References

- [docs/swarm-runtime.md](../../docs/swarm-runtime.md)
- [docs/architecture.md](../../docs/architecture.md) §16
- [skills/orchestrator/SKILL.md](../orchestrator/SKILL.md)
