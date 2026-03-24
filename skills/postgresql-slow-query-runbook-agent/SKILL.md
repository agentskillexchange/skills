---
name: "PostgreSQL Slow Query Runbook"
description: "Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.1
reviews: 86
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/"
---
# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.1/5 (86 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
