---
name: "PostgreSQL Slow Query Analyzer"
description: "Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-slow-query-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
