---
name: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: "✅ Verified"
security: "✅ Reviewed"
rating: "4.8"
reviews: "82"
creator: "Ben Taylor"
creator_handle: "@bentaylor"
creator_verified: false
source: "https://agentskillexchange.com/skill/postgresql-performance-diagnostics/"
---

# PostgreSQL Performance Diagnostics

Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install postgresql-performance-diagnostics
```

### Claude Code
```bash
claude skills add postgresql-performance-diagnostics
```

### Cursor
Add to your `.cursor/skills` configuration:
```json
{
  "skills": ["postgresql-performance-diagnostics"]
}
```

### OpenClaw
```bash
clawhub install postgresql-performance-diagnostics
```

### Codex
```bash
codex skills add postgresql-performance-diagnostics
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | ✅ Verified |
| **Security** | ✅ Reviewed |
| **Rating** | ⭐ 4.8 (82 reviews) |

## Creator

**Ben Taylor** 
Handle: `@bentaylor`
[View Profile on ASE](https://agentskillexchange.com/skill/postgresql-performance-diagnostics/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-performance-diagnostics/) • [Browse All Skills](https://agentskillexchange.com)