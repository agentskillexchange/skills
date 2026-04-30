---
title: "Diff live database schemas against declarative SQL before schema drift reaches production with sqldef"
description: "Compare checked-in SQL against live MySQL, PostgreSQL, SQLite, or SQL Server schemas and generate a reviewable apply plan before agents touch production databases."
verification: "listed"
source: "https://github.com/sqldef/sqldef"
author: "sqldef"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "sqldef/sqldef"
  github_stars: 3076
---

# Diff live database schemas against declarative SQL before schema drift reaches production with sqldef

Compare checked-in SQL against live MySQL, PostgreSQL, SQLite, or SQL Server schemas and generate a reviewable apply plan before agents touch production databases.

## Prerequisites

Go-built sqldef binary and access to a supported relational database

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the sqldef binary for your platform from the project releases or package manager, prepare declarative SQL files for the target database, then run the matching tool such as `psqldef`, `mysqldef`, or `sqlite3def` against a live database to review and apply the diff.
```

## Documentation

- https://github.com/sqldef/sqldef

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef/)
