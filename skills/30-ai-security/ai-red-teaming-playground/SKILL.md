# AI Red Teaming Playground Labs

**Category:** learning-resources / courses-labs  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://github.com/Azure/AI-Red-Teaming-Playground-Labs

## Description

Infrastructure and labs for running AI red teaming trainings.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `learning-resources` domain
- Looking for tooling or guidance related to `courses-labs`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Commander (`orchestrator`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
