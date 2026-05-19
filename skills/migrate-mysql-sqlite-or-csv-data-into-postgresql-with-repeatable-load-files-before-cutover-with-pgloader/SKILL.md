---
name: "Migrate MySQL, SQLite, or CSV data into PostgreSQL with repeatable load files before cutover with pgloader"
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

Use the upstream install or setup path that matches your environment:
- $ docker pull ghcr.io/dimitri/pgloader:latest
- $ docker run --rm -it ghcr.io/dimitri/pgloader:latest pgloader --version

Requirements and caveats from upstream:
- If you're using docker, you can use the latest version built by the CI at

Basic usage or getting-started notes:
- pgloader also implements data reformatting, a typical example of that
- --help -h boolean Show usage and exit.
- --dry-run boolean Only check database connections, don't load anything.

- Source: https://github.com/dimitri/pgloader
- Extracted from upstream docs: https://raw.githubusercontent.com/dimitri/pgloader/HEAD/README.md

## Documentation

- https://pgloader.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/migrate-mysql-sqlite-or-csv-data-into-postgresql-with-repeatable-load-files-before-cutover-with-pgloader/)
