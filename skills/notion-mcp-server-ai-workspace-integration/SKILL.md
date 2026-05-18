---
name: "Notion MCP Server for AI Workspace Integration"
slug: "notion-mcp-server-ai-workspace-integration"
description: "The official Notion MCP Server enables AI agents to interact with Notion workspaces through the Model Context Protocol. It provides tools for querying data sources, creating and updating pages, searching content, and managing databases — all accessible via natural language prompts from Claude, Cursor, Copilot, and other MCP clients."
github_stars: 4141
verification: "security_reviewed"
source: "https://github.com/makenotion/notion-mcp-server"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "makenotion/notion-mcp-server"
  github_stars: 4141
---

# Notion MCP Server for AI Workspace Integration

The official Notion MCP Server enables AI agents to interact with Notion workspaces through the Model Context Protocol. It provides tools for querying data sources, creating and updating pages, searching content, and managing databases — all accessible via natural language prompts from Claude, Cursor, Copilot, and other MCP clients.

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose build
- npx @notionhq/notion-mcp-server
- npx @notionhq/notion-mcp-server --transport stdio
- npx @notionhq/notion-mcp-server --transport http

Requirements and caveats from upstream:
- ##### Using Docker
- There are two options for running the MCP server with Docker:
- ###### Option 1: Using the official Docker Hub image

Basic usage or getting-started notes:
- #### 1. Setting up integration in Notion
- Go to [https://www.notion.so/profile/integrations](https://www.notion.so/profile/integrations) and create a new **internal** integration or select an existing one.
- ![Creating a Notion Integration token](docs/images/integrations-creation.png)

- Source: https://github.com/makenotion/notion-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/makenotion/notion-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-mcp-server-ai-workspace-integration/)
