---
name: "Run durable Node agent jobs without Redis using Sidequest"
slug: "run-durable-node-agent-jobs-without-redis-using-sidequest"
description: "Use Sidequest to run durable Node.js agent jobs, retries, cron schedules, and queue dashboards on PostgreSQL, MySQL, SQLite, or MongoDB without adding Redis."
github_stars: 1015
verification: "security_reviewed"
source: "https://github.com/sidequestjs/sidequest"
author: "Sidequest.js maintainers"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sidequestjs/sidequest"
  github_stars: 1015
  npm_package: "sidequest"
  npm_weekly_downloads: 7098
---

# Run durable Node agent jobs without Redis using Sidequest

Use Sidequest to run durable Node.js agent jobs, retries, cron schedules, and queue dashboards on PostgreSQL, MySQL, SQLite, or MongoDB without adding Redis.

## Prerequisites

Node.js 22.6 or newer, the sidequest npm package, a supported database backend package, and optionally the built-in dashboard.

## Installation

Install or set up from the source-backed instructions:

Install the core package with npm install sidequest, then install the backend driver for the database you will use, such as npm install @sidequest/postgres-backend. Start Sidequest in your Node.js process with the backend configuration, define job classes, and enqueue work with Sidequest.build(JobClass).enqueue(...).

- Source: https://github.com/sidequestjs/sidequest

## Documentation

- https://docs.sidequestjs.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-durable-node-agent-jobs-without-redis-using-sidequest/)
