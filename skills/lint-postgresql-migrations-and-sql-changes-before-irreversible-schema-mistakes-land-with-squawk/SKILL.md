---
title: "Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk"
description: "Catch locking, indexing, and schema-change hazards in PostgreSQL migration SQL before a review turns into downtime."
verification: listed
source: "https://github.com/sbdchd/squawk"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sbdchd/squawk"
  github_stars: 1050
---

# Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk

Use Squawk when an agent is reviewing PostgreSQL migrations or raw SQL files and needs a migration-safety pass, not when a user just wants a normal database client or editor. The workflow is tightly bounded: lint the migration SQL, flag risky patterns like blocking index creation or bad type choices, and return actionable fixes before merge or rollout. That scope boundary, pre-merge Postgres migration linting for operational safety, keeps it distinct from a generic Postgres product card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/)
