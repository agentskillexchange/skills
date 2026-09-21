---
name: "Run transactional Go and Postgres agent job queues with River"
slug: "run-transactional-go-postgres-agent-job-queues-with-river"
description: "Use River to keep Go-based agent jobs transactional with Postgres so queued work commits or rolls back with the application state that created it."
github_stars: 5699
verification: "security_reviewed"
source: "https://github.com/riverqueue/river"
author: "River Queue"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "riverqueue/river"
  github_stars: 5699
---

# Run transactional Go and Postgres agent job queues with River

Use River to keep Go-based agent jobs transactional with Postgres so queued work commits or rolls back with the application state that created it.

## Prerequisites

Go application, PostgreSQL, River Go modules, pgx-compatible database pool, optional River UI

## Installation

Install or set up from the source-backed instructions:

Add River to the Go service, create typed `JobArgs` and `Worker` implementations, register workers with `river.NewWorkers()` and `river.AddWorker`, start a `river.Client` with a Postgres driver and queue config, then enqueue jobs inside application transactions where consistency matters.

- Source: https://github.com/riverqueue/river

## Documentation

- https://riverqueue.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-transactional-go-postgres-agent-job-queues-with-river/)
