# Among-Check Agent Skills

**Tagline:** Find imposters among codebase.

Each folder is an **individual agent identity** in the Among-Check swarm — a Cursor/Claude skill with a codename, scope, and scanner ownership. Invoke by name when implementing or running that slice of the security surface.

## Roster

| Codename | Skill | Category | Role |
|----------|-------|----------|------|
| **Commander** | [orchestrator](orchestrator/SKILL.md) | Runtime | Dispatches swarm, merges findings, archives TOON |
| **Red** | [agent-vuln](agent-vuln/SKILL.md) | `vuln.*` | Injection, XSS, IDOR, CSRF, access control, CVEs |
| **Blue** | [agent-config](agent-config/SKILL.md) | `config.*` | Headers, TLS, cookies, privacy/compliance signals |
| **Green** | [agent-infra](agent-infra/SKILL.md) | `infra.*` | Vercel, Netlify, Cloudflare, Supabase, Firebase |
| **Orange** | [agent-supply](agent-supply/SKILL.md) | `supply.*` | Leaked secrets, GitHub Actions, dependencies |
| **Purple** | [agent-tenant](agent-tenant/SKILL.md) | `specialized` | Cross-tenant isolation with dual test actors |
| **Yellow** | [agent-webhook](agent-webhook/SKILL.md) | `specialized` | Unsigned or weak webhook handlers |
| **Cyan** | [agent-browser](agent-browser/SKILL.md) | `specialized` | Sensitive data in localStorage/sessionStorage |
| **White** | [agent-audit](agent-audit/SKILL.md) | Archive | TOON reports, git commits, delta/regression |
| **Pink** | [agent-fix](agent-fix/SKILL.md) | Output | AI-ready fix prompts per finding |

Machine-readable manifest: [registry.toon](registry.toon)

## Usage

### Cursor

Skills are mirrored under [.cursor/skills/](../.cursor/skills/) for editor discovery. Source of truth is this `skills/` directory.

### Claude Code

Reference skill paths from [AGENTS.md](../AGENTS.md) or invoke slash commands in [.claude/commands/](../.claude/commands/).

### Implementing a scanner

1. Identify owning agent from [registry.toon](registry.toon)
2. Read that agent's `SKILL.md`
3. Implement per [docs/architecture.md](../docs/architecture.md)
4. Register scanner ID in [docs/scanner-catalog.md](../docs/scanner-catalog.md)

## Adding a new agent

1. Create `skills/agent-<name>/SKILL.md` with identity + scope
2. Add row to `registry.toon` and this README
3. Mirror to `.cursor/skills/agent-<name>/SKILL.md`
4. Update [docs/agent-skills.md](../docs/agent-skills.md)
