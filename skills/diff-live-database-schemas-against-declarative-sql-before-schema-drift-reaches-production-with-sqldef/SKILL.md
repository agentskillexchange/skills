---
title: "Diff live database schemas against declarative SQL before schema drift reaches production with sqldef"
description: "Use sqldef when an agent needs to reconcile a live database with declarative SQL files, review the generated diff, and apply schema changes in a controlled way. Invoke it instead of doing manual DDL or ad hoc database admin work when the real job is drift detection and schema alignment from checked-in SQL. The scope boundary is narrow and skill-shaped: schema diff and apply for supported relational databases, not general querying, ORM migration authoring, or a generic database product listing."
source: "https://github.com/sqldef/sqldef"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sqldef/sqldef"
  github_stars: 3076
---

# Diff live database schemas against declarative SQL before schema drift reaches production with sqldef

Use sqldef when an agent needs to reconcile a live database with declarative SQL files, review the generated diff, and apply schema changes in a controlled way. Invoke it instead of doing manual DDL or ad hoc database admin work when the real job is drift detection and schema alignment from checked-in SQL. The scope boundary is narrow and skill-shaped: schema diff and apply for supported relational databases, not general querying, ORM migration authoring, or a generic database product listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef/)
