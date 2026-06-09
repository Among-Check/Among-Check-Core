# Among-Check Agent Skills

**Tagline:** Find imposters among codebase.

Each folder is an **individual agent identity** in the Among-Check swarm — a Cursor/Claude skill with a codename, scope, and scanner ownership. Invoke by name when implementing or running that slice of the security surface.

## Roster

| Codename | Skill | Category | Role |
|----------|-------|----------|------|
| **Commander** | [orchestrator](orchestrator/SKILL.md) | Runtime | Primary attach point; dispatches scan + fix swarms |
| **Silver** | [agent-sentinel](agent-sentinel/SKILL.md) | Runtime | Pulse/Relay/Patrol watchdogs for stale anchors |
| **Red** | [agent-vuln](agent-vuln/SKILL.md) | `vuln.*` | Injection, XSS, IDOR, CSRF, access control, CVEs |
| **Blue** | [agent-config](agent-config/SKILL.md) | `config.*` | Headers, TLS, cookies, privacy/compliance signals |
| **Green** | [agent-infra](agent-infra/SKILL.md) | `infra.*` | Vercel, Netlify, Cloudflare, Supabase, Firebase |
| **Orange** | [agent-supply](agent-supply/SKILL.md) | `supply.*` | Leaked secrets, GitHub Actions, dependencies |
| **Purple** | [agent-tenant](agent-tenant/SKILL.md) | `specialized` | Cross-tenant isolation with dual test actors |
| **Yellow** | [agent-webhook](agent-webhook/SKILL.md) | `specialized` | Unsigned or weak webhook handlers |
| **Cyan** | [agent-browser](agent-browser/SKILL.md) | `specialized` | Sensitive data in localStorage/sessionStorage |
| **White** | [agent-audit](agent-audit/SKILL.md) | Archive | TOON reports, git commits, delta/regression |
| **Pink** | [agent-fix](agent-fix/SKILL.md) | Output | AI-ready fix prompts per finding |

| **Runtime** | [swarm-runtime](swarm-runtime/SKILL.md) | Coordination | Hub, Sandboxes, Markers, Sweeps, Gate |

Machine-readable manifest: [registry.toon](registry.toon)

## Cybersecurity skills

Each skill is a folder: `skills/<skill-name>/SKILL.md`

### Anthropic Cybersecurity Skills (754)

Example: `skills/exploiting-sql-injection-vulnerabilities/SKILL.md`

**Credit:** [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) by Mahipal Jangra ([@mukul975](https://github.com/mukul975)) · Apache 2.0 · not affiliated with Anthropic PBC.

### Claude Code CyberSecurity Skills (15)

| Skill | Path |
|-------|------|
| Recon & OSINT | `skills/01-recon-osint/SKILL.md` |
| Vulnerability Scanner | `skills/02-vulnerability-scanner/SKILL.md` |
| Exploit Development | `skills/03-exploit-development/SKILL.md` |
| Reverse Engineering | `skills/04-reverse-engineering/SKILL.md` |
| Malware Analysis | `skills/05-malware-analysis/SKILL.md` |
| Threat Hunting | `skills/06-threat-hunting/SKILL.md` |
| Incident Response | `skills/07-incident-response/SKILL.md` |
| Network Security | `skills/08-network-security/SKILL.md` |
| Web Security | `skills/09-web-security/SKILL.md` |
| Cloud Security | `skills/10-cloud-security/SKILL.md` |
| CSOC Automation | `skills/11-csoc-automation/SKILL.md` |
| Log Analysis | `skills/12-log-analysis/SKILL.md` |
| Crypto Analysis | `skills/13-crypto-analysis/SKILL.md` |
| Red Team Ops | `skills/14-red-team-ops/SKILL.md` |
| Blue Team Defense | `skills/15-blue-team-defense/SKILL.md` |

**Credit:** [Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) by [@Masriyan](https://github.com/Masriyan) · MIT License

## Commander attach

All multi-agent sessions start through Commander. Read [docs/swarm-runtime.md](../docs/swarm-runtime.md) before assigning scouts.

## Usage

### Cursor

All skills live in this `skills/` directory — agents read `skills/<name>/SKILL.md` directly.

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
3. Update [docs/agent-skills.md](../docs/agent-skills.md)
