---
description: Invoke an Among-Check swarm agent by codename or skill ID
---

Act as the requested Among-Check agent. For multi-step work, prefer **`/commander`** first unless explicitly invoking a single scout.

**Agent:** $ARGUMENTS

If no argument, list agents from `skills/registry.toon` and ask which to invoke.

## Steps

1. If not Commander: confirm a Sweep/Marker assignment exists in `markers/index.toon`
2. Resolve agent from [skills/registry.toon](../../skills/registry.toon)
3. Read `skills/<skillId>/SKILL.md` fully — adopt codename and motto
4. Read `markers/index.toon` and `audits/latest.toon` if task is security-related
5. Work in assigned **Anchor** worktree when doing fix work
6. Work only within that agent's package scope and scanner IDs
7. Hand off to White (`agent-audit`) after scans; use Pink (`agent-fix`) for prompts
8. Commander enqueues **Gate** when sweep is complete

## Roster

Commander, Silver, Red, Blue, Green, Orange, Purple, Yellow, Cyan, White, Pink
