---
title: "Run durable Python agent schedules with APScheduler"
description: "Schedule recurring, interval, calendar, and one-off Python agent jobs with persistent job stores so background workflows survive restarts."
verification: "security_reviewed"
source: "https://github.com/agronholm/apscheduler"
author: "agronholm"
publisher_type: "individual"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "agronholm/apscheduler"
  github_stars: 7547
---

# Run durable Python agent schedules with APScheduler

Schedule recurring, interval, calendar, and one-off Python agent jobs with persistent job stores so background workflows survive restarts.

## Prerequisites

Python, APScheduler, optional persistent data store such as PostgreSQL, MySQL, SQLite, MongoDB, Redis, MQTT, or a Python web service runtime

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install APScheduler in the Python environment, define task functions, configure a scheduler with cron, interval, calendar, or date triggers, add a persistent job store when jobs must survive restarts, then run the scheduler or worker process with the agent service.
```

## Documentation

- https://apscheduler.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-durable-python-agent-schedules-with-apscheduler/)
