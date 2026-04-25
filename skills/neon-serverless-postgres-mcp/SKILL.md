---
title: "Neon Serverless Postgres MCP"
description: "Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform."
verification: "security_reviewed"
source: "https://github.com/neondatabase/mcp-server-neon"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 590
---

# Neon Serverless Postgres MCP

Neon MCP Server is maintained by Neon and designed for use with Claude Code, Cursor, VS Code, and any MCP-compatible client. It bridges natural language requests to the Neon Management API for full database lifecycle management.

Best for

- Creating and managing Neon projects through conversational commands

- Branch-based migrations: test schema changes on a temporary branch before committing

- Running SQL queries against any Neon database through the agent

- Exploring schemas, tables, and data summaries

How it differs from Postgres MCP Pro
Postgres MCP Pro provides deep query analysis against any PostgreSQL instance. Neon MCP manages Neon-specific platform infrastructure — creating projects, branching databases for safe migrations, and managing the serverless platform layer.

Install notes
Quickest: npx neonctl@latest init (auto-configures everything). Manual: npx -y @neondatabase/mcp-server-neon start YOUR_API_KEY. Remote: Connect to https://mcp.neon.tech/mcp with OAuth. Free tier available.

Source: github.com/neondatabase/mcp-server-neon

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/neon-serverless-postgres-mcp
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/neon-serverless-postgres-mcp`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
