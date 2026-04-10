---
name: Neon Serverless Postgres MCP
description: Neon&#8217;s official MCP server translates natural language requests
  into Neon API calls, letting AI agents create projects, manage branches, run SQL
  queries, and perform database migrations on Neon&#8217;s serverless Postgres platform.
verification: security_reviewed
source: https://github.com/neondatabase/mcp-server-neon
category:
- Integrations &amp; Connectors
framework:
- MCP
tool_ecosystem:
  github_repo: neondatabase/mcp-server-neon
  github_stars: 574
  license: MIT
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
