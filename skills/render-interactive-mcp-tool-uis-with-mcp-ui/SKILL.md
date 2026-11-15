---
name: "Render interactive MCP tool UIs with mcp-ui"
slug: "render-interactive-mcp-tool-uis-with-mcp-ui"
description: "Build an MCP Apps resource, attach it to a tool through _meta.ui.resourceUri, and verify the host renders the interactive UI alongside tool results."
github_stars: 4875
verification: "security_reviewed"
source: "https://github.com/MCP-UI-Org/mcp-ui"
author: "MCP-UI-Org"
publisher_type: "open-source organization"
category: "Integrations & Connectors"
framework: "MCP"
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

Use the upstream install or setup path that matches your environment:
- npm install @mcp-ui/server @mcp-ui/client
- pnpm add @mcp-ui/server @mcp-ui/client
- yarn add @mcp-ui/server @mcp-ui/client
- gem install mcp_ui_server

Requirements and caveats from upstream:
- <a href="https://pypi.org/project/mcp-ui-server/"><img src="https://img.shields.io/pypi/v/mcp-ui-server?label=python&color=yellow" alt="Python Server SDK Version"></a>
- **mcp-ui-server (Python)**: Create UI resources in Python.
- UI snippets must be able to interact with the agent. In mcp-ui, this is done by hooking into events sent from the UI snippet and reacting to them in the host (see onUIAction prop). For example, an HTML may trigger a t...

Basic usage or getting-started notes:
- <a href="#-getting-started">Getting Started</a> •
- **Usage:**

- Source: https://github.com/MCP-UI-Org/mcp-ui
- Extracted from upstream docs: https://raw.githubusercontent.com/MCP-UI-Org/mcp-ui/HEAD/README.md

## Documentation

- https://github.com/MCP-UI-Org/mcp-ui

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/render-interactive-mcp-tool-uis-with-mcp-ui/)
