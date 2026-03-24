---
name: "MySQL Query Agent"
description: "AI agent skill for querying, analyzing, and managing MySQL databases. Supports query generation, execution plan analysis, index recommendations, and schema inspection across MySQL 5.7+ and MariaDB."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mysql-query-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "mysql"  # from ase_tool_match
  github_stars: 4348  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8743089  # from ase_npm_downloads
  github_repo: "sidorares/node-mysql2"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# MySQL Query Agent

AI agent skill for querying, analyzing, and managing MySQL databases. Supports query generation, execution plan analysis, index recommendations, and schema inspection across MySQL 5.7+ and MariaDB.

## Overview

AI agent skill for querying, analyzing, and managing MySQL databases. Supports query generation, execution plan analysis, index recommendations, and schema inspection across MySQL 5.7+ and MariaDB.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mysql-query-agent -a codex
```

### OpenClaw

```bash
clawhub install mysql-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mysql-query-agent/
