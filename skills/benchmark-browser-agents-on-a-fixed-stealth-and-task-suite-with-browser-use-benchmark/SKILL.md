---
title: "Benchmark browser agents on a fixed stealth and task suite with browser-use benchmark"
description: "Compare browser-agent reliability on a repeatable task and anti-bot suite before choosing a stack or claiming progress."
verification: "listed"
source: "https://github.com/browser-use/benchmark"
author: "browser-use"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "browser-use/benchmark"
  github_stars: 71
---

# Benchmark browser agents on a fixed stealth and task suite with browser-use benchmark

Compare browser-agent reliability on a repeatable task and anti-bot suite before choosing a stack or claiming progress.

## Prerequisites

Python, uv, benchmark repository dependencies, required API keys for the judge model and selected browser provider, target browser agent configuration

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the benchmark repository, install dependencies with the documented uv workflow, populate the required .env variables, then run the provided evaluation commands for the main browser task suite or the stealth benchmark against the browser provider you want to compare.
```

## Documentation

- https://github.com/browser-use/benchmark#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-browser-agents-on-a-fixed-stealth-and-task-suite-with-browser-use-benchmark/)
