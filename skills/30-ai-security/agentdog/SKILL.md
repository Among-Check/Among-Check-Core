# AgentDoG

**Category:** benchmarks-evals / benchmarks  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://github.com/harishsg993010/AgentDoG

## Description

Risk-aware evaluation and guarding framework for autonomous agents — trajectory-level risk assessment.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `benchmarks-evals` domain
- Looking for tooling or guidance related to `benchmarks`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Commander (`orchestrator`), Red (`agent-vuln`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
