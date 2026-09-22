---
name: "Schedule Postgres-backed agent maintenance chains with pg_timetable"
slug: "schedule-postgres-backed-agent-maintenance-chains-with-pg-timetable"
description: "Use pg_timetable to run database-driven schedules, SQL chains, system commands, missed-run recovery, concurrency limits, and YAML-defined maintenance workflows from PostgreSQL."
github_stars: 1400
verification: "security_reviewed"
source: "https://github.com/cybertec-postgresql/pg_timetable"
author: "CYBERTEC PostgreSQL International"
publisher_type: "company"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cybertec-postgresql/pg_timetable"
  github_stars: 1400
---

# Schedule Postgres-backed agent maintenance chains with pg_timetable

Use pg_timetable to run database-driven schedules, SQL chains, system commands, missed-run recovery, concurrency limits, and YAML-defined maintenance workflows from PostgreSQL.

## Prerequisites

PostgreSQL, pg_timetable binary or Docker image, a scheduler database role, and SQL or YAML chain definitions.

## Installation

Install or set up from the source-backed instructions:

Install pg_timetable from the official release packages, Docker image, or source build. Create a PostgreSQL role with the required database privileges, define jobs with timetable.add_job(...) or YAML chain files, then run pg_timetable postgresql://user:pass@host/db with any needed --file startup definitions.

- Source: https://github.com/cybertec-postgresql/pg_timetable

## Documentation

- https://cybertec-postgresql.github.io/pg_timetable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schedule-postgres-backed-agent-maintenance-chains-with-pg-timetable/)
