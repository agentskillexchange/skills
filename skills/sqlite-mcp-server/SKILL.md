---
name: "SQLite MCP Server"
description: "Lightweight local database access for agent tasks."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sqlite-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  github_stars: 7041  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
  github_repo: "WiseLibs/better-sqlite3"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SQLite MCP Server

Lightweight local database access for agent tasks.

## Overview

Lets agents inspect and query SQLite databases, making it useful for local apps, exports, and embedded data workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sqlite-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install sqlite-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sqlite-mcp-server/
