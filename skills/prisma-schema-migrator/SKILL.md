---
title: Prisma Schema Migrator
description: The Prisma Schema Migrator handles database schema evolution for projects
  using Prisma ORM. It automates migration planning by analyzing schema.prisma changes
  and generating migration SQL via prisma migrate dev and prisma migrate deploy commands.
  Before applying changes, it performs dry-run introspection using prisma db pull
  to validate that proposed schema modifications are compatible with existing data.
  The tool detects potentially destructive operations like column drops, type changes,
  and unique constraint additions, flagging them for review with data impact estimates.
  It integrates with prisma format for schema normalization and prisma validate for
  syntax checking before any migration attempt. For complex migrations requiring data
  transformation, it generates companion TypeScript scripts using the Prisma Client
  API to move data between old and new schemas. The migrator also handles multi-database
  setups with separate schema files for PostgreSQL, MySQL, and SQLite targets, maintaining
  migration history consistency across environments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prisma-schema-migrator/
category:
- Library &amp; API Reference
framework:
- Codex
---

# Prisma Schema Migrator

The Prisma Schema Migrator handles database schema evolution for projects using Prisma ORM. It automates migration planning by analyzing schema.prisma changes and generating migration SQL via prisma migrate dev and prisma migrate deploy commands. Before applying changes, it performs dry-run introspection using prisma db pull to validate that proposed schema modifications are compatible with existing data. The tool detects potentially destructive operations like column drops, type changes, and unique constraint additions, flagging them for review with data impact estimates. It integrates with prisma format for schema normalization and prisma validate for syntax checking before any migration attempt. For complex migrations requiring data transformation, it generates companion TypeScript scripts using the Prisma Client API to move data between old and new schemas. The migrator also handles multi-database setups with separate schema files for PostgreSQL, MySQL, and SQLite targets, maintaining migration history consistency across environments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prisma-schema-migrator/)
