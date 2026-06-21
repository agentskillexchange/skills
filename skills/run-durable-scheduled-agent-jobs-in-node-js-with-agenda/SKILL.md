---
name: "Run durable scheduled agent jobs in Node.js with Agenda"
slug: "run-durable-scheduled-agent-jobs-in-node-js-with-agenda"
description: "Use Agenda when a custom Node.js agent needs persistent scheduled jobs, retries, locking, and background workers backed by MongoDB, PostgreSQL, or Redis instead of fragile in-process timers."
github_stars: 9677
verification: "security_reviewed"
source: "https://github.com/agenda/agenda"
author: "Agenda"
publisher_type: "open_source_collective"
category: "Templates & Workflows"
framework: "Custom Agents"
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

Use the upstream install or setup path that matches your environment:
- npm install agenda
- npm install @agendajs/mongo-backend
- npm install @agendajs/postgres-backend
- npm install @agendajs/redis-backend

Requirements and caveats from upstream:
- A light-weight job scheduling library for Node.js
- **ESM-only** - Modern ES modules (Node.js 18+)
- If your MongoDB deployment is a replica set (even a single-node replica set works), you can use MongoChangeStreamNotificationChannel for native real-time notifications without any external dependencies:

Basic usage or getting-started notes:
- **For MongoDB:** Install the official MongoDB backend:
- You will need a working [MongoDB](https://www.mongodb.com/) database (v4+).
- **For PostgreSQL:** Install the official PostgreSQL backend:

- Source: https://github.com/agenda/agenda
- Extracted from upstream docs: https://raw.githubusercontent.com/agenda/agenda/HEAD/README.md

## Documentation

- https://agenda.github.io/agenda/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-durable-scheduled-agent-jobs-in-node-js-with-agenda/)
