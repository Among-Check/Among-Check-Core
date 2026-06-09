# Agent Skills Registry

Among-Check uses **named agent identities** — each with a codename, skill file, and scanner scope. All skills live in [skills/](../skills/) — including 754 Anthropic cybersecurity playbooks and 15 Claude Code CyberSecurity skills.

**Tagline:** Find imposters among codebase.

---

## Swarm model

```mermaid
flowchart TB
  CMD[Commander — attach]
  CMD --> RT[Swarm runtime — Markers Sweeps Gate]
  CMD --> Red[Red — vuln]
  CMD --> Blue[Blue — config]
  CMD --> Green[Green — infra]
  CMD --> Orange[Orange — supply]
  CMD --> Purple[Purple — tenant]
  CMD --> Yellow[Yellow — webhook]
  CMD --> Cyan[Cyan — browser]
  Silver[Silver — sentinels] --> CMD
  Red & Blue & Green & Orange & Purple & Yellow & Cyan --> White[White — audit TOON]
  White --> Pink[Pink — fix prompts]
  White --> RT
```

| Agent | Hunts imposters like… |
|-------|------------------------|
| **Red** | Routes that look safe but accept injection |
| **Blue** | Headers/cookies that claim protection but don't |
| **Green** | Cloud configs that look locked down but are wide open |
| **Orange** | Clean repos hiding keys in history or CI |
| **Purple** | "My data only" APIs that leak across tenants |
| **Yellow** | Webhooks that pretend to verify signatures |
| **Cyan** | Sessions stored where any XSS can read them |

---

## Skill locations

| Path | Purpose |
|------|---------|
| `skills/<agent>/SKILL.md` | Among-Check swarm agent identity |
| `skills/<skill-name>/SKILL.md` | Cybersecurity playbook (769 total) |
| `skills/01-recon-osint/` … `skills/15-blue-team-defense/` | Masriyan Claude Code CyberSecurity skills |
| `skills/registry.toon` | Machine-readable swarm roster |

---

## When to invoke which agent

| Task | Invoke |
|------|--------|
| Commander attach / fix-swarm coordination | `orchestrator` + `swarm-runtime` |
| Sandbox, anchor, marker, sweep, gate CLI | `swarm-runtime` |
| Stuck-agent recovery / sentinels | `agent-sentinel` |
| Scaffold orchestrator / registry | `orchestrator` |
| SQLi, XSS, IDOR, CSRF scanners | `agent-vuln` |
| Headers, TLS, cookies, GDPR signals | `agent-config` |
| Supabase RLS, Firebase, Vercel, etc. | `agent-infra` |
| Secrets in git, GitHub Actions | `agent-supply` |
| Tenant isolation checks | `agent-tenant` |
| Webhook signature verification | `agent-webhook` |
| localStorage / sessionStorage audit | `agent-browser` |
| TOON archive + git commit | `agent-audit` |
| AI-ready fix prompt quality | `agent-fix` |

---

## Related

- [skills/README.md](../skills/README.md) — full roster
- [architecture.md](./architecture.md) — technical interfaces
- [scanner-catalog.md](./scanner-catalog.md) — scanner IDs per agent
