---
title: "pgroll PostgreSQL Zero-Downtime Schema Migration"
description: "pgroll is an open-source CLI tool by Xata that performs zero-downtime, reversible schema migrations for PostgreSQL. It uses the expand-and-contract pattern to keep old and new schema versions running simultaneously with automatic backfilling and instant rollback."
verification: "security_reviewed"
source: "https://github.com/xataio/pgroll"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "xataio/pgroll"
  github_stars: 6408
---

# pgroll PostgreSQL Zero-Downtime Schema Migration

pgroll is an open-source PostgreSQL schema migration tool built by Xata that eliminates downtime and breaking changes during database migrations. Written in Go and available as a standalone CLI binary, it implements the expand-and-contract pattern to evolve database schemas safely in production environments. The core principle behind pgroll is dual-schema versioning: when a migration starts, pgroll creates a new version of the schema while keeping the old version fully operational. Both schema versions coexist simultaneously, allowing applications using the old schema to continue working while new application versions adopt the updated schema. This eliminates the traditional migration problem where a schema change can break running application instances during deployment. Migrations are defined as JSON operation files that describe the desired schema changes. pgroll supports column additions, removals, renames, type changes, constraint modifications, index creation, and table-level operations. When a column is modified, pgroll automatically creates the new column version and sets up triggers to backfill data bidirectionally between old and new columns. This means reads and writes work correctly against both schema versions throughout the migration lifecycle. Key technical capabilities include: zero database locking during migrations (PostgreSQL does not block data access while changes are applied), automatic column backfilling with configurable transformation expressions, instant rollback by canceling a migration (the old schema was never removed), and support for multi-step migrations that compose multiple operations atomically. The CLI interface is minimal: pgroll start begins a migration, pgroll complete finalizes it (removing the old schema version), and pgroll rollback reverts. pgroll tracks migration state in a dedicated schema within the target database. The tool has over 5,000 GitHub stars, is actively maintained with regular releases, and is licensed under Apache 2.0. It installs via Go, Homebrew, or direct binary download from GitHub releases.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pgroll-postgresql-zero-downtime-schema-migration/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pgroll-postgresql-zero-downtime-schema-migration
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pgroll-postgresql-zero-downtime-schema-migration`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgroll-postgresql-zero-downtime-schema-migration/)
