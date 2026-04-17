---
title: "Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity"
description: "Open a live PostgreSQL activity view during incidents so you can see sessions, waits, locks, and pressure before making a bad call."
verification: listed
source: "https://github.com/dalibo/pg_activity"
category:
  - "Runbooks & Diagnostics"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity/)
