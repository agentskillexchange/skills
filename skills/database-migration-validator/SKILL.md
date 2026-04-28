---
title: Database Migration Validator
description: Validates SQL database migrations for safety using pg_stat_statements
  analysis and pt-online-schema-change dry-run mode. Checks for long-running locks,
  missing indexes on foreign keys, and backward-incompatible column changes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/database-migration-validator/
category:
- Runbooks & Diagnostics
framework:
- OpenClaw
---

# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/database-migration-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/database-migration-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/database-migration-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/)
