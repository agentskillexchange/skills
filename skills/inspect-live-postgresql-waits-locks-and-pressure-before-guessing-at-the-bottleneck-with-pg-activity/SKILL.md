---
title: "Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity"
slug: "inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity"
description: "Open a live PostgreSQL activity view during incidents so you can see sessions, waits, locks, and pressure before making a bad call."
github_stars: 3010
verification: "security_reviewed"
source: "https://github.com/dalibo/pg_activity"
author: "DALIBO"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dalibo/pg_activity"
  github_stars: 3010
  npm_package: "pg_activity"
  npm_weekly_downloads: 20770
---

# Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity

Open a live PostgreSQL activity view during incidents so you can see sessions, waits, locks, and pressure before making a bad call.

## Prerequisites

PostgreSQL connection access, pg_activity installation, terminal access to the target environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pg_activity from distribution packages, pip, or pipx as documented upstream, provide credentials for the target PostgreSQL instance, then run pg_activity against the live server during diagnosis.
```

## Documentation

- https://github.com/dalibo/pg_activity

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity/)
