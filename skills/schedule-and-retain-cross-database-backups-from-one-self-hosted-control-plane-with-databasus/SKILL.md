---
title: "Schedule and retain cross-database backups from one self-hosted control plane with Databasus"
slug: "schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus"
description: "Run scheduled backups with retention rules and storage targets across PostgreSQL, MySQL, MariaDB, and MongoDB from one place."
github_stars: 6581
verification: "security_reviewed"
source: "https://github.com/databasus/databasus"
author: "databasus"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "databasus/databasus"
  github_stars: 6581
---

# Schedule and retain cross-database backups from one self-hosted control plane with Databasus

Run scheduled backups with retention rules and storage targets across PostgreSQL, MySQL, MariaDB, and MongoDB from one place.

## Prerequisites

Databasus deployment, access to supported databases, configured storage destination, backup credentials, optional notification integrations

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Deploy Databasus using its documented install script, Docker, or compose path, connect the target databases and storage backends, then configure schedules, retention, and notifications for the backup jobs you want it to run.
```

## Documentation

- https://databasus.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus/)
