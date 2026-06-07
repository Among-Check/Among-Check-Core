---
description: Invoke an Among-Check swarm agent by codename or skill ID
---

Act as the requested Among-Check agent. Read its skill identity first, then execute the task.

**Agent:** $ARGUMENTS

If no argument, list agents from `skills/registry.toon` and ask which to invoke.

## Steps

1. Resolve agent from [skills/registry.toon](../../skills/registry.toon)
2. Read `skills/<skillId>/SKILL.md` fully — adopt codename and motto
3. Read `audits/latest.toon` if task is security-related
4. Work only within that agent's package scope and scanner IDs
5. Hand off to White (`agent-audit`) after scans; use Pink (`agent-fix`) for prompts

## Roster

Commander, Red, Blue, Green, Orange, Purple, Yellow, Cyan, White, Pink
