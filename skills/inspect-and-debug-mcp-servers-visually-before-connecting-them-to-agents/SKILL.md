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
  ase_npm_package: "@modelcontextprotocol/inspector"
  npm_weekly_downloads: 635249
---

# Inspect and debug MCP servers visually before connecting them to agents

Use MCP Inspector when the job is to validate or debug an MCP server itself. It opens a local UI and proxy layer that can launch a target server over stdio, SSE, or streamable HTTP, list exposed tools and resources, execute calls, pass arguments and environment variables, and export launch configurations for downstream clients. The boundary is clean and publishable: this is a visual MCP server testing workflow, not a generic protocol listing and not merely a product card for the broader MCP ecosystem.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/)
