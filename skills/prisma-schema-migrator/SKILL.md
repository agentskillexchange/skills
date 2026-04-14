---
title: "Prisma Schema Migrator"
description: "Automates Prisma ORM schema evolution and migration planning using prisma migrate and prisma db commands. Validates schema changes against existing data with dry-run introspection via prisma db pull."
verification: security_reviewed
source: "https://github.com/prisma/prisma"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prisma-schema-migrator/)
