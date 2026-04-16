---
title: "Supabase MCP Server for Database and Project Management"
description: "An official MCP server that connects Supabase projects to AI assistants like Claude, Cursor, and Windsurf. Enables natural-language database management, table operations, SQL queries, and project configuration through the Model Context Protocol."
verification: "security_reviewed"
source: "https://github.com/supabase-community/supabase-mcp"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "supabase-community/supabase-mcp"
  github_stars: 2572
---

# Supabase MCP Server for Database and Project Management

The Supabase MCP Server is an official Model Context Protocol integration built by the Supabase community that connects your Supabase projects directly to AI assistants. Available at github.com/supabase-community/supabase-mcp, this server bridges the gap between natural language AI interactions and Supabase’s powerful backend-as-a-service platform.

At its core, the server exposes Supabase’s complete feature set through MCP tools. AI agents can execute SQL queries against your Postgres database, manage tables and schemas, configure Row Level Security policies, handle storage buckets, and interact with Edge Functions — all through conversational commands. The server supports both Supabase Cloud (via OAuth 2.1 authentication) and self-hosted instances, making it flexible for any deployment model.

Security is handled through multiple layers. The server supports read-only mode to restrict operations to safe queries, project scoping to limit access to a single project, and feature groups to enable only specific tool categories. This means you can give an AI assistant access to query your database without worrying about destructive operations.

Integration is straightforward: configure your MCP client with the server URL (https://mcp.supabase.com/mcp) and authenticate via OAuth. The server works with Claude Desktop, Cursor, Windsurf, and any MCP-compatible client. For local development with Supabase CLI, the server is available at localhost:54321/mcp. With 2,600+ GitHub stars and active development, the Supabase MCP Server is one of the most widely adopted MCP integrations available.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supabase-mcp-server-database-project-management/)
