---
title: "Neon Serverless Postgres MCP"
description: "Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform."
slug: "neon-serverless-postgres-mcp"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/neondatabase/mcp-server-neon"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 574
---

# Neon Serverless Postgres MCP

Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install neon-serverless-postgres-mcp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
