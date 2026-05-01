---
title: "Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema"
description: "Pull live MySQL schema into files, inspect diffs, and push reviewed changes back with a repeatable workflow."
verification: "listed"
source: "https://github.com/skeema/skeema"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "skeema/skeema"
  github_stars: 1361
---

# Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema

Use Skeema when an agent needs to manage MySQL or MariaDB schema as reviewable files, compare intended changes against live databases, and stage safe deploys. A user should invoke this instead of using the database normally when the task is schema pull, diff, lint, and controlled push, not ad hoc querying or generic administration. The scope boundary is crisp and skill-shaped: filesystem-backed schema change review and deployment for MySQL-family databases, not a plain database product or migration framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema/)
