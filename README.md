# Among-Check Core

**Find imposters among codebase.**

Among-Check is an agent swarm built to run **100+ individual security checks** across your web application, cloud infrastructure, and CI/CD pipelines — and deliver a full report in **under 30 seconds**.

It acts as an automated security engineer: it finds misconfigurations and vulnerabilities, then surfaces **actionable fixes** (including AI-ready fix prompts) so you can ship faster without guessing what to patch.

---

## What it checks

| Area | Examples |
|------|----------|
| **Vulnerability scanning** | SQL injection, XSS, IDOR, CSRF, open redirects, broken access control, known CVEs in your stack |
| **Configuration & compliance** | Security headers, SSL/TLS, cookies/sessions, GDPR and basic legal/privacy signals |
| **Infrastructure & cloud** | Vercel, Netlify, Cloudflare, Supabase RLS, Firebase security rules |
| **Supply chain & secrets** | Leaked API keys/tokens in repos, insecure GitHub Actions and supply-chain config |
| **AI-native workflow** | Every finding ships with an AI-ready fix prompt; MCP server for Cursor, Claude Code, and other editors |
| **TOON audit archive** | Every scan commits security history to `audits/` in TOON for agent context |
| **Swarm runtime** | Commander-led fix swarm: Sandboxes, Anchors, Markers, Sweeps, Gate, Sentinels |

## Notable scanners

- **Tenant isolation** — Two authenticated test actors verify data cannot leak across accounts.
- **Webhook security** — Flags handlers that accept webhooks without signature verification.
- **Browser storage** — Audits JWTs, refresh tokens, and other sensitive data in `localStorage` / `sessionStorage`.

---

## Documentation

| Doc | Description |
|-----|-------------|
| [docs/overview.md](docs/overview.md) | Product capabilities and agent swarm design |
| [docs/architecture.md](docs/architecture.md) | **Technical architecture for agentic codegen** |
| [docs/swarm-runtime.md](docs/swarm-runtime.md) | **Multi-agent orchestration** (Markers, Anchors, Gate) |
| [markers/index.toon](markers/index.toon) | Git-backed task queue for scouts |
| [docs/scanner-catalog.md](docs/scanner-catalog.md) | Scanner IDs and implementation status |
| [docs/audit-archive.md](docs/audit-archive.md) | TOON version-controlled audit history |
| [audits/latest.toon](audits/latest.toon) | Latest security audit (agent-readable) |
| [skills/README.md](skills/README.md) | Agent identities (Commander, Red, Blue, …) |
| [docs/agent-skills.md](docs/agent-skills.md) | Swarm skill registry and invoke guide |
| [AGENTS.md](AGENTS.md) | Rules for all coding agents |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Human and agent contribution guide |

## Agent tooling

Preconfigured for AI-assisted development:

| Tool | Config |
|------|--------|
| **Cursor** | [.cursor/rules/](.cursor/rules/), [skills/](skills/), [.cursor/mcp.json](.cursor/mcp.json) |
| **Claude Code** | [CLAUDE.md](CLAUDE.md), [.claude/](.claude/) |
| **GitHub** | [.github/](.github/) — CI, issue/PR templates, Dependabot |

---

## Status

Documentation and agent scaffolding are ready. Application code starts at **Phase 0** in [docs/architecture.md](docs/architecture.md) (pnpm monorepo, core orchestrator, CLI, MCP stub).

