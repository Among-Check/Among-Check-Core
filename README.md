# Among-Check Core

**Find imposters among codebase.**

Among-Check is an agent swarm that runs **100+ security checks** across your web application, cloud infrastructure, and CI/CD pipelines — full report in **under 30 seconds**. Every finding ships with an AI-ready fix prompt. All probe execution runs inside an **ephemeral Docker sandbox**.

---

## What it checks

| Area | Examples |
|------|----------|
| **Vulnerability scanning** | SQLi, XSS, IDOR, CSRF, open redirects, broken access control, known CVEs |
| **Configuration & compliance** | Security headers, SSL/TLS, cookies/sessions, GDPR signals |
| **Infrastructure & cloud** | Vercel, Netlify, Cloudflare, Supabase RLS, Firebase security rules |
| **Supply chain & secrets** | Leaked API keys/tokens in repos, insecure GitHub Actions |
| **Tenant isolation** | Dual-actor test verifying data cannot leak across accounts |
| **Webhook security** | Handlers that accept webhooks without signature verification |
| **Browser storage** | JWTs, refresh tokens, secrets in `localStorage`/`sessionStorage` |

---

## Agent swarm

| Codename | Role |
|----------|------|
| **Commander** | Entry point — orchestrates scan + fix swarms |
| **Silver** | Watchdogs — detects and recovers stuck agents |
| **Red** | Vulnerability scanners (SQLi, XSS, IDOR, CSRF, CVEs) |
| **Blue** | Config & compliance (headers, TLS, cookies) |
| **Green** | Infrastructure (cloud, containers, IaC) |
| **Orange** | Supply chain (secrets, GitHub Actions) |
| **Purple** | Tenant isolation |
| **Yellow** | Webhooks, JWT, API auth |
| **Cyan** | Browser storage |
| **White** | TOON audit archive |
| **Pink** | AI-ready fix prompts |

---

## Quick start (Docker sandbox)

```bash
# Build the scanner image
docker build -f docker/scanner.Dockerfile -t among-check-scanner .

# Scan a URL
docker run --rm --read-only --tmpfs /tmp:rw,size=256m \
  --cap-drop ALL --security-opt no-new-privileges \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --url https://example.com

# Scan a repo
docker run --rm --read-only --tmpfs /tmp:rw,size=512m \
  --cap-drop ALL --security-opt no-new-privileges \
  -v "$(pwd):/repo:ro" -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --repo /repo
```

Results are committed to `audits/` in TOON format after every scan.

---

## Skills

769 cybersecurity playbooks in `skills/` — no external dependency:

- **754 skills** from [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ([@mukul975](https://github.com/mukul975), Apache 2.0)
- **46 skills** from [Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) ([@Masriyan](https://github.com/Masriyan), MIT)
- **177 skills** from [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) ([@ottosulin](https://github.com/ottosulin), MIT) — LLM/AI security tools, frameworks, guardrails, red-teaming

Each Among-Check agent's `SKILL.md` lists the relevant external skills for that agent with no redundancy.

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/overview.md](docs/overview.md) | Product capabilities and design |
| [docs/architecture.md](docs/architecture.md) | **Technical architecture** (§1–§19) |
| [docs/swarm-runtime.md](docs/swarm-runtime.md) | Multi-agent orchestration |
| [docs/sandbox.md](docs/sandbox.md) | **Docker isolation spec** |
| [docs/agent-skills.md](docs/agent-skills.md) | Agent skill roster |
| [docs/scanner-catalog.md](docs/scanner-catalog.md) | Scanner IDs and status |
| [docs/audit-archive.md](docs/audit-archive.md) | TOON audit history |
| [skills/README.md](skills/README.md) | Skills index (769 entries) |
| [AGENTS.md](AGENTS.md) | Rules for all coding agents |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide |

---

## Agent tooling

| Tool | Config |
|------|--------|
| **Cursor** | [.cursor/rules/](.cursor/rules/), [skills/](skills/), [.cursor/mcp.json](.cursor/mcp.json) |
| **Claude Code** | [CLAUDE.md](CLAUDE.md), [.claude/commands/](.claude/commands/) |
| **GitHub** | [.github/](.github/) — CI, issue templates, Dependabot |

Multi-agent sessions start with **`/commander`** — reads `markers/index.toon`, `.among-check/hub.toon`, and `audits/latest.toon`.

---

## Status

Documentation, agent skills, and Docker sandbox are ready. Application code starts at **Phase 0** in [docs/architecture.md §10](docs/architecture.md#10-implementation-phases) — pnpm monorepo, core orchestrator, CLI, MCP stub.
