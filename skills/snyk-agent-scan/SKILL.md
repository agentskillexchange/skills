---
name: "Snyk Agent Scan"
slug: "snyk-agent-scan"
description: "Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories."
github_stars: 2508
verification: "security_reviewed"
source: "https://github.com/snyk/agent-scan"
author: "Snyk"
publisher_type: "company"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "snyk/agent-scan"
  github_stars: 2508
---

# Snyk Agent Scan

Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories.

## Prerequisites

Python 3.10+, uv package manager, Snyk API token

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

## Documentation

- https://github.com/snyk/agent-scan/blob/main/docs/scanning.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-agent-scan/)
