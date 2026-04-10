---
title: "Database Migration Validator"
description: "Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes."
slug: "database-migration-validator"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/database-migration-validator/"
---

# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install database-migration-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Database Migration Validator skill ensures database schema migrations are safe to deploy in production environments. It analyzes SQL migration files to detect potentially dangerous operations like ALTER TABLE on large tables without concurrent index creation, column type changes that require full table rewrites, and DROP operations on referenced objects.
For PostgreSQL environments, the skill queries pg_stat_statements to estimate query impact and uses pg_locks analysis to predict lock contention. For MySQL, it integrates with Percona pt-online-schema-change in dry-run mode to validate that online DDL operations will complete without blocking writes. It checks for missing indexes on foreign key columns that could cause sequential scans during JOIN operations.
Additional validation includes backward compatibility checking for column renames and type changes (ensuring old application code can still function during rolling deployments), transaction isolation level verification for migration scripts, and estimation of migration duration based on table statistics from pg_class or INFORMATION_SCHEMA.TABLES. The skill outputs a risk assessment with specific recommendations for safer migration alternatives.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/)
