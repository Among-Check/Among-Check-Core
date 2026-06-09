# HackingBuddyGPT

**Category:** attack-red-teaming / ai-assisted-offensive  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://github.com/ipa-lab/hackingBuddyGPT

## Description

LLM-powered ethical hacking assistant in 50 lines of code or less.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `attack-red-teaming` domain
- Looking for tooling or guidance related to `ai-assisted-offensive`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Red (`agent-vuln`), Commander (`orchestrator`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
