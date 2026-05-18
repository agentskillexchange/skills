---
name: "Neon MCP Server for Serverless Postgres Management"
slug: "neon-mcp-server-serverless-postgres"
description: "The Neon MCP Server enables AI agents to manage serverless PostgreSQL databases through natural language via the Model Context Protocol. Create projects, run queries, manage branches, and perform database migrations conversationally."
github_stars: 567
verification: "listed"
source: "https://github.com/neondatabase/mcp-server-neon"
author: "Neon"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 567
  npm_package: "@neondatabase/mcp-server-neon"
  npm_weekly_downloads: 15537
---

# Neon MCP Server for Serverless Postgres Management

The Neon MCP Server enables AI agents to manage serverless PostgreSQL databases through natural language via the Model Context Protocol. Create projects, run queries, manage branches, and perform database migrations conversationally.

## Installation

Use the upstream install or setup path that matches your environment:
- npx neonctl@latest init
- npx add-mcp https://mcp.neon.tech/mcp
- npx add-mcp https://mcp.neon.tech/mcp --header "Authorization: Bearer <$NEON_API_KEY>"
- npx add-mcp https://mcp.neon.tech/sse --type sse

Requirements and caveats from upstream:
- **Node.js (>= v18.0.0):** Download from [nodejs.org](https://nodejs.org).
- For development, you'll need Node.js 22+ (pnpm is provided via Corepack — run corepack enable to activate it).
- Connect to Neon's managed MCP server using OAuth for authentication. This is the easiest setup, requires no local installation of this server, and doesn't need a Neon API key configured in the client.

Basic usage or getting-started notes:
- For example, in Claude Code, or any MCP Client, you can use natural language to accomplish things with Neon, such as:
- I want to run a migration on my project called "my-project" that alters the users table to add a new column called "created_at".
- **Quick Setup with API Key (Cursor, VS Code, and Claude Code):** Run [neonctl@latest init](https://neon.com/docs/reference/cli-init) to automatically configure Neon's MCP Server, [agent skills](https://github.com/neon...

- Source: https://github.com/neondatabase/mcp-server-neon
- Extracted from upstream docs: https://raw.githubusercontent.com/neondatabase/mcp-server-neon/HEAD/README.md

## Documentation

- https://github.com/neondatabase/mcp-server-neon

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-mcp-server-serverless-postgres/)
