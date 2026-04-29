---
title: "Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest"
description: "Execute PostgreSQL backup, restore, verification, and point-in-time recovery runbooks with explicit repository and WAL handling."
verification: "listed"
source: "https://github.com/pgbackrest/pgbackrest"
author: "pgbackrest"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pgbackrest/pgbackrest"
  github_stars: 3729
---

# Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest

Execute PostgreSQL backup, restore, verification, and point-in-time recovery runbooks with explicit repository and WAL handling.

## Prerequisites

pgBackRest installation, PostgreSQL server access, configured backup repository storage, credentials and retention settings for the target environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pgBackRest from the upstream packages or build instructions, configure a stanza and repository for the target PostgreSQL cluster, then use the documented backup, check, restore, and WAL recovery commands for the intended runbook.
```

## Documentation

- https://pgbackrest.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest/)
