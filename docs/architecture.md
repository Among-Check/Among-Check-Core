# Among-Check Core — Technical Architecture

**Audience:** Human engineers and **coding agents** implementing Among-Check Core.

**Tagline:** Find imposters among codebase.

This document is the source of truth for **how to build** the system. Product intent lives in [overview.md](./overview.md). When generating code, follow this layout, interfaces, and phase order unless a human explicitly overrides them.

---

## 1. System context

Among-Check Core is a **security scanner orchestration platform**. It does not implement every check in one binary; it runs an **agent swarm** of small, focused scanners behind a shared runtime.

```mermaid
flowchart TB
  subgraph surfaces [Entry surfaces]
    CLI[CLI]
    API[HTTP API]
    MCP[MCP server]
  end

  subgraph runtime [Core runtime]
    ORCH[Orchestrator]
    REG[Scanner registry]
    CTX[Scan context]
    AGG[Finding aggregator]
    PROMPT[Fix prompt generator]
  end

  subgraph agents [Scanner agents]
    S1[Agent modules]
    S2[...]
    Sn[Agent N]
  end

  subgraph outputs [Outputs]
    JSON[JSON report]
    TOON[TOON audit archive]
    GIT[Git commit]
    MD[Markdown summary]
    CI[CI exit codes]
  end

  CLI --> ORCH
  API --> ORCH
  MCP --> ORCH
  ORCH --> REG
  ORCH --> CTX
  REG --> S1
  REG --> S2
  REG --> Sn
  S1 --> AGG
  S2 --> AGG
  Sn --> AGG
  AGG --> PROMPT
  PROMPT --> JSON
  PROMPT --> TOON
  TOON --> GIT
  PROMPT --> MD
  PROMPT --> CI
```

### Non-goals (v1)

- Full DAST replacement or authenticated crawl of large SPAs
- Legal compliance certification (heuristics only)
- Storing customer scan data server-side (local/CI execution first)

---

## 2. Repository layout

Use a **pnpm monorepo** with TypeScript. Agents must not invent alternate top-level layouts.

```
among-check-core/
├── packages/
│   ├── core/                 # Types, orchestrator, registry, report model
│   ├── cli/                  # `among-check` binary
│   ├── mcp/                  # MCP server (stdio + optional HTTP)
│   ├── agents/               # All scanner implementations
│   │   ├── vuln/             # SQLi, XSS, IDOR, CSRF, ...
│   │   ├── config/           # Headers, TLS, cookies, compliance
│   │   ├── infra/            # Vercel, Netlify, Cloudflare, Supabase, Firebase
│   │   ├── supply/           # Secrets, GitHub Actions, dependencies
│   │   └── specialized/      # Tenant isolation, webhooks, browser storage
│   └── shared/               # HTTP, git, parsers, test actors, logging
├── audits/                   # TOON audit archive (committed; see §14)
│   ├── latest.toon
│   ├── index.toon
│   └── history/
├── markers/                  # Git-backed task tracker (see §16)
│   ├── index.toon
│   ├── open/
│   └── closed/
├── .among-check/             # Hub runtime state — sandboxes, anchors, gate (see §16)
│   ├── hub.toon
│   └── sandboxes/
├── skills/                   # Agent identity repo (SKILL.md per swarm member)
│   ├── registry.toon
│   ├── orchestrator/
│   ├── agent-vuln/
│   └── ...
├── docs/
│   ├── overview.md
│   ├── architecture.md       # this file
│   ├── agent-skills.md       # skill invoke guide
│   ├── audit-archive.md      # TOON schemas & agent workflow
│   └── scanner-catalog.md
├── .cursor/
│   └── rules/                # Cursor agent rules (skills live in skills/)
├── .claude/
├── .github/
├── AGENTS.md
├── CLAUDE.md
├── package.json
├── pnpm-workspace.yaml
└── tsconfig.base.json
```

### Package dependency rules

| Package | May depend on |
|---------|----------------|
| `core` | `shared` only |
| `agents/*` | `core`, `shared` |
| `cli`, `mcp` | `core`, `agents` (barrel import), `shared` |
| `shared` | External libs only |

**Never** import `cli` or `mcp` from `core` or `agents`.

---

## 3. Core domain model

All agents emit the same `Finding` shape. The orchestrator normalizes and deduplicates.

### 3.1 Types (`packages/core/src/types.ts`)

```typescript
export type Severity = 'critical' | 'high' | 'medium' | 'low' | 'info';

export type FindingCategory =
  | 'vulnerability'
  | 'configuration'
  | 'infrastructure'
  | 'supply-chain'
  | 'specialized';

export interface ScanTarget {
  url?: string;
  repoPath?: string;
  cloud?: CloudTarget;
}

export interface CloudTarget {
  provider: 'vercel' | 'netlify' | 'cloudflare' | 'supabase' | 'firebase';
  projectId?: string;
  configPath?: string;
}

export interface AuditArchiveOptions {
  enabled?: boolean;           // default true
  commit?: boolean;            // git commit after write; default true
  rootDir?: string;            // default: git root of target repo
  directory?: string;          // default: 'audits'
  writeDelta?: boolean;        // default true — delta.toon vs previous latest
}

export interface ScanOptions {
  timeoutMs?: number;          // default 30_000
  parallel?: number;           // default 16
  categories?: FindingCategory[];
  scannerIds?: string[];       // allowlist; default = all registered
  auth?: TestActor[];          // for tenant-isolation and authenticated checks
  outputFormat?: 'json' | 'markdown' | 'toon';
  archive?: AuditArchiveOptions;
}

export interface TestActor {
  id: string;
  label: string;
  headers?: Record<string, string>;
  cookies?: Record<string, string>;
  bearerToken?: string;
}

export interface Evidence {
  summary: string;
  request?: string;
  response?: string;
  snippet?: string;
  filePath?: string;
  lineRange?: [number, number];
}

export interface Finding {
  id: string;                  // stable slug, e.g. "headers.missing-hsts"
  scannerId: string;
  title: string;
  severity: Severity;
  category: FindingCategory;
  location: string;
  impact: string;
  remediation: string;
  evidence: Evidence;
  aiFixPrompt: string;
  metadata?: Record<string, unknown>;
}

export interface ScanReport {
  scanId: string;
  startedAt: string;
  finishedAt: string;
  durationMs: number;
  target: ScanTarget;
  findings: Finding[];
  stats: {
    total: number;
    bySeverity: Record<Severity, number>;
    scannersRun: number;
    scannersFailed: number;
  };
}
```

### 3.2 Scanner contract (`packages/core/src/scanner.ts`)

Every check is a **Scanner** — pure async function + metadata.

```typescript
export interface ScannerMeta {
  id: string;                  // unique, kebab-case: "vuln.open-redirect"
  name: string;
  category: FindingCategory;
  description: string;
  tags: string[];
  estimatedMs: number;
  requiresAuth?: boolean;
  requiresRepo?: boolean;
  requiresUrl?: boolean;
}

export interface ScannerContext {
  target: ScanTarget;
  options: ScanOptions;
  signal: AbortSignal;
  logger: Logger;
  http: HttpClient;            // from shared
  fs: FileSystemAdapter;
  git?: GitAdapter;
}

export interface Scanner {
  meta: ScannerMeta;
  run(ctx: ScannerContext): Promise<Finding[]>;
}
```

**Rules for scanner implementations:**

1. Return `[]` when not applicable (wrong target type), never throw for "skip".
2. Throw only on unexpected internal errors; orchestrator catches and records `scannersFailed`.
3. `id` must match `scanner-catalog.md` entry when catalog lists it.
4. `aiFixPrompt` is required on every finding — use `buildAiFixPrompt()` from `core`.
5. Keep each scanner **single-purpose**; compose at orchestrator level, not inside one mega-scanner.

### 3.3 Registry (`packages/core/src/registry.ts`)

```typescript
export interface ScannerRegistry {
  register(scanner: Scanner): void;
  list(filter?: { categories?: FindingCategory[]; ids?: string[] }): Scanner[];
  get(id: string): Scanner | undefined;
}
```

Registration happens in `packages/agents/src/index.ts` (barrel). Each subpackage exports its scanners; barrel imports and registers all.

### 3.4 Orchestrator (`packages/core/src/orchestrator.ts`)

Responsibilities:

1. Validate `ScanTarget` and `ScanOptions`
2. Resolve scanner list from registry
3. Run scanners with **bounded concurrency** (`p-limit` or equivalent)
4. Enforce **global timeout** (`options.timeoutMs`, default 30s)
5. Merge findings, **dedupe** by `(id, location)` hash
6. Sort by severity then `id`
7. Build `ScanReport`

```typescript
export async function runScan(
  target: ScanTarget,
  options: ScanOptions,
  registry: ScannerRegistry
): Promise<ScanReport>;
```

---

## 4. Agent swarm execution model

| Concern | Approach |
|---------|----------|
| Parallelism | Pool size `options.parallel` (default 16); independent scanners only |
| Timeout | `AbortSignal` linked to global deadline; partial report on timeout |
| Auth actors | `TestActor[]` injected into context for tenant-isolation agent |
| Rate limiting | `shared/http` per-host throttle to avoid self-DoS |
| Failure isolation | One scanner failure does not abort the scan |

### Severity rubric (agents must follow)

| Severity | When |
|----------|------|
| `critical` | Exploitable without auth, secret exposure, RLS wide open |
| `high` | Exploitable with low friction, missing webhook verification |
| `medium` | Defense-in-depth gaps, misconfig with partial mitigation |
| `low` | Best-practice deviations |
| `info` | Informational fingerprinting |

---

## 5. Notable scanner designs

### 5.1 Tenant isolation (`agents/specialized/tenant-isolation`)

Requires **≥ 2** `TestActor` entries in `ScanOptions.auth`.

Algorithm:

1. Discover resource IDs accessible as Actor A (URLs from sitemap, API enumeration, or config).
2. Replay requests as Actor B using same resource IDs.
3. Flag any `200` with cross-tenant data or mutation success.

Finding `id`: `specialized.tenant-isolation-leak`

### 5.2 Webhook security (`agents/specialized/webhook-signature`)

1. Static: find route handlers matching webhook patterns (`/webhook`, `/hooks/`, provider names).
2. Dynamic (if URL): probe with unsigned POST; flag `2xx` without challenge.

Finding `id`: `specialized.webhook-no-signature`

### 5.3 Browser storage (`agents/specialized/browser-storage`)

1. If URL: load page in headless browser (Playwright).
2. Inspect `localStorage` / `sessionStorage` keys and values for JWT-shaped strings, `api_key`, etc.

Finding `id`: `specialized.sensitive-browser-storage`

---

## 6. Entry surfaces

### 6.1 CLI (`packages/cli`)

```
among-check scan --url https://example.com
among-check scan --repo .
among-check scan --url https://app.example.com --auth actors.json
among-check scan --repo . --category supply-chain
among-check scan --repo . --format toon          # stdout TOON
among-check scan --repo . --no-audit-commit      # write audits/ without git commit
among-check audit log                            # print index.toon / latest summary
among-check list-scanners
among-check mcp   # optional: start MCP stdio from CLI shim
```

Exit codes: `0` = no critical/high; `1` = findings ≥ high; `2` = runtime error.

Every scan **writes** `audits/` in the target repo by default (see §14).

### 6.2 MCP server (`packages/mcp`)

Tools to expose:

| Tool | Purpose |
|------|---------|
| `among_check_scan` | Run scan from editor; archives TOON + commits by default |
| `among_check_list_scanners` | Introspect registry |
| `among_check_explain_finding` | Expand one finding + fix prompt |
| `among_check_read_audit` | Return `latest.toon`, `delta.toon`, and `index.toon` for agent context |

Transport: **stdio** default; document HTTP in README when added.

### 6.3 HTTP API (phase 3, optional)

`POST /v1/scan` with JSON body matching `ScanTarget` + `ScanOptions`. Same `runScan()` path.

---

## 7. AI-ready fix prompts

`packages/core/src/fix-prompt.ts`:

```typescript
export function buildAiFixPrompt(finding: Omit<Finding, 'aiFixPrompt'>): string;
```

Template sections (in order):

1. **Role** — "You are fixing a security issue in Among-Check."
2. **Finding** — title, severity, location
3. **Evidence** — trimmed snippet
4. **Impact** — one paragraph
5. **Required fix** — remediation steps
6. **Constraints** — minimal diff, preserve behavior, add tests if package has tests

Agents generating findings **must** use this helper — no hand-rolled one-off prompts.

---

## 8. Shared utilities (`packages/shared`)

| Module | Responsibility |
|--------|----------------|
| `http/` | Fetch wrapper, redirect follower, header capture |
| `git/` | Shallow log, grep secrets patterns |
| `parse/` | package.json, workflow YAML, Supabase/Firebase rules |
| `browser/` | Playwright lifecycle for storage/XSS checks |
| `logger/` | Structured JSON logs, scanner-scoped child loggers |
| `toon/` | `encodeReport`, `decodeReport`, strict validation via `@toon-format/toon` |
| `git/` (extended) | `commitAuditArchive()` — stage `audits/` and commit with conventional message |

---

## 9. Testing strategy

| Layer | Location | Expectation |
|-------|----------|-------------|
| Unit | `*.test.ts` next to scanner | Mock `ScannerContext`, assert `Finding[]` |
| Contract | `packages/core` | Registry, dedupe, timeout, severity sort |
| Integration | `packages/agents` | VCR/fixtures against sample apps in `fixtures/` |
| E2E | `packages/cli` | Golden JSON report for `fixtures/vulnerable-app` |

**Fixture apps** live in `fixtures/` (not published):

- `fixtures/vulnerable-app/` — intentional vulns for regression
- `fixtures/clean-app/` — expect zero critical/high

---

## 10. Implementation phases (agents: follow in order)

### Phase 0 — Scaffold

- [ ] pnpm workspace, `tsconfig.base.json`, ESLint, Vitest
- [ ] `core` types + registry + orchestrator (stub scanners)
- [ ] `cli` with `scan`, `list-scanners`, and `audit log`
- [ ] Empty `agents` barrel
- [ ] `core` audit archiver stub + TOON encode/decode round-trip tests
- [ ] `audits/` layout + placeholder `latest.toon` / `index.toon`

### Phase 1 — Config & supply (fast wins)

- [ ] Headers scanner (CSP, HSTS, X-Frame-Options, Referrer-Policy)
- [ ] TLS/SSL basic checker
- [ ] Cookie flags analyzer
- [ ] Git secrets patterns (API keys, tokens)
- [ ] GitHub Actions permission analyzer

### Phase 2 — Vulnerability baselines

- [ ] Open redirect, IDOR probes, CSRF heuristics
- [ ] Reflected XSS probes (safe, non-destructive payloads)
- [ ] Dependency CVE lookup (OSV API)

### Phase 3 — Infrastructure

- [ ] Supabase RLS policy parser
- [ ] Firebase rules parser
- [ ] Vercel/Netlify/Cloudflare config auditors

### Phase 4 — Specialized + MCP

- [ ] Tenant isolation, webhook, browser storage
- [ ] MCP server tools (include `among_check_read_audit`)
- [ ] Markdown report formatter
- [ ] Audit archiver: delta computation + git auto-commit

---

## 11. Naming conventions

| Artifact | Pattern | Example |
|----------|---------|---------|
| Scanner id | `{category}.{kebab-name}` | `config.missing-hsts` |
| File | `{kebab-name}.scanner.ts` | `missing-hsts.scanner.ts` |
| Test | `{kebab-name}.scanner.test.ts` | |
| Finding id | same as scanner id or `scannerId.variant` | `supply.leaked-aws-key` |

---

## 12. Security & ethics constraints for codegen

Coding agents **must**:

- Use **non-destructive** probe payloads only
- Respect `robots.txt` for crawls (configurable override for owned targets)
- Never exfiltrate scan targets to third parties except OSV/CVE APIs
- Redact secrets in evidence blocks (replace with `***`)
- Not commit real credentials to fixtures

---

## 13. Extension: adding a new scanner

1. Add entry to `docs/scanner-catalog.md`
2. Implement `Scanner` in correct `agents/{category}/` folder
3. Register in `agents/src/index.ts`
4. Add unit test + fixture if applicable
5. Update MCP tool schema descriptions if user-facing

---

## 14. Audit archive (TOON version control)

Every scan run is **persisted to git** so coding agents retain security context across sessions. Full spec: [audit-archive.md](./audit-archive.md).

### 14.1 Pipeline (`packages/core/src/audit-archive.ts`)

Runs **after** `runScan()` succeeds (partial reports allowed on timeout — still archive with `metadata.partial: true`).

```typescript
export interface AuditArchiveResult {
  directory: string;           // absolute path to audits/
  files: string[];             // written paths
  committed: boolean;
  commitSha?: string;
  delta?: AuditDelta;
}

export interface AuditDelta {
  previousScanId?: string;
  currentScanId: string;
  newFindings: Pick<Finding, 'id' | 'severity' | 'location'>[];
  resolvedFindings: Pick<Finding, 'id' | 'location'>[];
  unchangedCount: number;
}

export async function archiveScanReport(
  report: ScanReport,
  options: AuditArchiveOptions,
  deps: { toon: ToonCodec; git: GitAdapter; fs: FileSystemAdapter }
): Promise<AuditArchiveResult>;
```

**Steps:**

1. Resolve git root from `target.repoPath` or `process.cwd()`
2. Redact secrets in report (see [audit-archive.md](./audit-archive.md))
3. Encode full report → `history/<iso>/report.toon`
4. Emit tabular `findings.toon` (uniform array — optimal TOON shape)
5. Load previous `latest.toon`, compute `delta.toon`, write to history
6. Overwrite `latest.toon` and prepend run to `index.toon`
7. If `commit: true` and inside git repo: `git add audits/` + commit:

   `chore(security): among-check audit <iso> (<n> findings)`

**Never** commit if `commit: false`, not a git repo, or `CI` env with `AMONG_CHECK_AUDIT_COMMIT=false`.

### 14.2 TOON codec (`packages/shared/toon/`)

- Dependency: `@toon-format/toon`
- `encodeReport(report: ScanReport): string` — canonical field order for stable diffs
- `decodeReport(toon: string): ScanReport` — `strict: true`
- `encodeFindingsTable(findings: Finding[]): string` — tabular subset for agents
- `encodeDelta(delta: AuditDelta): string`

Agents reading TOON should prefer `findings.toon` and `delta.toon` over full `report.toon` unless they need `aiFixPrompt` text.

### 14.3 Orchestrator integration

```typescript
const report = await runScan(target, options, registry);
if (options.archive?.enabled !== false) {
  await archiveScanReport(report, options.archive ?? {}, deps);
}
return report;
```

CLI, MCP, and CI **all** call this path — no duplicate archive logic in entry surfaces.

### 14.4 Agent contract

Coding agents working in a repo scanned by Among-Check **must**:

1. Read `audits/latest.toon` at session start when touching security-sensitive code
2. After fixes, expect a new audit commit; verify `resolved[]` in latest `delta.toon`
3. Treat `new[]` in `delta.toon` as regressions to fix before merge

Documented in [AGENTS.md](../AGENTS.md) and [.cursor/rules/project-core.mdc](../.cursor/rules/project-core.mdc).

---

## 15. Agent skills repository

Each swarm member has an **individual identity** as a Cursor/Claude skill in `skills/<agent>/SKILL.md`. Machine roster: `skills/registry.toon`. Invoke the owning skill before implementing that agent's scanners.

| Codename | Skill ID | Package |
|----------|----------|---------|
| Commander | `orchestrator` | `packages/core` |
| Red | `agent-vuln` | `packages/agents/vuln` |
| Blue | `agent-config` | `packages/agents/config` |
| Green | `agent-infra` | `packages/agents/infra` |
| Orange | `agent-supply` | `packages/agents/supply` |
| Purple / Yellow / Cyan | `agent-tenant`, `agent-webhook`, `agent-browser` | `packages/agents/specialized` |
| White | `agent-audit` | `packages/core` (archive) |
| Pink | `agent-fix` | `packages/core` (fix prompts) |

All skills live in `skills/` — no mirror. See [agent-skills.md](./agent-skills.md).

---

## 16. Swarm runtime (fix-swarm orchestration)

Long-running multi-agent work (remediating findings, implementing scanners) uses a **runtime layer** separate from the 30s scan pipeline. Full spec: [swarm-runtime.md](./swarm-runtime.md).

### 16.1 Types (`packages/core/src/runtime.ts`)

```typescript
export type MarkerStatus = 'open' | 'in_progress' | 'closed' | 'cancelled';
export type AnchorStatus = 'idle' | 'in_progress' | 'stale' | 'closed';
export type GateStatus = 'pending' | 'running' | 'passed' | 'failed' | 'merged';

export interface Marker {
  markerId: string;
  title: string;
  status: MarkerStatus;
  priority: 'critical' | 'high' | 'medium' | 'low';
  assignee: string;           // scout codename: Red, Blue, ...
  source: 'audit' | 'manual' | 'scanner-request';
  sandboxId: string;
  findingId?: string;
  findingLocation?: string;
  acceptance: string[];
  aiFixPrompt?: string;
  createdAt: string;
}

export interface AnchorState {
  anchorId: string;
  agent: string;
  sandboxId: string;
  branch: string;
  worktreePath: string;
  markerIds: string[];
  status: AnchorStatus;
  lastHeartbeat: string;
  checkpoint?: { summary: string; files: string[] };
}

export interface Sweep {
  sweepId: string;
  sandboxId: string;
  assignee: string;
  anchorId: string;
  markerIds: string[];
  status: 'assigned' | 'in_progress' | 'complete' | 'cancelled';
  createdAt: string;
  deadline?: string;
}

export interface GateJob {
  gateId: string;
  sweepId: string;
  anchorId: string;
  branch: string;
  status: GateStatus;
  checks: { name: string; status: 'pending' | 'passed' | 'failed' }[];
}
```

### 16.2 CLI commands (Phase R2)

```
among-check commander status
among-check sandbox create|list|use
among-check anchor create|resume|list
among-check marker create|list|close|sync-audit
among-check sweep create|assign|status
among-check gate enqueue|status|approve
among-check sentinel status|patrol
```

### 16.3 Runtime pipeline

1. **Commander attach** — read `hub.toon`, `markers/index.toon`, `audits/latest.toon`
2. **marker sync-audit** — open Markers for each `delta.new` finding without a Marker
3. **sweep assign** — bundle markers → scout; create/resume Anchor worktree
4. Scout works in Anchor; writes heartbeat to `state.toon`
5. **gate enqueue** — run tests + `runScan()` + verify acceptance → merge to default branch
6. **Silver sentinel** — Pulse/Relay/Patrol on stale anchors (background)

### 16.4 Git adapter extensions (`packages/shared/git/`)

- `createWorktree(repoPath, branch, path)`
- `removeWorktree(path)`
- `listWorktrees(repoPath)`

### 16.5 Best practices (enforced in AGENTS.md)

| Practice | Implementation |
|----------|----------------|
| Delegate to Commander | `/commander` slash command; `swarm-runtime` skill |
| One repo per Sandbox | `sandbox create --repo` isolation |
| Git-backed tasks | `markers/` TOON files committed |
| Persistent scout state | Anchor worktrees + `state.toon` |
| Verify before merge | Gate queue (test + re-scan) |
| Stuck agent recovery | Silver sentinels (Pulse, Relay, Patrol) |
| Parallel stability | tmux recommended in `hub.toon` |

---

## Related documents

- [overview.md](./overview.md) — product capabilities
- [swarm-runtime.md](./swarm-runtime.md) — fix-swarm orchestration
- [agent-skills.md](./agent-skills.md) — agent identity roster
- [audit-archive.md](./audit-archive.md) — TOON schemas, CI, redaction
- [scanner-catalog.md](./scanner-catalog.md) — full check list
- [skills/README.md](../skills/README.md) — canonical skill files
- [AGENTS.md](../AGENTS.md) — agent workflow rules
- [CONTRIBUTING.md](../CONTRIBUTING.md) — human + agent contribution
