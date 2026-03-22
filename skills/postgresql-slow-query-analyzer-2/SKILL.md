---
name: "PostgreSQL Slow Query Analyzer"
description: "Queries pg_stat_statements and pg_stat_activity to surface top slow queries by execution time and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrites, or vacuum triggers. Works on RDS, Supabase, and self-hosted Postgres."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 4.4
reviews: 83
creator: Alex Thompson
creator_handle: alexthompson
creator_verified: true
source: https://agentskillexchange.com/skill/postgresql-slow-query-analyzer-2/
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface top slow queries by execution time and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrites, or vacuum triggers. Works on RDS, Supabase, and self-hosted Postgres.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer-2 -a cursor
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-analyzer-2
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer-2 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Security Reviewed |
| Rating | 4.4/5 (83 reviews) |

## Creator

**Alex Thompson** (Verified Creator ✓)
- Profile: [@alexthompson](https://agentskillexchange.com/browse-skills/?creator=alexthompson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-analyzer-2/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
