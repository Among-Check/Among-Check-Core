# AgentLens

**Category:** defense-controls / agent-runtime-sandbox  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://github.com/harishsg993010/AgentLens

## Description

Agent observability and replay tooling for AI safety and interpretability research. Captures trajectories in ATIF format.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `defense-controls` domain
- Looking for tooling or guidance related to `agent-runtime-sandbox`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Blue (`agent-config`), Green (`agent-infra`), Commander (`orchestrator`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
