---
name: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-performance-diagnostics/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# PostgreSQL Performance Diagnostics

Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-performance-diagnostics
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
