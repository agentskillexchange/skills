---
name: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
rating: 4.8
reviews: 82
creator: "Ben Taylor"
creator_handle: "@bentaylor"
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-performance-diagnostics/"
security: "✅ Reviewed"
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
[View Profile on ASE](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/) • [Browse All Skills](https://agentskillexchange.com)