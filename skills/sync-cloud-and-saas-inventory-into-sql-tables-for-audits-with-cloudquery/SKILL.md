---
title: "Sync cloud and SaaS inventory into SQL tables for audits with CloudQuery"
description: "Extract cloud and SaaS configuration data into queryable tables so agents can run audits, drift checks, and evidence collection with SQL."
verification: "listed"
source: "https://github.com/cloudquery/cloudquery"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "cloudquery/cloudquery"
  github_stars: 6375
---

# Sync cloud and SaaS inventory into SQL tables for audits with CloudQuery

Use CloudQuery when an agent needs to pull infrastructure and SaaS inventory into structured tables for audit or drift analysis instead of navigating each provider console by hand. A user should invoke this instead of using the product normally when the task is repeatable inventory extraction into a destination database for SQL-driven review, not ordinary cloud administration. The scope boundary is specific and skill-shaped: source-backed inventory ETL for audits and evidence collection, not a generic cloud platform or SDK listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sync-cloud-and-saas-inventory-into-sql-tables-for-audits-with-cloudquery/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sync-cloud-and-saas-inventory-into-sql-tables-for-audits-with-cloudquery
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sync-cloud-and-saas-inventory-into-sql-tables-for-audits-with-cloudquery`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-cloud-and-saas-inventory-into-sql-tables-for-audits-with-cloudquery/)
