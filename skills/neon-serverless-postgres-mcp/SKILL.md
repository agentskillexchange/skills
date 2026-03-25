---
name: "Neon Serverless Postgres MCP"
description: "Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# Neon Serverless Postgres MCP

Neon’s official MCP server translates natural language requests into Neon API calls, letting AI agents create projects, manage branches, run SQL queries, and perform database migrations on Neon’s serverless Postgres platform.

## Overview

Neon MCP Server is maintained by Neon and designed for use with Claude Code, Cursor, VS Code, and any MCP-compatible client. It bridges natural language requests to the Neon Management API for full database lifecycle management.

Best for

Creating and managing Neon projects through conversational commands

Branch-based migrations: test schema changes on a temporary branch before committing

Running SQL queries against any Neon database through the agent

Exploring schemas, tables, and data summaries

How it differs from Postgres MCP Pro

Postgres MCP Pro provides deep query analysis against any PostgreSQL instance. Neon MCP manages Neon-specific platform infrastructure — creating projects, branching databases for safe migrations, and managing the serverless platform layer.

Install notes

**Quickest:** `npx neonctl@latest init` (auto-configures everything). **Manual:** `npx -y @neondatabase/mcp-server-neon start YOUR_API_KEY`. **Remote:** Connect to `https://mcp.neon.tech/mcp` with OAuth. Free tier available.

**Source:** [github.com/neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill neon-serverless-postgres-mcp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill neon-serverless-postgres-mcp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill neon-serverless-postgres-mcp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill neon-serverless-postgres-mcp -a codex
```

### OpenClaw

```bash
clawhub install neon-serverless-postgres-mcp
```

## Source

- Marketplace: https://agentskillexchange.com/skills/neon-serverless-postgres-mcp/
