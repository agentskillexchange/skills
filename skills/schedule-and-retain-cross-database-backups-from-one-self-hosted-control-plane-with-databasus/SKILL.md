---
title: "Schedule and retain cross-database backups from one self-hosted control plane with Databasus"
description: "Run scheduled backups with retention rules and storage targets across PostgreSQL, MySQL, MariaDB, and MongoDB from one place."
verification: "listed"
source: "https://github.com/databasus/databasus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "databasus/databasus"
  github_stars: 6581
---

# Schedule and retain cross-database backups from one self-hosted control plane with Databasus

Use Databasus when an agent needs to operate recurring database backup jobs across multiple engines and storage backends from one self-hosted system. This should be invoked instead of manually stitching together per-database backup commands when the real task is scheduled backup orchestration, retention handling, and destination management. That scope boundary—multi-database backup operations with schedules, retention, storage, and notifications—keeps it from being just a generic database product card or a plain database client listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus/)
