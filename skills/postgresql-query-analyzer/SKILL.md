---
name: "PostgreSQL Query Analyzer"
description: "Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-analyzer/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# PostgreSQL Query Analyzer

Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-query-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
