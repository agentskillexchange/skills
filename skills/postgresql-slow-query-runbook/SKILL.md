---
name: "PostgreSQL Slow Query Runbook"
description: "Identifies slow queries in PostgreSQL by querying pg_stat_statements and pg_stat_activity via the PostgreSQL information schema and psycopg2. Correlates query plans from EXPLAIN ANALYZE with table bloat metrics from pgstattuple. Outputs an actionable runbook with index recommendations and vacuum scheduling."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.8
reviews: 76
creator: James Whitfield
creator_handle: jwhitfield
creator_verified: true
source: https://agentskillexchange.com/skill/postgresql-slow-query-runbook/
---

# PostgreSQL Slow Query Runbook

Identifies slow queries in PostgreSQL by querying pg_stat_statements and pg_stat_activity via the PostgreSQL information schema and psycopg2. Correlates query plans from EXPLAIN ANALYZE with table bloat metrics from pgstattuple. Outputs an actionable runbook with index recommendations and vacuum scheduling.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook -a cursor
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.8/5 (76 reviews) |

## Creator

**James Whitfield** (Verified Creator ✓)
- Profile: [@jwhitfield](https://agentskillexchange.com/browse-skills/?creator=jwhitfield)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
