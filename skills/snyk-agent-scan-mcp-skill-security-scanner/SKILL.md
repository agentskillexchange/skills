---
name: "Snyk Agent Scan MCP and Skill Security Scanner"
description: "Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more."
verification: security_reviewed
source: "https://github.com/snyk/agent-scan"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2039
---

# Snyk Agent Scan MCP and Skill Security Scanner

Snyk Agent Scan (formerly mcp-scan by Invariant Labs, now maintained by Snyk) is a security scanner purpose-built for the AI agent ecosystem. It auto-discovers agent configurations on a machine and scans MCP servers, agent skills, and harnesses for over 15 distinct security risk categories including prompt injection, tool poisoning, tool shadowing, toxic flows, malware payloads hidden in natural language, credential handling issues, and hardcoded secrets.
How It Works
When invoked, Agent Scan reads well-known configuration paths for supported agents (Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, OpenClaw, Kiro, Codex, and others) to build an inventory of all installed MCP servers and skills. For MCP servers, it inspects tool descriptions, prompt definitions, and resource URIs looking for injection patterns and poisoned tool definitions that could cause an agent to exfiltrate data or execute unintended operations. For agent skills, it scans SKILL.md files and associated scripts for malicious payloads disguised as instructions, credential mishandling, and social engineering vectors.
Running a Scan
The scanner runs as a Python CLI distributed via PyPI. The standard invocation is uvx snyk-agent-scan@latest for a full machine scan, or uvx snyk-agent-scan@latest --skills to also discover and scan agent skills. You can also point it at specific MCP configuration files or skill directories for targeted analysis. Results are displayed in a terminal-friendly format with issue codes, severity ratings, and remediation guidance for each finding.
Detected Threats
The scanner detects MCP-specific threats including E001 (Prompt Injection in tool descriptions), E002 (Tool Shadowing where one tool impersonates another), E003 (Tool Poisoning via manipulated descriptions), and TF001 (Toxic Flows where data moves through untrusted channels). For skills, it detects E004 (Prompt Injection in skill files), E006 (Malware Payloads), W007 (Credential Handling issues), W008 (Hardcoded Secrets), and W011 (Untrusted Content execution). Each finding maps to a documented issue code with a detailed explanation.
Integration and Output
Agent Scan requires a Snyk API token for operation and outputs a structured inventory and findings report. The tool integrates into CI/CD pipelines for continuous monitoring of agent security posture. It publishes a technical report on emerging threats in the agent skill ecosystem, making it a valuable reference for security-conscious agent developers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan-mcp-skill-security-scanner/)
