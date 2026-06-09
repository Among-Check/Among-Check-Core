# MIT AI Risk Repository

**Category:** governance-risk / taxonomies  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://airisk.mit.edu/

## Description

MIT's comprehensive repository of AI risks.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `governance-risk` domain
- Looking for tooling or guidance related to `taxonomies`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Commander (`orchestrator`), Blue (`agent-config`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
