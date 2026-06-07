# Hub runtime state

This directory holds **Among-Check swarm runtime** configuration for the Hub workspace. It is separate from `audits/` (security scan output) and `markers/` (task tracker).

| Path | Purpose |
|------|---------|
| `hub.toon` | Hub identity, defaults, sentinel thresholds |
| `sandboxes/<id>/` | Per-repo isolation: anchors, sweeps, gate queue |

## Rules

- One **Sandbox** per target Git repository — never mix codebases
- Scouts work in **Anchors** (git worktrees) under their sandbox
- Commander is the only entry point for assigning **Sweeps**

Not committed by default until runtime CLI exists — add to git when your team adopts the full runtime.

See [docs/swarm-runtime.md](../docs/swarm-runtime.md).
