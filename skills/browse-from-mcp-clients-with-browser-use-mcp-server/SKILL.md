---
title: "Browse from MCP clients with Browser Use MCP Server"
description: "Expose browser-use web automation through an MCP server so Cursor or another MCP client can operate websites with browser state returned to the agent."
verification: "security_reviewed"
source: "https://github.com/kontext-security/browser-use-mcp-server"
author: "kontext-security"
publisher_type: "organization"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "kontext-security/browser-use-mcp-server"
  github_stars: 827
---

# Browse from MCP clients with Browser Use MCP Server

Expose browser-use web automation through an MCP server so Cursor or another MCP client can operate websites with browser state returned to the agent.

## Prerequisites

Python, uv, Playwright, mcp-proxy, MCP-compatible client such as Cursor

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install uv, install mcp-proxy with `uv tool install mcp-proxy`, install the browser-use-mcp-server package, configure the required environment variables, then add the server command to the MCP client configuration.
```

## Documentation

- https://github.com/kontext-security/browser-use-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browse-from-mcp-clients-with-browser-use-mcp-server/)
