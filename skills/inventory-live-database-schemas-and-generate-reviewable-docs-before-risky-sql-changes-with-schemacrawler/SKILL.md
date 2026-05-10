---
title: "Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler"
slug: "inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler"
description: "Lets an agent crawl a live database and produce schema inventories, dependency views, and reviewable documentation before migrations or handoffs."
github_stars: 1801
verification: "security_reviewed"
source: "https://github.com/schemacrawler/SchemaCrawler"
author: "SchemaCrawler"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "schemacrawler/SchemaCrawler"
  github_stars: 1801
---

# Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler

Lets an agent crawl a live database and produce schema inventories, dependency views, and reviewable documentation before migrations or handoffs.

## Prerequisites

Java, JDBC driver for target database, SchemaCrawler CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the SchemaCrawler CLI, then run it with the correct JDBC driver for the target database.
```

## Documentation

- https://www.schemacrawler.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler/)
