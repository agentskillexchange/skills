---
name: "Database Migration Validator"
description: "Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/database-migration-validator/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
---

# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill database-migration-validator
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill database-migration-validator -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill database-migration-validator -a cursor
```

### OpenClaw
```bash
clawhub install database-migration-validator
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill database-migration-validator -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
