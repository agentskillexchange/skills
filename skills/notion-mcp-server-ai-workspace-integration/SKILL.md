---
title: Notion MCP Server for AI Workspace Integration
description: What is the Notion MCP Server? The Notion MCP Server is an official Model
  Context Protocol server built and maintained by Notion (makenotion). It implements
  the MCP specification to bridge AI agents and LLM-powered code editors with the
  Notion API, enabling natural language interaction with Notion workspaces. Published
  as @notionhq/notion-mcp-server on npm with over 15 releases, it is one of the most
  widely adopted MCP servers in the ecosystem with over 4,000 GitHub stars. How It
  Works The server exposes 22 MCP tools that map to Notion API endpoints. AI agents
  can search pages and databases, query data sources with filters and sorts, create
  and update pages with rich content, manage comments, and retrieve user information.
  The server runs locally via npx or Docker, communicating over stdio or HTTP transport
  with MCP clients like Claude Desktop, Cursor, Windsurf, VS Code Copilot, or Cline.
  Version 2.0 introduced data sources as the primary abstraction for databases, aligning
  with Notion API 2025-09-03. This means agents work with data_source_id instead of
  database_id, enabling more flexible querying and manipulation of structured data
  within Notion. The server also supports OAuth-based remote connections via Notion
  MCP (remote) for even simpler setup. What It Outputs Agents using this server can
  create new pages with structured content, query databases and return filtered results,
  post comments on pages, move pages between parents, and search across an entire
  workspace. Output follows MCP tool response format, making it directly consumable
  by LLMs for summarization, analysis, or follow-up actions. Integration Points Configuration
  requires a Notion integration token and a one-line addition to your MCP client config.
  The server works with any MCP-compatible client. It supports both stdio transport
  (default) and Streamable HTTP transport for web-based applications. Docker images
  are available on Docker Hub as mcp/notion for containerized deployments.
verification: security_reviewed
source: https://github.com/makenotion/notion-mcp-server
category:
- Integrations &amp; Connectors
framework:
- MCP
tool_ecosystem:
  github_repo: makenotion/notion-mcp-server
  github_stars: 4141
---

# Notion MCP Server for AI Workspace Integration

What is the Notion MCP Server? The Notion MCP Server is an official Model Context Protocol server built and maintained by Notion (makenotion). It implements the MCP specification to bridge AI agents and LLM-powered code editors with the Notion API, enabling natural language interaction with Notion workspaces. Published as @notionhq/notion-mcp-server on npm with over 15 releases, it is one of the most widely adopted MCP servers in the ecosystem with over 4,000 GitHub stars. How It Works The server exposes 22 MCP tools that map to Notion API endpoints. AI agents can search pages and databases, query data sources with filters and sorts, create and update pages with rich content, manage comments, and retrieve user information. The server runs locally via npx or Docker, communicating over stdio or HTTP transport with MCP clients like Claude Desktop, Cursor, Windsurf, VS Code Copilot, or Cline. Version 2.0 introduced data sources as the primary abstraction for databases, aligning with Notion API 2025-09-03. This means agents work with data_source_id instead of database_id, enabling more flexible querying and manipulation of structured data within Notion. The server also supports OAuth-based remote connections via Notion MCP (remote) for even simpler setup. What It Outputs Agents using this server can create new pages with structured content, query databases and return filtered results, post comments on pages, move pages between parents, and search across an entire workspace. Output follows MCP tool response format, making it directly consumable by LLMs for summarization, analysis, or follow-up actions. Integration Points Configuration requires a Notion integration token and a one-line addition to your MCP client config. The server works with any MCP-compatible client. It supports both stdio transport (default) and Streamable HTTP transport for web-based applications. Docker images are available on Docker Hub as mcp/notion for containerized deployments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-mcp-server-ai-workspace-integration/)
