# ATTACK-BERT

**Category:** security-ai-models / domain-models  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://huggingface.co/harishsg993010/ATTACK-BERT

## Description

Sentence-transformer model for mapping security text to MITRE ATT&CK techniques.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `security-ai-models` domain
- Looking for tooling or guidance related to `domain-models`
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
