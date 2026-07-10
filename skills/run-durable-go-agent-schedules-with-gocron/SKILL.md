---
title: "Run durable Go agent schedules with gocron"
description: "Embed gocron in Go-based agents or operators to run recurring tasks, cron expressions, one-time jobs, singleton executions, concurrency limits, and distributed leader-elected schedules."
verification: "security_reviewed"
source: "https://github.com/go-co-op/gocron"
author: "go-co-op"
publisher_type: "open_source"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "go-co-op/gocron"
  github_stars: 7079
---

# Run durable Go agent schedules with gocron

Embed gocron in Go-based agents or operators to run recurring tasks, cron expressions, one-time jobs, singleton executions, concurrency limits, and distributed leader-elected schedules.

## Prerequisites

Go 1.x project using github.com/go-co-op/gocron/v2

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run `go get github.com/go-co-op/gocron/v2`, create a scheduler in the Go agent or worker process, register jobs with the documented job types and concurrency options, and bind scheduler start/shutdown to the service lifecycle.
```

## Documentation

- https://pkg.go.dev/github.com/go-co-op/gocron/v2

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-durable-go-agent-schedules-with-gocron/)
