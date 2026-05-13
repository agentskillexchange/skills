---
title: "PostgreSQL Performance Runbook"
slug: "postgresql-performance-runbook"
description: "Executes diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer statistics."
github_stars: 13127
verification: "security_reviewed"
source: "https://github.com/brianc/node-postgres"
category: "Runbooks & Diagnostics"
framework: "Codex"
tool_ecosystem:
  github_repo: "brianc/node-postgres"
  github_stars: 13127
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Performance Runbook

Executes diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer statistics.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-runbook/)
