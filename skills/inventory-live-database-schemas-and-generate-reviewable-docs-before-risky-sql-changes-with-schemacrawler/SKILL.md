---
title: "Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler"
description: "Lets an agent crawl a live database and produce schema inventories, dependency views, and reviewable documentation before migrations or handoffs."
verification: "listed"
source: "https://github.com/schemacrawler/SchemaCrawler"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "schemacrawler/SchemaCrawler"
  github_stars: 1801
---

# Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler

Use SchemaCrawler when an agent needs a trustworthy picture of a live database before migration, cleanup, documentation, or governance work begins. It fits situations where the problem is incomplete schema understanding, not general database administration.

Invoke this instead of using the database product normally when the agent must extract a structural inventory, map dependencies, and generate reviewable docs from the live schema. This is skill-shaped because the job boundary is narrow: schema discovery and documentation. It is not a generic SQL client, database server, or broad data platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler/)
