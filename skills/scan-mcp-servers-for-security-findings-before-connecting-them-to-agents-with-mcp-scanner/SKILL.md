---
name: "Scan MCP servers for security findings before connecting them to agents with MCP Scanner"
slug: "scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner"
description: "Run MCP Scanner against a remote or local MCP server before trusting it, so the agent gets a bounded security review of tools, prompts, resources, dependencies, and supply-chain risk."
github_stars: 889
verification: "security_reviewed"
source: "https://github.com/cisco-ai-defense/mcp-scanner"
author: "Cisco AI Defense"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "cisco-ai-defense/mcp-scanner"
  github_stars: 889
---

# Scan MCP servers for security findings before connecting them to agents with MCP Scanner

Run MCP Scanner against a remote or local MCP server before trusting it, so the agent gets a bounded security review of tools, prompts, resources, dependencies, and supply-chain risk.

## Prerequisites

Python 3.11+, uv, optional Cisco AI Defense API key, optional LLM provider key, optional VirusTotal API key

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with uv: uv tool install --python 3.13 cisco-ai-mcp-scanner
```

## Documentation

- https://blogs.cisco.com/ai/securing-the-ai-agent-supply-chain-with-ciscos-open-source-mcp-scanner

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner/)
