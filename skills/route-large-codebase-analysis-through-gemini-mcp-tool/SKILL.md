---
name: "Route large codebase analysis through Gemini MCP Tool"
slug: "route-large-codebase-analysis-through-gemini-mcp-tool"
description: "Use Gemini MCP Tool to let MCP-capable coding agents delegate large file and codebase analysis to Gemini or Antigravity CLI without leaving the agent workflow."
github_stars: 2260
verification: "security_reviewed"
source: "https://github.com/jamubc/gemini-mcp-tool"
author: "jamubc"
publisher_type: "community"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "jamubc/gemini-mcp-tool"
  github_stars: 2260
  npm_package: "gemini-mcp-tool"
  npm_weekly_downloads: 11864
---

# Route large codebase analysis through Gemini MCP Tool

Use Gemini MCP Tool to let MCP-capable coding agents delegate large file and codebase analysis to Gemini or Antigravity CLI without leaving the agent workflow.

## Prerequisites

Node.js 16+, MCP-capable host such as Claude Code or Claude Desktop, Gemini CLI or Antigravity CLI with authentication

## Installation

Prerequisites: Node.js 16 or newer and a configured Gemini CLI or Antigravity CLI backend.

For Claude Code, add the MCP server with the upstream one-line setup:

- claude mcp add gemini-cli -- npx -y gemini-mcp-tool

For Claude Desktop or other MCP clients, configure the server command as npx with args -y and gemini-mcp-tool.

Verify in Claude Code with /mcp after restarting or reloading MCP servers.

- Source: https://github.com/jamubc/gemini-mcp-tool
- Extracted from upstream docs: https://raw.githubusercontent.com/jamubc/gemini-mcp-tool/HEAD/README.md

## Documentation

- https://jamubc.github.io/gemini-mcp-tool/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-large-codebase-analysis-through-gemini-mcp-tool/)
