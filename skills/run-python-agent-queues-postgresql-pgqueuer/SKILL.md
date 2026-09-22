---
name: "Run Python Agent Queues on PostgreSQL with PgQueuer"
slug: "run-python-agent-queues-postgresql-pgqueuer"
description: "Use PgQueuer to run Python agent background jobs from PostgreSQL with transactional enqueue, SKIP LOCKED concurrency, LISTEN/NOTIFY dispatch, recurring schedules, metrics, and a dashboard."
github_stars: 1526
verification: "security_reviewed"
source: "https://github.com/janbjorge/pgqueuer"
author: "janbjorge"
publisher_type: "open-source"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "janbjorge/pgqueuer"
  github_stars: 1526
---

# Run Python Agent Queues on PostgreSQL with PgQueuer

Use PgQueuer to run Python agent background jobs from PostgreSQL with transactional enqueue, SKIP LOCKED concurrency, LISTEN/NOTIFY dispatch, recurring schedules, metrics, and a dashboard.

## Prerequisites

Python 3.10 or newer, PostgreSQL 13 or newer, pgqueuer package, asyncpg-compatible database connection

## Installation

Install or set up from the source-backed instructions:

Install with pip install pgqueuer, then run pgq install to create the database objects. Define PgQueuer entrypoint consumers and run them with pgq run module:function.

- Source: https://github.com/janbjorge/pgqueuer

## Documentation

- https://janbjorge.github.io/pgqueuer/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-python-agent-queues-postgresql-pgqueuer/)
