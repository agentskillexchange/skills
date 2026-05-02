---
title: "Inspect and debug MCP servers visually before connecting them to agents"
description: "Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents."
verification: "listed"
source: "https://github.com/modelcontextprotocol/inspector"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "modelcontextprotocol/inspector"
  github_stars: 9431
  npm_package: "@modelcontextprotocol/inspector"
  npm_weekly_downloads: 635249
---

# Inspect and debug MCP servers visually before connecting them to agents

Use MCP Inspector when the job is to validate or debug an MCP server itself. It opens a local UI and proxy layer that can launch a target server over stdio, SSE, or streamable HTTP, list exposed tools and resources, execute calls, pass arguments and environment variables, and export launch configurations for downstream clients. The boundary is clean and publishable: this is a visual MCP server testing workflow, not a generic protocol listing and not merely a product card for the broader MCP ecosystem.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/)
