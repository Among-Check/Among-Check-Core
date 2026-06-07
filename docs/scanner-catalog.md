# Scanner Catalog

Stable IDs for all planned checks. Implementations must use these `id` values. Status: **planned** until marked **shipped** in code.

---

## Vulnerability (`vuln.*`)

| ID | Name | Status |
|----|------|--------|
| `vuln.sqli` | SQL injection heuristics | planned |
| `vuln.xss-reflected` | Reflected XSS probes | planned |
| `vuln.xss-stored` | Stored XSS indicators | planned |
| `vuln.idor` | Insecure direct object reference | planned |
| `vuln.csrf` | Missing CSRF protection | planned |
| `vuln.open-redirect` | Open redirect | planned |
| `vuln.broken-access-control` | Missing authorization on routes | planned |
| `vuln.cve-dependencies` | Known CVEs in dependencies (OSV) | planned |

---

## Configuration (`config.*`)

| ID | Name | Status |
|----|------|--------|
| `config.missing-csp` | Content-Security-Policy | planned |
| `config.missing-hsts` | Strict-Transport-Security | planned |
| `config.missing-x-frame-options` | X-Frame-Options / frame-ancestors | planned |
| `config.missing-referrer-policy` | Referrer-Policy | planned |
| `config.tls-weak` | Weak TLS/cipher configuration | planned |
| `config.mixed-content` | Mixed content | planned |
| `config.cookie-insecure` | Cookie missing Secure | planned |
| `config.cookie-no-httponly` | Cookie missing HttpOnly | planned |
| `config.cookie-samesite` | Cookie SameSite misconfiguration | planned |
| `config.privacy-signals` | Basic GDPR/privacy page heuristics | planned |
| `config.terms-signals` | Terms of Service presence | planned |

---

## Infrastructure (`infra.*`)

| ID | Name | Status |
|----|------|--------|
| `infra.vercel-exposure` | Vercel deployment/config exposure | planned |
| `infra.netlify-config` | Netlify headers/redirect risks | planned |
| `infra.cloudflare-ssl` | Cloudflare SSL mode misconfig | planned |
| `infra.supabase-rls-disabled` | Supabase table without RLS | planned |
| `infra.supabase-rls-permissive` | Supabase policy allows all | planned |
| `infra.firebase-rules-open` | Firebase rules too permissive | planned |

---

## Supply chain (`supply.*`)

| ID | Name | Status |
|----|------|--------|
| `supply.leaked-api-key` | API key in repo | planned |
| `supply.leaked-token` | Token/secret in repo | planned |
| `supply.leaked-private-key` | Private key in repo | planned |
| `supply.gh-actions-pin` | Unpinned GitHub Actions | planned |
| `supply.gh-actions-permissions` | Overbroad workflow permissions | planned |
| `supply.dependency-unpinned` | Unpinned critical dependencies | planned |

---

## Specialized (`specialized.*`)

| ID | Name | Status |
|----|------|--------|
| `specialized.tenant-isolation-leak` | Cross-tenant data access | planned |
| `specialized.webhook-no-signature` | Webhook without signature verification | planned |
| `specialized.sensitive-browser-storage` | Secrets in localStorage/sessionStorage | planned |

---

## Catalog maintenance

When adding scanners beyond this list, update this file **before** implementation. Target: **100+** checks via sub-variants (e.g. per-header, per-provider, per-secret-pattern) as the swarm grows.
