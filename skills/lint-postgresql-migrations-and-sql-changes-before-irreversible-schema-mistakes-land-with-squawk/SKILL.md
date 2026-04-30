---
title: "Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk"
description: "Catch locking, indexing, and schema-change hazards in PostgreSQL migration SQL before a review turns into downtime."
verification: "listed"
source: "https://github.com/sbdchd/squawk"
author: "sbdchd"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "sbdchd/squawk"
  github_stars: 1050
---

# Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk

Catch locking, indexing, and schema-change hazards in PostgreSQL migration SQL before a review turns into downtime.

## Prerequisites

Squawk CLI or container image, PostgreSQL migration SQL files, and optional CI or pre-commit integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Squawk from the upstream CLI, package, container, or release path, point it at the migration SQL files or repository, and review the reported warnings before merging or applying schema changes.
```

## Documentation

- https://squawkhq.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/)
