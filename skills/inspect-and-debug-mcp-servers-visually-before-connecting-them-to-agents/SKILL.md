---
title: "Inspect and debug MCP servers visually before connecting them to agents"
description: "Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents."
verification: listed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/)
