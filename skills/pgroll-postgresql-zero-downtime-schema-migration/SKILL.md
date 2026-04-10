---
title: "pgroll PostgreSQL Zero-Downtime Schema Migration"
description: "pgroll is an open-source CLI tool by Xata that performs zero-downtime, reversible schema migrations for PostgreSQL. It uses the expand-and-contract pattern to keep old and new schema versions running simultaneously with automatic backfilling and instant rollback."
slug: "pgroll-postgresql-zero-downtime-schema-migration"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/xataio/pgroll"
tool_ecosystem:
  github_repo: "xataio/pgroll"
  github_stars: 6408
listed: true
---

# pgroll PostgreSQL Zero-Downtime Schema Migration

pgroll is an open-source CLI tool by Xata that performs zero-downtime, reversible schema migrations for PostgreSQL. It uses the expand-and-contract pattern to keep old and new schema versions running simultaneously with automatic backfilling and instant rollback.

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
clawhub install pgroll-postgresql-zero-downtime-schema-migration
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

pgroll is an open-source PostgreSQL schema migration tool built by Xata that eliminates downtime and breaking changes during database migrations. Written in Go and available as a standalone CLI binary, it implements the expand-and-contract pattern to evolve database schemas safely in production environments.
The core principle behind pgroll is dual-schema versioning: when a migration starts, pgroll creates a new version of the schema while keeping the old version fully operational. Both schema versions coexist simultaneously, allowing applications using the old schema to continue working while new application versions adopt the updated schema. This eliminates the traditional migration problem where a schema change can break running application instances during deployment.
Migrations are defined as JSON operation files that describe the desired schema changes. pgroll supports column additions, removals, renames, type changes, constraint modifications, index creation, and table-level operations. When a column is modified, pgroll automatically creates the new column version and sets up triggers to backfill data bidirectionally between old and new columns. This means reads and writes work correctly against both schema versions throughout the migration lifecycle.
Key technical capabilities include: zero database locking during migrations (PostgreSQL does not block data access while changes are applied), automatic column backfilling with configurable transformation expressions, instant rollback by canceling a migration (the old schema was never removed), and support for multi-step migrations that compose multiple operations atomically.
The CLI interface is minimal: pgroll start begins a migration, pgroll complete finalizes it (removing the old schema version), and pgroll rollback reverts. pgroll tracks migration state in a dedicated schema within the target database. The tool has over 5,000 GitHub stars, is actively maintained with regular releases, and is licensed under Apache 2.0. It installs via Go, Homebrew, or direct binary download from GitHub releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgroll-postgresql-zero-downtime-schema-migration/)
