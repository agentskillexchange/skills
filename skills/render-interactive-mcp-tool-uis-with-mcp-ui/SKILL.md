---
title: "Render interactive MCP tool UIs with mcp-ui"
description: "Build an MCP Apps resource, attach it to a tool through _meta.ui.resourceUri, and verify the host renders the interactive UI alongside tool results."
verification: "security_reviewed"
source: "https://github.com/MCP-UI-Org/mcp-ui"
author: "MCP-UI-Org"
publisher_type: "open-source organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "MCP-UI-Org/mcp-ui"
  github_stars: 4875
  npm_package: "@mcp-ui/server; @mcp-ui/client"
  npm_weekly_downloads: 1645678
---

# Render interactive MCP tool UIs with mcp-ui

Build an MCP Apps resource, attach it to a tool through _meta.ui.resourceUri, and verify the host renders the interactive UI alongside tool results.

## Prerequisites

MCP server, MCP Apps-compatible host or legacy MCP-UI host, TypeScript packages @mcp-ui/server and @mcp-ui/client; Python and Ruby server SDKs are also available.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For TypeScript, run npm install @mcp-ui/server @mcp-ui/client, or pnpm add @mcp-ui/server @mcp-ui/client. Create a UI resource with createUIResource, register it with the MCP Apps resource handler, then link a tool to the resource using _meta.ui.resourceUri. For Python use pip install mcp-ui-server; for Ruby use gem install mcp_ui_server.
```

## Documentation

- https://github.com/MCP-UI-Org/mcp-ui

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/render-interactive-mcp-tool-uis-with-mcp-ui/)
