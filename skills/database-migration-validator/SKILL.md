---
title: "Database Migration Validator"
description: "The Database Migration Validator skill ensures database schema migrations are safe to deploy in production environments. It analyzes SQL migration files to detect potentially dangerous operations like ALTER TABLE on large tables without concurrent index creation, column type changes that require full table rewrites, and DROP operations on referenced objects. For PostgreSQL environments, the skill queries pg_stat_statements to estimate query impact and uses pg_locks analysis to predict lock contention. For MySQL, it integrates with Percona pt-online-schema-change in dry-run mode to validate that online DDL operations will complete without blocking writes. It checks for missing indexes on foreign key columns that could cause sequential scans during JOIN operations. Additional validation includes backward compatibility checking for column renames and type changes (ensuring old application code can still function during rolling deployments), transaction isolation level verification for migration scripts, and estimation of migration duration based on table statistics from pg_class or INFORMATION_SCHEMA.TABLES. The skill outputs a risk assessment with specific recommendations for safer migration alternatives."
source: "https://agentskillexchange.com/skills/database-migration-validator/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Database Migration Validator

The Database Migration Validator skill ensures database schema migrations are safe to deploy in production environments. It analyzes SQL migration files to detect potentially dangerous operations like ALTER TABLE on large tables without concurrent index creation, column type changes that require full table rewrites, and DROP operations on referenced objects. For PostgreSQL environments, the skill queries pg_stat_statements to estimate query impact and uses pg_locks analysis to predict lock contention. For MySQL, it integrates with Percona pt-online-schema-change in dry-run mode to validate that online DDL operations will complete without blocking writes. It checks for missing indexes on foreign key columns that could cause sequential scans during JOIN operations. Additional validation includes backward compatibility checking for column renames and type changes (ensuring old application code can still function during rolling deployments), transaction isolation level verification for migration scripts, and estimation of migration duration based on table statistics from pg_class or INFORMATION_SCHEMA.TABLES. The skill outputs a risk assessment with specific recommendations for safer migration alternatives.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/)
