---
name: "PostgreSQL Health Diagnostics Agent"
description: "Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: "security_reviewed"
rating: 4.9
reviews: 11
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/postgresql-health-diagnostics-agent/"
---

# PostgreSQL Health Diagnostics Agent

Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns.

## Installation

Install this skill across different agents:

### Any AI Agent (npx)
```bash
npx @anthropic/skills install postgresql-health-diagnostics-agent
```

### Claude Code
```bash
claude skills install postgresql-health-diagnostics-agent
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["postgresql-health-diagnostics-agent"]
}
```

### OpenClaw
```bash
clawhub install postgresql-health-diagnostics-agent
```

### Codex
```bash
codex skills install postgresql-health-diagnostics-agent
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

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-health-diagnostics-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
