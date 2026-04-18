---
title: "Diff live database schemas against declarative SQL before schema drift reaches production with sqldef"
description: "Compare checked-in SQL against live MySQL, PostgreSQL, SQLite, or SQL Server schemas and generate a reviewable apply plan before agents touch production databases."
verification: listed
source: "https://github.com/sqldef/sqldef"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sqldef/sqldef"
  github_stars: 3076
---

# Diff live database schemas against declarative SQL before schema drift reaches production with sqldef

Use sqldef when an agent needs to reconcile a live database with declarative SQL files, review the generated diff, and apply schema changes in a controlled way. Invoke it instead of doing manual DDL or ad hoc database admin work when the real job is drift detection and schema alignment from checked-in SQL. The scope boundary is narrow and skill-shaped: schema diff and apply for supported relational databases, not general querying, ORM migration authoring, or a generic database product listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-live-database-schemas-against-declarative-sql-before-schema-drift-reaches-production-with-sqldef/)
