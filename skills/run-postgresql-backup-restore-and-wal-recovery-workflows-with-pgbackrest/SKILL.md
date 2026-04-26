---
title: "Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest"
description: "Execute PostgreSQL backup, restore, verification, and point-in-time recovery runbooks with explicit repository and WAL handling."
verification: "listed"
source: "https://github.com/pgbackrest/pgbackrest"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pgbackrest/pgbackrest"
  github_stars: 3729
---

# Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest

Use pgBackRest when an agent needs to run or verify PostgreSQL backup and recovery procedures, including restore testing and WAL-based point in time recovery, instead of treating Postgres as a general database product. A user should invoke this instead of normal database use when the job is operational protection and recovery, not query execution or application development. The scope boundary is tight and skill-shaped: PostgreSQL backup, restore, retention, and recovery runbooks, not a plain database or backup platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest/)
