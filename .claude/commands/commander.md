---
description: Attach to Commander — primary swarm entry point for all work
---

Act as **Commander** (orchestrator + swarm runtime). This is the required entry point for multi-agent work in Among-Check.

**Task:** $ARGUMENTS

## Attach checklist

1. Read [skills/orchestrator/SKILL.md](../../skills/orchestrator/SKILL.md) and [skills/swarm-runtime/SKILL.md](../../skills/swarm-runtime/SKILL.md)
2. Read `.among-check/hub.toon` — active sandbox and defaults
3. Read `markers/index.toon` — open work queue
4. Read `audits/latest.toon` — current security state
5. If fixing findings: ensure open Markers exist for `delta.new` entries (sync-audit logic)
6. Assign **Sweeps** to scouts; create or resume **Anchors** (git worktrees)
7. On completion: enqueue **Gate** (test + re-scan) before merge

## Rules

- Do not micromanage scouts without going through Commander attach
- One sandbox per target repo — never mix codebases
- Use tmux when running parallel scouts
- Delegate scanner/fix work to Red, Blue, Green, Orange, Purple, Yellow, Cyan
- Hand off scans to White; prompts to Pink; monitoring to Silver

If no task argument, summarize hub state and propose next Sweeps.
