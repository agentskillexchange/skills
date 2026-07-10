---
name: "Browse from MCP clients with Browser Use MCP Server"
slug: "browse-from-mcp-clients-with-browser-use-mcp-server"
description: "Expose browser-use web automation through an MCP server so Cursor or another MCP client can operate websites with browser state returned to the agent."
github_stars: 827
verification: "security_reviewed"
source: "https://github.com/kontext-security/browser-use-mcp-server"
author: "kontext-security"
publisher_type: "organization"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "kontext-security/browser-use-mcp-server"
  github_stars: 827
---

# Browse from MCP clients with Browser Use MCP Server

Expose browser-use web automation through an MCP server so Cursor or another MCP client can operate websites with browser state returned to the agent.

## Prerequisites

Python, uv, Playwright, mcp-proxy, MCP-compatible client such as Cursor

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install mcp-proxy
- uv tool update-shell
- uv sync
- uv pip install playwright

Requirements and caveats from upstream:
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- Using Docker provides a consistent and isolated environment for running the server.

Basic usage or getting-started notes:
- [Playwright](https://playwright.dev/) - Browser automation
- [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) - Required for stdio mode
- Create a .env file:

- Source: https://github.com/kontext-security/browser-use-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/kontext-security/browser-use-mcp-server/HEAD/README.md

## Documentation

- https://github.com/kontext-security/browser-use-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browse-from-mcp-clients-with-browser-use-mcp-server/)
