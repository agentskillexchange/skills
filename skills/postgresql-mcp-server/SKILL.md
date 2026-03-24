---
name: "PostgreSQL MCP Server"
description: "Agent access to PostgreSQL data and queries through MCP."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL MCP Server

Agent access to PostgreSQL data and queries through MCP.

## Overview

Lets agents inspect schemas, run queries, and work with PostgreSQL-backed data sources in a structured way.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install postgresql-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-mcp-server/
