---
title: "Turn PostgreSQL logs into incident and tuning reports with pgBadger"
slug: "turn-postgresql-logs-into-incident-and-tuning-reports-with-pgbadger"
description: "Use pgBadger when an agent needs to convert raw PostgreSQL logs into readable evidence about slow queries, errors, and workload hotspots after an incident."
github_stars: 3994
verification: "security_reviewed"
source: "https://github.com/darold/pgbadger"
author: "darold"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "darold/pgbadger"
  github_stars: 3994
---

# Turn PostgreSQL logs into incident and tuning reports with pgBadger

Use pgBadger when an agent needs to convert raw PostgreSQL logs into readable evidence about slow queries, errors, and workload hotspots after an incident.

## Prerequisites

pgBadger, PostgreSQL logs with compatible log settings, and a shell environment for report generation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pgBadger from your package manager or source, point it at PostgreSQL log files, and generate HTML or text reports during incident review or tuning sessions.
```

## Documentation

- https://pgbadger.darold.net/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-postgresql-logs-into-incident-and-tuning-reports-with-pgbadger/)
