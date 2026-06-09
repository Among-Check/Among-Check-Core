# Anthropic Cybersecurity Skills

**Category:** agentic-skills / skill-collections  
**Source:** [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) by [@ottosulin](https://github.com/ottosulin) · MIT License  
**Reference:** https://github.com/mukul975/Anthropic-Cybersecurity-Skills

## Description

734+ structured cybersecurity skills for AI agents. MITRE ATT&CK mapped, agentskills.io standard. Compatible with Claude Code, Copilot, Codex CLI, Cursor, Gemini CLI.

## When to invoke

Invoke this skill when:
- Working on AI/LLM security assessments in the `agentic-skills` domain
- Looking for tooling or guidance related to `skill-collections`
- Among-Check agents need to understand the AI-security threat landscape

## Relevant Among-Check agents

Commander (`orchestrator`), Pink (`agent-fix`)

## Usage notes

- All tool execution must happen inside the Docker sandbox (`docs/sandbox.md`)
- Reference only when invoked from an editor session
- Check reference URL for latest version and documentation

## Safety rules

- Non-destructive probes only on authorized targets
- Never exfiltrate scan results to third parties
- Redact secrets and PII in evidence blocks
