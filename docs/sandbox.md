# Sandbox — Docker Isolation for Scan Agents

**Tagline:** Find imposters among codebase.

Among-Check scan agents execute potentially unsafe tooling (sqlmap, Nikto, Trivy, gitleaks, Playwright, awscli). All such execution **must run inside an ephemeral Docker container** — never directly on the host.

---

## Why sandbox

| Risk without sandbox | Mitigation |
|---|---|
| Probe tools write to host filesystem | Container has read-only host mounts |
| Secrets leak from scan environment | Container env is isolated; real creds never injected |
| Malicious target triggers reverse shell | No inbound ports; egress limited to target + OSV API |
| Playwright loads malicious JS | Headless Chromium confined to container |
| CVE in scan tooling affects host | Container destroyed after scan |

---

## Dockerfile (`docker/scanner.Dockerfile`)

```dockerfile
FROM node:20-slim

# Security tooling
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl python3 python3-pip nmap \
    && pip3 install --no-cache-dir gitleaks-python 2>/dev/null || true \
    && npm install -g @toon-format/toon 2>/dev/null || true \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Playwright (Cyan agent)
RUN npx playwright install --with-deps chromium 2>/dev/null || true

# Drop privileges
RUN useradd -m -u 1001 scanner
USER scanner

WORKDIR /scan

ENTRYPOINT ["node", "/scan/packages/cli/dist/index.js"]
```

Build:
```bash
docker build -f docker/scanner.Dockerfile -t among-check-scanner .
```

---

## Run a scan inside the sandbox

```bash
docker run --rm \
  --network host \
  --read-only \
  --tmpfs /tmp:rw,size=256m \
  --tmpfs /scan/audits:rw,size=128m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -e AMONG_CHECK_AUDIT_COMMIT=false \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --url https://example.com
```

### Flags explained

| Flag | Reason |
|------|--------|
| `--rm` | Container destroyed on exit — no persistent state |
| `--read-only` | Host filesystem immutable inside container |
| `--tmpfs /tmp` | Ephemeral scratch space for tools |
| `--cap-drop ALL` | No Linux capabilities (no raw sockets, no ptrace) |
| `--security-opt no-new-privileges` | Prevent privilege escalation |
| `--network host` | Scan target reachable; no inbound ports |
| `-v audits:rw` | Audit TOON committed from host after scan |

### Repo scan (Orange agent)

```bash
docker run --rm \
  --read-only \
  --tmpfs /tmp:rw,size=512m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v "$(pwd):/repo:ro" \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --repo /repo
```

Repo is mounted **read-only** — gitleaks and secret scanners cannot modify source.

---

## Agent-specific sandbox notes

| Scout | Extra constraints |
|-------|------------------|
| **Red** | `--network host` to probe target URL; no outbound except scan target + OSV API |
| **Blue** | Passive TLS/header checks only; same network policy |
| **Green** | Mount cloud config read-only (`-v config:/repo:ro`); never inject real AWS/GCP creds |
| **Orange** | Repo mounted read-only; `AMONG_CHECK_AUDIT_COMMIT=false` inside container |
| **Purple** | Synthetic `TestActor` creds injected via env — never real production tokens |
| **Yellow** | Benign webhook probe payloads only; no outbound except target URL |
| **Cyan** | Playwright confined to container; `--ipc=host` may be needed for Chromium shared memory |

---

## CI / GitHub Actions

```yaml
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build scanner image
        run: docker build -f docker/scanner.Dockerfile -t among-check-scanner .
      - name: Run scan
        run: |
          docker run --rm \
            --read-only \
            --tmpfs /tmp:rw,size=256m \
            --cap-drop ALL \
            --security-opt no-new-privileges \
            -v "${{ github.workspace }}:/repo:ro" \
            -v "${{ github.workspace }}/audits:/scan/audits:rw" \
            among-check-scanner scan --repo /repo
      - name: Commit audit archive
        run: git add audits/ && git commit -m "chore(security): among-check audit" || true
```

`AMONG_CHECK_AUDIT_COMMIT=false` inside container — the host job commits instead, using its own git identity and token.

---

## Safety rules for external skills

When loading skills from `skills/<skill-name>/SKILL.md` inside a scan session:

1. **Non-destructive payloads only** — no `DROP TABLE`, no `rm -rf`, no reverse-shell payloads
2. **Authorized targets only** — scanner confirms `ScanTarget.url` or `repoPath` is owned/authorized
3. **No real credentials in container** — use `fixtures/actors.example.json` for tenant checks
4. **Redact secrets in evidence** — `supply.*` scanners replace matched values with `***`
5. **Respect `robots.txt`** — crawler and DAST tools check `robots.txt` unless `options.respectRobots: false`
6. **Timeout enforced** — global `AbortSignal` (default 30s) kills hung tools

---

## Related

- [docs/architecture.md](./architecture.md) §12 — Security & ethics constraints
- [AGENTS.md](../AGENTS.md) — Hard rules
- [skills/README.md](../skills/README.md) — Skill index
