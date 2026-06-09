# OWASP LLM TOP 10

**Category:** learning-resources / reading-guides  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://owasp.org/www-project-top-10-for-large-language-model-applications/

## Description

OWASP's top 10 security and safety risks for large language model applications.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `learning-resources` domain
- Looking for tooling or guidance related to `reading-guides`
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
