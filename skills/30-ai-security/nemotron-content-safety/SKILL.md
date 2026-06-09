# Nemotron 3.5 Content Safety

**Category:** security-ai-models / safety-classifiers  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety

## Description

NVIDIA's 4B multimodal content safety model: text+image, 35+ languages, customizable enterprise policy, auditable reasoning.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `security-ai-models` domain
- Looking for tooling or guidance related to `safety-classifiers`
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
