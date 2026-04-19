---
title: "Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity"
description: "Use pg_activity when an agent or operator needs a diagnose-now view of a running PostgreSQL instance rather than a general database client or monitoring platform. It is for checking active sessions, lock contention, waits, throughput, and resource pressure while an incident is happening. That scope boundary, live operational diagnosis for PostgreSQL workload pressure, keeps it skill-shaped instead of collapsing into a generic Postgres product card."
source: "https://github.com/dalibo/pg_activity"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dalibo/pg_activity"
  github_stars: 3010
  npm_package: "pg_activity"
  npm_weekly_downloads: 20770
---

# Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity

Use pg_activity when an agent or operator needs a diagnose-now view of a running PostgreSQL instance rather than a general database client or monitoring platform. It is for checking active sessions, lock contention, waits, throughput, and resource pressure while an incident is happening. That scope boundary, live operational diagnosis for PostgreSQL workload pressure, keeps it skill-shaped instead of collapsing into a generic Postgres product card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity/)
