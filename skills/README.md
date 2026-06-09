# Among-Check Agent Skills

**Tagline:** Find imposters among codebase.

989 cybersecurity skills in one place — 12 agent identities + 977 practitioner playbooks. All skills live here in `skills/`; no external dependency at runtime.

---

## Among-Check agent roster

Each Among-Check swarm member has a `SKILL.md` defining its identity, scanner ownership, and relevant external skills.

| Codename | Folder | Category | Role |
|----------|--------|----------|------|
| **Commander** | [orchestrator/](orchestrator/SKILL.md) | Runtime | Primary attach point; dispatches scan + fix swarms |
| **Silver** | [agent-sentinel/](agent-sentinel/SKILL.md) | Runtime | Pulse/Relay/Patrol watchdogs for stale anchors |
| **Red** | [agent-vuln/](agent-vuln/SKILL.md) | `vuln.*` | SQLi, XSS, IDOR, CSRF, access control, CVEs |
| **Blue** | [agent-config/](agent-config/SKILL.md) | `config.*` | Headers, TLS, cookies, privacy/compliance |
| **Green** | [agent-infra/](agent-infra/SKILL.md) | `infra.*` | Vercel, Netlify, Cloudflare, Supabase, Firebase |
| **Orange** | [agent-supply/](agent-supply/SKILL.md) | `supply.*` | Leaked secrets, GitHub Actions, dependencies |
| **Purple** | [agent-tenant/](agent-tenant/SKILL.md) | `specialized` | Cross-tenant isolation with dual test actors |
| **Yellow** | [agent-webhook/](agent-webhook/SKILL.md) | `specialized` | Unsigned/weak webhook handlers, JWT, API auth |
| **Cyan** | [agent-browser/](agent-browser/SKILL.md) | `specialized` | Sensitive data in localStorage/sessionStorage |
| **White** | [agent-audit/](agent-audit/SKILL.md) | Archive | TOON reports, git commits, delta/regression |
| **Pink** | [agent-fix/](agent-fix/SKILL.md) | Output | AI-ready fix prompts per finding |
| **–** | [swarm-runtime/](swarm-runtime/SKILL.md) | Coordination | Hub, Sandboxes, Markers, Sweeps, Gate |

Machine-readable manifest: [registry.toon](registry.toon)

---

## Cybersecurity skill catalog

### Structure

```
skills/
├── 01-15-*/          # Claude-Code-CyberSecurity-Skill (46 topic files, 15 categories)
├── 16-29-*/          # Anthropic Cybersecurity Skills (754 playbooks, 14 categories)
├── 30-ai-security/   # awesome-ai-security (177 tools/frameworks, 8 categories)
└── agent-*/          # Among-Check swarm agents (12 SKILL.md files)
```

Each numbered folder contains individual skill subfolders with `SKILL.md` (playbook), `references/`, and `scripts/`.

---

### 01–15 Claude Code CyberSecurity Skills

**Credit:** [Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) by [@Masriyan](https://github.com/Masriyan) · MIT License

| # | Category | Path |
|---|----------|------|
| 01 | Recon & OSINT | [01-recon-osint/](01-recon-osint/) |
| 02 | Vulnerability Scanner | [02-vulnerability-scanner/](02-vulnerability-scanner/) |
| 03 | Exploit Development | [03-exploit-development/](03-exploit-development/) |
| 04 | Reverse Engineering | [04-reverse-engineering/](04-reverse-engineering/) |
| 05 | Malware Analysis | [05-malware-analysis/](05-malware-analysis/) |
| 06 | Threat Hunting | [06-threat-hunting/](06-threat-hunting/) |
| 07 | Incident Response | [07-incident-response/](07-incident-response/) |
| 08 | Network Security | [08-network-security/](08-network-security/) |
| 09 | Web Security | [09-web-security/](09-web-security/) |
| 10 | Cloud Security | [10-cloud-security/](10-cloud-security/) |
| 11 | CSOC Automation | [11-csoc-automation/](11-csoc-automation/) |
| 12 | Log Analysis | [12-log-analysis/](12-log-analysis/) |
| 13 | Crypto Analysis | [13-crypto-analysis/](13-crypto-analysis/) |
| 14 | Red Team Ops | [14-red-team-ops/](14-red-team-ops/) |
| 15 | Blue Team Defense | [15-blue-team-defense/](15-blue-team-defense/) |

---

### 16–29 Anthropic Cybersecurity Skills

**Credit:** [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) by Mahipal Jangra ([@mukul975](https://github.com/mukul975)) · Apache 2.0 · not affiliated with Anthropic PBC.

| # | Category | Skills | Agent(s) | Path |
|---|----------|--------|----------|------|
| 16 | Web App Security | 100 | Red, Yellow | [16-web-app-security/](16-web-app-security/) |
| 17 | Network Security | 45 | Red, Blue | [17-network-security/](17-network-security/) |
| 18 | Digital Forensics | 45 | White, Red | [18-digital-forensics/](18-digital-forensics/) |
| 19 | Malware Analysis | 68 | Red, White | [19-malware-analysis/](19-malware-analysis/) |
| 20 | Cloud Security | 92 | Green | [20-cloud-security/](20-cloud-security/) |
| 21 | Identity & Access Management | 66 | Purple, Yellow | [21-identity-access-management/](21-identity-access-management/) |
| 22 | Threat Intelligence & OSINT | 96 | Commander, Red | [22-threat-intelligence-osint/](22-threat-intelligence-osint/) |
| 23 | Incident Response & SOC | 81 | White, Commander | [23-incident-response/](23-incident-response/) |
| 24 | Penetration Testing & Red Team | 29 | Red, Commander | [24-penetration-testing-red-team/](24-penetration-testing-red-team/) |
| 25 | Vulnerability Management | 33 | Blue, Orange | [25-vulnerability-management/](25-vulnerability-management/) |
| 26 | ICS / IoT / OT Security | 31 | Green | [26-ics-iot-ot-security/](26-ics-iot-ot-security/) |
| 27 | DevSecOps & Supply Chain | 25 | Orange | [27-devsecops-supply-chain/](27-devsecops-supply-chain/) |
| 28 | Cryptography & PKI | 22 | Blue, Yellow | [28-cryptography-pki/](28-cryptography-pki/) |
| 29 | Zero Trust & Network Access | 21 | Green, Blue | [29-zero-trust-network-access/](29-zero-trust-network-access/) |

---

### 30 awesome-ai-security

**Credit:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License

| Category | Skills | Agent(s) | Path |
|----------|--------|----------|------|
| Learning Resources | 19 | Commander | [30-ai-security/](30-ai-security/) |
| Governance & Risk | 22 | Commander, Blue | [30-ai-security/](30-ai-security/) |
| Attack Techniques & Red Teaming | 39 | Red, Commander | [30-ai-security/](30-ai-security/) |
| Benchmarks & Evaluations | 5 | Commander, Red | [30-ai-security/](30-ai-security/) |
| Defense & Security Controls | 57 | Blue, Green, Commander | [30-ai-security/](30-ai-security/) |
| Agentic AI Security Skills | 10 | Commander, Pink | [30-ai-security/](30-ai-security/) |
| Security-Focused AI Models | 11 | Commander, Red | [30-ai-security/](30-ai-security/) |
| Datasets | 4 | Commander, Red | [30-ai-security/](30-ai-security/) |

Full index: [30-ai-security/README.md](30-ai-security/README.md)

---

## Agent → category quick-ref

Each Among-Check agent's `SKILL.md` contains an `## External skills` section listing the most relevant category folders (deduplicated — no skill appears in more than one agent's table).

| Agent | Primary category folders |
|-------|-------------------------|
| Red | 16, 17, 19, 22, 24 |
| Blue | 17, 25, 28 |
| Green | 20, 26, 29 |
| Orange | 27 |
| Purple | 21 |
| Yellow | 16, 21, 28 |
| Cyan | 16 |
| White | 18, 23 |
| Commander | 22, 23, 24 |

---

## Commander attach

All multi-agent sessions start through Commander. Read [docs/swarm-runtime.md](../docs/swarm-runtime.md) before assigning scouts.

---

## Usage

### Loading a skill in Cursor / Claude Code

```
# Load an agent identity
skills/agent-vuln/SKILL.md

# Load a playbook from a category
skills/16-web-app-security/testing-for-xss-vulnerabilities/SKILL.md

# Browse a category
skills/22-threat-intelligence-osint/
```

### Executing skill scripts

All tool commands from external skills run inside the Docker sandbox — never bare host:

```bash
docker run --rm --read-only --tmpfs /tmp:rw,size=512m \
  --cap-drop ALL --security-opt no-new-privileges \
  among-check-scanner ...
```

See [docs/sandbox.md](../docs/sandbox.md).

### Implementing a scanner

1. Identify owning agent from [registry.toon](registry.toon)
2. Read that agent's `SKILL.md` (check `## External skills` section)
3. Implement per [docs/architecture.md §13](../docs/architecture.md#13-adding-a-new-scanner)
4. Register scanner ID in [docs/scanner-catalog.md](../docs/scanner-catalog.md)

---

## Adding a new Among-Check agent

1. Create `skills/agent-<name>/SKILL.md` with identity + scope
2. Add row to [registry.toon](registry.toon) and this README
3. Update [docs/agent-skills.md](../docs/agent-skills.md)
