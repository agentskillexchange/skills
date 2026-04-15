---
title: "Snyk Agent Scan"
description: "Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories."
verification: security_reviewed
source: "https://github.com/snyk/agent-scan"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2124
---

# Snyk Agent Scan

Snyk Agent Scan (formerly Invariant Labs MCP-Scan) is a command-line security scanner purpose-built for the AI agent supply chain. It auto-discovers agent configurations for Claude Code, Claude Desktop, Cursor, Windsurf, Gemini CLI, and other MCP-compatible platforms, then runs a comprehensive vulnerability assessment against every discovered component.

Best for

Auditing installed MCP servers and agent skills before trusting them
Detecting prompt injection attacks hidden in tool descriptions
Identifying tool shadowing between MCP servers
Verifying skills don’t contain malware payloads or unsafe credential handling

What it scans

MCP servers: Prompt injection in tool descriptions, tool shadowing, tool poisoning via hidden instructions, and toxic data flows
Agent skills: Prompt injection in skill files, malware payloads, untrusted content references, unsafe credential handling, and hardcoded secrets
Agent harnesses: Configuration discovery and inventory across all supported platforms

Install notes
Get an API token from app.snyk.io/account. Set SNYK_TOKEN, install uv, then run uvx snyk-agent-scan@latest for a full machine scan. For targeted scans: uvx snyk-agent-scan@latest ~/.cursor/mcp.json.

Source: github.com/snyk/agent-scan

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snyk-agent-scan
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snyk-agent-scan` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan/)
