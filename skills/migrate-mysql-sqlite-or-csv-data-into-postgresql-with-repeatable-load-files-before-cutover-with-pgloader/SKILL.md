---
title: "Migrate MySQL, SQLite, or CSV data into PostgreSQL with repeatable load files before cutover with pgloader"
slug: "migrate-mysql-sqlite-or-csv-data-into-postgresql-with-repeatable-load-files-before-cutover-with-pgloader"
description: "Move data into PostgreSQL with declarative load files, built-in type conversion, and repeatable migration runs before one-off import scripts become cutover risk."
github_stars: 6393
verification: "security_reviewed"
source: "https://github.com/dimitri/pgloader"
author: "Dimitri Fontaine"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dimitri/pgloader"
  github_stars: 6393
---

# Migrate MySQL, SQLite, or CSV data into PostgreSQL with repeatable load files before cutover with pgloader

Move data into PostgreSQL with declarative load files, built-in type conversion, and repeatable migration runs before one-off import scripts become cutover risk.

## Prerequisites

pgloader and access to source systems plus a PostgreSQL target

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pgloader from your package manager or build instructions, create a `.load` file describing the source and PostgreSQL target, then run `pgloader your-migration.load` to execute and iterate on the migration.
```

## Documentation

- https://pgloader.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/migrate-mysql-sqlite-or-csv-data-into-postgresql-with-repeatable-load-files-before-cutover-with-pgloader/)
