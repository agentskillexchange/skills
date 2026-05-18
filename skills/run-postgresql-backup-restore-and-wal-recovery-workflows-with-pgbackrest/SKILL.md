---
name: "Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest"
slug: "run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest"
description: "Execute PostgreSQL backup, restore, verification, and point-in-time recovery runbooks with explicit repository and WAL handling."
github_stars: 3729
verification: "listed"
source: "https://github.com/pgbackrest/pgbackrest"
author: "pgbackrest"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pgbackrest/pgbackrest"
  github_stars: 3729
---

# Run PostgreSQL backup restore and WAL recovery workflows with pgBackRest

Execute PostgreSQL backup, restore, verification, and point-in-time recovery runbooks with explicit repository and WAL handling.

## Prerequisites

pgBackRest installation, PostgreSQL server access, configured backup repository storage, credentials and retention settings for the target environment

## Installation

Basic usage or getting-started notes:
- Multiple repositories allow, for example, a local repository with minimal retention for fast restores and a remote repository with a longer retention for redundancy and access across the enterprise.
- Dedicated commands are included for pushing WAL to the archive and getting WAL from the archive. Both commands support parallelism to accelerate processing and run asynchronously to provide the fastest possible respon...
- pgBackRest strives to be easy to configure and operate:

- Source: https://github.com/pgbackrest/pgbackrest
- Extracted from upstream docs: https://raw.githubusercontent.com/pgbackrest/pgbackrest/HEAD/README.md

## Documentation

- https://pgbackrest.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-postgresql-backup-restore-and-wal-recovery-workflows-with-pgbackrest/)
