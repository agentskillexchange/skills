---
title: "Neon Serverless Postgres MCP"
description: "Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform."
verification: security_reviewed
source: "https://github.com/neondatabase/mcp-server-neon"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 579
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/)
