---
title: "Prisma Schema Migrator"
description: "Automates Prisma ORM schema evolution and migration planning using prisma migrate and prisma db commands. Validates schema changes against existing data with dry-run introspection via prisma db pull."
verification: security_reviewed
source: "https://github.com/prisma/prisma"
category:
  - "Library & API Reference"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prisma-schema-migrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prisma-schema-migrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prisma-schema-migrator/)
