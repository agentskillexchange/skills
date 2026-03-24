---
name: "PostgreSQL Query Plan Explainer"
description: "Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.1
reviews: 53
creator: "Community"
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-plan-explainer/"
---
# PostgreSQL Query Plan Explainer

Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-query-plan-explainer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a codex
```
## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | 4.1 ⭐⭐⭐⭐ (53 reviews) |

## Creator

**Community**

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-query-plan-explainer/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
