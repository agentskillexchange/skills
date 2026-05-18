---
name: "Turn PostgreSQL logs into incident and tuning reports with pgBadger"
slug: "turn-postgresql-logs-into-incident-and-tuning-reports-with-pgbadger"
description: "Use pgBadger when an agent needs to convert raw PostgreSQL logs into readable evidence about slow queries, errors, and workload hotspots after an incident."
github_stars: 3994
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- make && sudo make install

Requirements and caveats from upstream:
- Requires incremental output directories and the
- month. Requires incremental output directories and
- You must enable and set some configuration directives in your postgresql.conf

Basic usage or getting-started notes:
- PostgreSQL log analyzer with fully detailed reports and graphs.
- Arguments:
- logfile can be a single log file, a list of files, or a shell command

- Source: https://github.com/darold/pgbadger
- Extracted from upstream docs: https://raw.githubusercontent.com/darold/pgbadger/HEAD/README.md

## Documentation

- https://pgbadger.darold.net/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-postgresql-logs-into-incident-and-tuning-reports-with-pgbadger/)
