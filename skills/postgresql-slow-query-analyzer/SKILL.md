---
name: "PostgreSQL Slow Query Analyzer"
description: "Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: listed
rating: 4.8
reviews: 80
creator: "Tom Anderson"
creator_handle: "@tanderson"
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/"
---
# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Listed |
| Rating | 4.8/5 (80 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
