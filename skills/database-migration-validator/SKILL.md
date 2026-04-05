---
name: "Database Migration Validator"
description: "Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes."
category: "Runbooks &amp; Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/database-migration-validator/"
---
# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

The Database Migration Validator skill ensures database schema migrations are safe to deploy in production environments. It analyzes SQL migration files to detect potentially dangerous operations like ALTER TABLE on large tables without concurrent index creation, column type changes that require full table rewrites, and DROP operations on referenced objects.

For PostgreSQL environments, the skill queries pg_stat_statements to estimate query impact and uses pg_locks analysis to predict lock contention. For MySQL, it integrates with Percona pt-online-schema-change in dry-run mode to validate that online DDL operations will complete without blocking writes. It checks for missing indexes on foreign key columns that could cause sequential scans during JOIN operations.

Additional validation includes backward compatibility checking for column renames and type changes (ensuring old application code can still function during rolling deployments), transaction isolation level verification for migration scripts, and estimation of migration duration based on table statistics from pg_class or INFORMATION_SCHEMA.TABLES. The skill outputs a risk assessment with specific recommendations for safer migration alternatives.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill database-migration-validator -a codex
```

### OpenClaw

```bash
clawhub install database-migration-validator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/)
