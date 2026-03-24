---
name: "PostgreSQL Slow Query Runbook"
description: "Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-slow-query-runbook-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
