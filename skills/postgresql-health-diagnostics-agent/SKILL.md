---
name: "PostgreSQL Health Diagnostics Agent"
description: "Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# PostgreSQL Health Diagnostics Agent

Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-health-diagnostics-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-health-diagnostics-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-health-diagnostics-agent -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-health-diagnostics-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-health-diagnostics-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
