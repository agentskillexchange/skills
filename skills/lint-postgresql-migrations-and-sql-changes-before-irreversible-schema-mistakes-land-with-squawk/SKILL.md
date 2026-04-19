---
title: "Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk"
description: "Use Squawk when an agent is reviewing PostgreSQL migrations or raw SQL files and needs a migration-safety pass, not when a user just wants a normal database client or editor. The workflow is tightly bounded: lint the migration SQL, flag risky patterns like blocking index creation or bad type choices, and return actionable fixes before merge or rollout. That scope boundary, pre-merge Postgres migration linting for operational safety, keeps it distinct from a generic Postgres product card."
source: "https://github.com/sbdchd/squawk"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sbdchd/squawk"
  github_stars: 1050
---

# Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk

Use Squawk when an agent is reviewing PostgreSQL migrations or raw SQL files and needs a migration-safety pass, not when a user just wants a normal database client or editor. The workflow is tightly bounded: lint the migration SQL, flag risky patterns like blocking index creation or bad type choices, and return actionable fixes before merge or rollout. That scope boundary, pre-merge Postgres migration linting for operational safety, keeps it distinct from a generic Postgres product card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/)
