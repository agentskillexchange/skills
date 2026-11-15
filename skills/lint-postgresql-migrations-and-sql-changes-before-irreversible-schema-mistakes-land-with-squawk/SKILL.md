---
name: "Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk"
slug: "lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk"
description: "Catch locking, indexing, and schema-change hazards in PostgreSQL migration SQL before a review turns into downtime."
github_stars: 1050
verification: "security_reviewed"
source: "https://github.com/sbdchd/squawk"
author: "sbdchd"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sbdchd/squawk"
  github_stars: 1050
---

# Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk

Catch locking, indexing, and schema-change hazards in PostgreSQL migration SQL before a review turns into downtime.

## Prerequisites

Squawk CLI or container image, PostgreSQL migration SQL files, and optional CI or pre-commit integration.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g squawk-cli
- pip install squawk-cli
- docker run --rm -v $(pwd):/data ghcr.io/sbdchd/squawk:latest *.sql
- cargo install

Requirements and caveats from upstream:
- ### Or via Docker
- You can also run Squawk using Docker. The official image is available on GitHub Container Registry.
- warning[prefer-text-field]: Changing the size of a varchar field requires an ACCESS EXCLUSIVE lock, that will prevent all reads and writes to the table.

Basic usage or getting-started notes:
- [Quick Start](https://squawkhq.com/docs/) | [Playground](https://play.squawkhq.com) | [Rules Documentation](https://squawkhq.com/docs/rules) | [GitHub Action](https://github.com/sbdchd/squawk-action) | [DIY GitHub Int...
- shell
- # or via PYPI

- Source: https://github.com/sbdchd/squawk
- Extracted from upstream docs: https://raw.githubusercontent.com/sbdchd/squawk/HEAD/README.md

## Documentation

- https://squawkhq.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/)
