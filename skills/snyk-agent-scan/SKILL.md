---
title: "Snyk Agent Scan"
description: "Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories."
slug: "snyk-agent-scan"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/snyk/agent-scan"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2083
listed: true
---

# Snyk Agent Scan

Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories.

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
clawhub install snyk-agent-scan
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Snyk Agent Scan (formerly Invariant Labs MCP-Scan) is a command-line security scanner purpose-built for the AI agent supply chain. It auto-discovers agent configurations for Claude Code, Claude Desktop, Cursor, Windsurf, Gemini CLI, and other MCP-compatible platforms, then runs a comprehensive vulnerability assessment against every discovered component.
Best for
- Auditing installed MCP servers and agent skills before trusting them
- Detecting prompt injection attacks hidden in tool descriptions
- Identifying tool shadowing between MCP servers
- Verifying skills don’t contain malware payloads or unsafe credential handling
What it scans
- MCP servers: Prompt injection in tool descriptions, tool shadowing, tool poisoning via hidden instructions, and toxic data flows
- Agent skills: Prompt injection in skill files, malware payloads, untrusted content references, unsafe credential handling, and hardcoded secrets
- Agent harnesses: Configuration discovery and inventory across all supported platforms
Install notes
Get an API token from app.snyk.io/account. Set SNYK_TOKEN, install uv, then run uvx snyk-agent-scan@latest for a full machine scan. For targeted scans: uvx snyk-agent-scan@latest ~/.cursor/mcp.json.
Source: github.com/snyk/agent-scan

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan/)
