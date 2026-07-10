---
title: "Run durable scheduled agent jobs in Node.js with Agenda"
description: "Use Agenda when a custom Node.js agent needs persistent scheduled jobs, retries, locking, and background workers backed by MongoDB, PostgreSQL, or Redis instead of fragile in-process timers."
verification: "security_reviewed"
source: "https://github.com/agenda/agenda"
author: "Agenda"
publisher_type: "open_source_collective"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "agenda/agenda"
  github_stars: 9677
  npm_package: "agenda"
  npm_weekly_downloads: 167228
---

# Run durable scheduled agent jobs in Node.js with Agenda

Use Agenda when a custom Node.js agent needs persistent scheduled jobs, retries, locking, and background workers backed by MongoDB, PostgreSQL, or Redis instead of fragile in-process timers.

## Prerequisites

Node.js, the agenda npm package, and a supported persistence backend such as MongoDB, PostgreSQL, or Redis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Agenda with npm install agenda, then install one backend package such as @agendajs/mongo-backend, @agendajs/postgres-backend, or @agendajs/redis-backend. Define named jobs in the Node.js worker, connect the backend, call agenda.start(), and schedule one-off or recurring agent tasks with Agenda's job APIs.
```

## Documentation

- https://agenda.github.io/agenda/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-durable-scheduled-agent-jobs-in-node-js-with-agenda/)
