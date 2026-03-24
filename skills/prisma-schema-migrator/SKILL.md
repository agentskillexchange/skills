---
name: "Prisma Schema Migrator"
description: "Automates Prisma ORM schema evolution and migration planning using prisma migrate and prisma db commands. Validates schema changes against existing data with dry-run introspection via prisma db pull."
category: "Library & API Reference"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prisma-schema-migrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prisma"  # from ase_tool_match
  github_stars: 45585  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9355280  # from ase_npm_downloads
  github_repo: "prisma/prisma"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prisma Schema Migrator

Automates Prisma ORM schema evolution and migration planning using prisma migrate and prisma db commands. Validates schema changes against existing data with dry-run introspection via prisma db pull.

## Overview

The Prisma Schema Migrator handles database schema evolution for projects using Prisma ORM. It automates migration planning by analyzing schema.prisma changes and generating migration SQL via prisma migrate dev and prisma migrate deploy commands. Before applying changes, it performs dry-run introspection using prisma db pull to validate that proposed schema modifications are compatible with existing data. The tool detects potentially destructive operations like column drops, type changes, and unique constraint additions, flagging them for review with data impact estimates. It integrates with prisma format for schema normalization and prisma validate for syntax checking before any migration attempt. For complex migrations requiring data transformation, it generates companion TypeScript scripts using the Prisma Client API to move data between old and new schemas. The migrator also handles multi-database setups with separate schema files for PostgreSQL, MySQL, and SQLite targets, maintaining migration history consistency across environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prisma-schema-migrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prisma-schema-migrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prisma-schema-migrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prisma-schema-migrator -a codex
```

### OpenClaw

```bash
clawhub install prisma-schema-migrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prisma-schema-migrator/
