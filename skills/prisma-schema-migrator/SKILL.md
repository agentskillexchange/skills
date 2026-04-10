---
name: Prisma Schema Migrator
description: Automates Prisma ORM schema evolution and migration planning using prisma
  migrate and prisma db commands. Validates schema changes against existing data with
  dry-run introspection via prisma db pull.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prisma-schema-migrator/)
