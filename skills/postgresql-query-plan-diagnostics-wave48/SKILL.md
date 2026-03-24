---
name: "PostgreSQL Query Plan Diagnostics"
description: "Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
rating: 4.9
reviews: 5
creator: "Sarah Chen"
creator_handle: "@sarahchen"
creator_verified: true
source: "https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/"
---
# PostgreSQL Query Plan Diagnostics

Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a cursor
```

### OpenClaw

```bash
clawhub install postgresql-query-plan-diagnostics-wave48
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.9/5 (5 reviews) |

## Creator

**Sarah Chen** (Verified Creator ✓)
- Profile: [@sarahchen](https://agentskillexchange.com/browse-skills/?creator=sarahchen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-query-plan-diagnostics-wave48/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
