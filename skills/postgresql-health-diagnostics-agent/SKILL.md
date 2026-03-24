---
name: "PostgreSQL Health Diagnostics Agent"
description: "Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
rating: 4.9
reviews: 11
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/"
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

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.9/5 (11 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
