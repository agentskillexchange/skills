---
title: "PostgreSQL Slow Query Runbook"
slug: "postgresql-slow-query-runbook-agent"
description: "Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
