---
title: "Neon Serverless Postgres MCP"
description: "Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform."
verification: "security_reviewed"
source: "https://github.com/neondatabase/mcp-server-neon"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 580
  license: "MIT"
---

# Neon Serverless Postgres MCP

Neon MCP Server is maintained by Neon and designed for use with Claude Code, Cursor, VS Code, and any MCP-compatible client. It bridges natural language requests to the Neon Management API for full database lifecycle management.

Best for

Creating and managing Neon projects through conversational commands

Branch-based migrations: test schema changes on a temporary branch before committing

Running SQL queries against any Neon database through the agent

Exploring schemas, tables, and data summaries

How it differs from Postgres MCP Pro

Postgres MCP Pro provides deep query analysis against any PostgreSQL instance. Neon MCP manages Neon-specific platform infrastructure — creating projects, branching databases for safe migrations, and managing the serverless platform layer.

Install notes

Quickest: npx neonctl@latest init (auto-configures everything). Manual: npx -y @neondatabase/mcp-server-neon start YOUR_API_KEY. Remote: Connect to https://mcp.neon.tech/mcp with OAuth. Free tier available.

Source: github.com/neondatabase/mcp-server-neon

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
