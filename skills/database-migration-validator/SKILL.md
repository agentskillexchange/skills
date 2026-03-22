---
name: "Database Migration Validator"
description: "Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward..."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: "verified_metadata"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/database-migration-validator/"
---

# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/skills install database-migration-validator
```

### Claude Code
```bash
claude mcp add database-migration-validator
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "database-migration-validator": {
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install database-migration-validator
```

### Codex
```bash
codex install database-migration-validator
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | verified_metadata |
| **Rating** | 0 (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/database-migration-validator/)
- [Browse All Skills](https://agentskillexchange.com/)
