---
title: "Snyk Agent Scan"
description: "Snyk Agent Scan (formerly Invariant Labs MCP-Scan) is a command-line security scanner purpose-built for the AI agent supply chain. It auto-discovers agent configurations for Claude Code, Claude Desktop, Cursor, Windsurf, Gemini CLI, and other MCP-compatible platforms, then runs a comprehensive vulnerability assessment against every discovered component. Best for Auditing installed MCP servers and agent skills before trusting them Detecting prompt injection attacks hidden in tool descriptions Identifying tool shadowing between MCP servers Verifying skills don&#8217;t contain malware payloads or unsafe credential handling What it scans MCP servers: Prompt injection in tool descriptions, tool shadowing, tool poisoning via hidden instructions, and toxic data flows Agent skills: Prompt injection in skill files, malware payloads, untrusted content references, unsafe credential handling, and hardcoded secrets Agent harnesses: Configuration discovery and inventory across all supported platforms Install notes Get an API token from app.snyk.io/account . Set SNYK_TOKEN , install uv , then run uvx snyk-agent-scan@latest for a full machine scan. For targeted scans: uvx snyk-agent-scan@latest ~/.cursor/mcp.json . Source: github.com/snyk/agent-scan"
source: "https://github.com/snyk/agent-scan"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2151
---

# Snyk Agent Scan

Snyk Agent Scan (formerly Invariant Labs MCP-Scan) is a command-line security scanner purpose-built for the AI agent supply chain. It auto-discovers agent configurations for Claude Code, Claude Desktop, Cursor, Windsurf, Gemini CLI, and other MCP-compatible platforms, then runs a comprehensive vulnerability assessment against every discovered component. Best for Auditing installed MCP servers and agent skills before trusting them Detecting prompt injection attacks hidden in tool descriptions Identifying tool shadowing between MCP servers Verifying skills don&#8217;t contain malware payloads or unsafe credential handling What it scans MCP servers: Prompt injection in tool descriptions, tool shadowing, tool poisoning via hidden instructions, and toxic data flows Agent skills: Prompt injection in skill files, malware payloads, untrusted content references, unsafe credential handling, and hardcoded secrets Agent harnesses: Configuration discovery and inventory across all supported platforms Install notes Get an API token from app.snyk.io/account . Set SNYK_TOKEN , install uv , then run uvx snyk-agent-scan@latest for a full machine scan. For targeted scans: uvx snyk-agent-scan@latest ~/.cursor/mcp.json . Source: github.com/snyk/agent-scan

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan/)
