---
title: "Snyk Agent Scan MCP and Skill Security Scanner"
description: "Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more."
slug: "snyk-agent-scan-mcp-skill-security-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/snyk/agent-scan"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2039
---

# Snyk Agent Scan MCP and Skill Security Scanner

Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install snyk-agent-scan-mcp-skill-security-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Snyk Agent Scan (formerly mcp-scan by Invariant Labs, now maintained by Snyk) is a security scanner purpose-built for the AI agent ecosystem. It auto-discovers agent configurations on a machine and scans MCP servers, agent skills, and harnesses for over 15 distinct security risk categories including prompt injection, tool poisoning, tool shadowing, toxic flows, malware payloads hidden in natural language, credential handling issues, and hardcoded secrets.
How It Works
When invoked, Agent Scan reads well-known configuration paths for supported agents (Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, OpenClaw, Kiro, Codex, and others) to build an inventory of all installed MCP servers and skills. For MCP servers, it inspects tool descriptions, prompt definitions, and resource URIs looking for injection patterns and poisoned tool definitions that could cause an agent to exfiltrate data or execute unintended operations. For agent skills, it scans SKILL.md files and associated scripts for malicious payloads disguised as instructions, credential mishandling, and social engineering vectors.
Running a Scan
The scanner runs as a Python CLI distributed via PyPI. The standard invocation is uvx snyk-agent-scan@latest for a full machine scan, or uvx snyk-agent-scan@latest --skills to also discover and scan agent skills. You can also point it at specific MCP configuration files or skill directories for targeted analysis. Results are displayed in a terminal-friendly format with issue codes, severity ratings, and remediation guidance for each finding.
Detected Threats
The scanner detects MCP-specific threats including E001 (Prompt Injection in tool descriptions), E002 (Tool Shadowing where one tool impersonates another), E003 (Tool Poisoning via manipulated descriptions), and TF001 (Toxic Flows where data moves through untrusted channels). For skills, it detects E004 (Prompt Injection in skill files), E006 (Malware Payloads), W007 (Credential Handling issues), W008 (Hardcoded Secrets), and W011 (Untrusted Content execution). Each finding maps to a documented issue code with a detailed explanation.
Integration and Output
Agent Scan requires a Snyk API token for operation and outputs a structured inventory and findings report. The tool integrates into CI/CD pipelines for continuous monitoring of agent security posture. It publishes a technical report on emerging threats in the agent skill ecosystem, making it a valuable reference for security-conscious agent developers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan-mcp-skill-security-scanner/)
