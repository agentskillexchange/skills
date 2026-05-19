---
name: "Snyk Agent Scan MCP and Skill Security Scanner"
slug: "snyk-agent-scan-mcp-skill-security-scanner"
description: "Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more."
github_stars: 2039
verification: "security_reviewed"
source: "https://github.com/snyk/agent-scan"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2039
---

# Snyk Agent Scan MCP and Skill Security Scanner

Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more.

## Installation

Use the upstream install or setup path that matches your environment:
- uv run pip install -e .
- uv run -m src.agent_scan.cli

Requirements and caveats from upstream:
- <a href="https://pypi.python.org/pypi/snyk-agent-scan"><img src="https://img.shields.io/pypi/v/snyk-agent-scan.svg" alt="snyk-agent-scan"/></a>
- <a href="https://pypi.python.org/pypi/snyk-agent-scan"><img src="https://img.shields.io/pypi/l/snyk-agent-scan.svg" alt="snyk-agent-scan license"/></a>
- <a href="https://pypi.python.org/pypi/snyk-agent-scan"><img src="https://img.shields.io/pypi/pyversions/snyk-agent-scan.svg" alt="snyk-agent-scan python version requirements"/></a>

Basic usage or getting-started notes:
- **Use --dangerously-run-mcp-servers** only in trusted environments where you've verified all MCP server commands
- To get started:
- **Sign up at [Snyk](https://snyk.io)** and get an API token from [https://app.snyk.io/account](https://app.snyk.io/account) (API Token → KEY → click to show).

- Source: https://github.com/snyk/agent-scan
- Extracted from upstream docs: https://raw.githubusercontent.com/snyk/agent-scan/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan-mcp-skill-security-scanner/)
