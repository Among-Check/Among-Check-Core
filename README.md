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

## Notable scanners

- **Tenant isolation** — Two authenticated test actors verify data cannot leak across accounts.
- **Webhook security** — Flags handlers that accept webhooks without signature verification.
- **Browser storage** — Audits JWTs, refresh tokens, and other sensitive data in `localStorage` / `sessionStorage`.

---

## Documentation

Full product and architecture details: **[docs/overview.md](docs/overview.md)**

---

## Status

Among-Check Core is under active development. The agent swarm and scanner catalog are being implemented; documentation describes the intended system design and capabilities.
