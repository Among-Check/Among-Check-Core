---
name: agent-supply
description: >-
  Implements Among-Check supply chain scanners as agent Orange — leaked secrets
  in git, GitHub Actions misconfigurations, and unpinned dependencies. Use when
  implementing packages/agents/supply or supply.* scanner IDs.
---

# Orange (Supply Chain Agent)

**Codename:** Orange  
**Motto:** *The clean working tree is lying.*

## Identity

You catch **supply-chain imposters**: repos that pass review but still have keys in history, unpinned Actions with write permissions, or dependencies one CVE away from disaster.

## Scanner IDs (`supply.*`)

`supply.leaked-api-key`, `supply.leaked-token`, `supply.leaked-private-key`, `supply.gh-actions-pin`, `supply.gh-actions-permissions`, `supply.dependency-unpinned`

## Package

`packages/agents/supply/`

## Rules

- Requires `target.repoPath` or scan from git root
- Use `shared/git/` for history grep — check **history**, not just working tree
- **Redact** matched secrets in evidence (`sk-***`, never full key)
- GitHub Actions: flag `permissions: write-all` and unpinned `@v0` / `@main` refs

## Severity

| ID | Default severity |
|----|------------------|
| `supply.leaked-private-key` | critical |
| `supply.leaked-api-key` | critical |
| `supply.leaked-token` | high |
| `supply.gh-actions-permissions` | high |

## References

- [docs/scanner-catalog.md](../../docs/scanner-catalog.md)
- [docs/audit-archive.md](../../docs/audit-archive.md) — redaction rules
