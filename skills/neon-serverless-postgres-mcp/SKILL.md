---
title: "Neon Serverless Postgres MCP"
description: "Neon MCP Server is maintained by Neon and designed for use with Claude Code, Cursor, VS Code, and any MCP-compatible client. It bridges natural language requests to the Neon Management API for full database lifecycle management.\nBest for\n\nCreating and managing Neon projects through conversational commands\nBranch-based migrations: test schema changes on a temporary branch before committing\nRunning SQL queries against any Neon database through the agent\nExploring schemas, tables, and data summaries\n\nHow it differs from Postgres MCP Pro\nPostgres MCP Pro provides deep query analysis against any PostgreSQL instance. Neon MCP manages Neon-specific platform infrastructure — creating projects, branching databases for safe migrations, and managing the serverless platform layer.\nInstall notes\nQuickest: npx neonctl@latest init (auto-configures everything). Manual: npx -y @neondatabase/mcp-server-neon start YOUR_API_KEY. Remote: Connect to https://mcp.neon.tech/mcp with OAuth. Free tier available.\nSource: github.com/neondatabase/mcp-server-neon"
verification: security_reviewed
source: "https://github.com/neondatabase/mcp-server-neon"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 580
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/neon-serverless-postgres-mcp
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/neon-serverless-postgres-mcp` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
