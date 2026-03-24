---
name: "PostgreSQL Query Plan Explainer"
description: "Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-plan-explainer/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-explainer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
