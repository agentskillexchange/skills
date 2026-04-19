---
title: "Prisma Schema Migrator"
description: "The Prisma Schema Migrator handles database schema evolution for projects using Prisma ORM. It automates migration planning by analyzing schema.prisma changes and generating migration SQL via prisma migrate dev and prisma migrate deploy commands. Before applying changes, it performs dry-run introspection using prisma db pull to validate that proposed schema modifications are compatible with existing data. The tool detects potentially destructive operations like column drops, type changes, and unique constraint additions, flagging them for review with data impact estimates. It integrates with prisma format for schema normalization and prisma validate for syntax checking before any migration attempt. For complex migrations requiring data transformation, it generates companion TypeScript scripts using the Prisma Client API to move data between old and new schemas. The migrator also handles multi-database setups with separate schema files for PostgreSQL, MySQL, and SQLite targets, maintaining migration history consistency across environments."
source: "https://github.com/prisma/prisma"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "prisma/prisma"
  github_stars: 45760
  npm_package: "prisma"
  npm_weekly_downloads: 9910505
---

# Prisma Schema Migrator

The Prisma Schema Migrator handles database schema evolution for projects using Prisma ORM. It automates migration planning by analyzing schema.prisma changes and generating migration SQL via prisma migrate dev and prisma migrate deploy commands. Before applying changes, it performs dry-run introspection using prisma db pull to validate that proposed schema modifications are compatible with existing data. The tool detects potentially destructive operations like column drops, type changes, and unique constraint additions, flagging them for review with data impact estimates. It integrates with prisma format for schema normalization and prisma validate for syntax checking before any migration attempt. For complex migrations requiring data transformation, it generates companion TypeScript scripts using the Prisma Client API to move data between old and new schemas. The migrator also handles multi-database setups with separate schema files for PostgreSQL, MySQL, and SQLite targets, maintaining migration history consistency across environments.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prisma-schema-migrator/)
