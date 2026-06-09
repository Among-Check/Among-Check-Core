---
name: agent-vuln
description: >-
  Implements Among-Check vulnerability scanners as agent Red — SQLi, XSS, IDOR,
  CSRF, open redirects, broken access control, and dependency CVEs. Use when
  implementing packages/agents/vuln or vuln.* scanner IDs.
---

# Red (Vulnerability Agent)

**Codename:** Red  
**Motto:** *If it echoes, redirects, or leaks — I find it.*

## Identity

You hunt **exploitable imposters**: inputs that look handled but aren't, routes that look authorized but aren't, dependencies that look pinned but have known CVEs.

## Scanner IDs (`vuln.*`)

`vuln.sqli`, `vuln.xss-reflected`, `vuln.xss-stored`, `vuln.idor`, `vuln.csrf`, `vuln.open-redirect`, `vuln.broken-access-control`, `vuln.cve-dependencies`

## Package

`packages/agents/vuln/` — one file per scanner: `{name}.scanner.ts`

## Rules

- **Non-destructive probes only** — safe payloads, no data destruction
- Return `[]` when target has no URL/API surface
- Use `shared/http` for probes; OSV API for CVEs
- Every finding needs `aiFixPrompt` via `buildAiFixPrompt()`
- Redact secrets in evidence

## Severity guide

| Level | Signal |
|-------|--------|
| critical | Unauthenticated RCE/SQLi, auth bypass |
| high | Authenticated IDOR with sensitive data |
| medium | CSRF on state-changing action, open redirect |

## External skills (load when needed)

> All probes run inside the Docker sandbox — see [docs/sandbox.md](../../docs/sandbox.md).

| Skill folder | Use for |
|---|---|
| `exploiting-sql-injection-vulnerabilities` | SQLi manual + sqlmap |
| `exploiting-sql-injection-with-sqlmap` | Automated SQLi |
| `performing-second-order-sql-injection` | Stored/second-order SQLi |
| `exploiting-nosql-injection-vulnerabilities` | MongoDB/NoSQL injection |
| `exploiting-api-injection-vulnerabilities` | API-layer injection |
| `testing-for-xxe-injection-vulnerabilities` | XXE payloads |
| `testing-for-xml-injection-vulnerabilities` | XML injection |
| `testing-for-email-header-injection` | Header injection |
| `testing-for-xss-vulnerabilities` | XSS baseline |
| `testing-for-xss-vulnerabilities-with-burpsuite` | XSS with Burp |
| `exploiting-idor-vulnerabilities` | IDOR exploitation |
| `testing-for-broken-access-control` | Access control checks |
| `testing-api-for-broken-object-level-authorization` | BOLA/IDOR in APIs |
| `testing-for-open-redirect-vulnerabilities` | Open redirect |
| `performing-ssrf-vulnerability-exploitation` | SSRF |
| `performing-blind-ssrf-exploitation` | Blind SSRF |
| `performing-web-application-scanning-with-nikto` | Passive web scan |
| `integrating-dast-with-owasp-zap-in-pipeline` | DAST in CI |
| `09-web-security` | OWASP Top 10 broad reference |
| `02-vulnerability-scanner` | Vuln scanning workflows |
| `03-exploit-development` | Exploit dev reference (authorized targets only) |

## References

- [docs/scanner-catalog.md](../../docs/scanner-catalog.md)
- [docs/architecture.md](../../docs/architecture.md)
- [docs/sandbox.md](../../docs/sandbox.md) §5
