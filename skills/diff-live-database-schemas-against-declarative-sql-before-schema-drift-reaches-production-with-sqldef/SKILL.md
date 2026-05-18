---
name: "Diff live database schemas against declarative SQL before schema drift reaches production with sqldef"
slug: "diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef"
description: "Compare checked-in SQL against live MySQL, PostgreSQL, SQLite, or SQL Server schemas and generate a reviewable apply plan before agents touch production databases."
github_stars: 3076
verification: "listed"
source: "https://github.com/sqldef/sqldef"
author: "sqldef"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sqldef/sqldef"
  github_stars: 3076
---

# Diff live database schemas against declarative SQL before schema drift reaches production with sqldef

Compare checked-in SQL against live MySQL, PostgreSQL, SQLite, or SQL Server schemas and generate a reviewable apply plan before agents touch production databases.

## Prerequisites

Go-built sqldef binary and access to a supported relational database

## Installation

Use the upstream install or setup path that matches your environment:
- Docker images are available on Docker Hub:
- brew install sqldef/sqldef/mysqldef
- brew install sqldef/sqldef/psqldef
- brew install sqldef/sqldef/sqlite3def

Requirements and caveats from upstream:
- ### Docker images
- https://hub.docker.com/u/sqldef
- Debian packages are not currently available. Use the pre-built binaries or Docker images instead.

Basic usage or getting-started notes:
- Each database gets its own command (mysqldef, psqldef, sqlite3def, mssqldef) that mimics the connection options of the native database client, making it familiar and easy to integrate into existing workflows. The tool...
- ### Basic Workflow
- This is the basic workflow, which is identical across all databases - only the connection options differ between commands.

- Source: https://github.com/sqldef/sqldef
- Extracted from upstream docs: https://raw.githubusercontent.com/sqldef/sqldef/HEAD/README.md

## Documentation

- https://github.com/sqldef/sqldef

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef/)
