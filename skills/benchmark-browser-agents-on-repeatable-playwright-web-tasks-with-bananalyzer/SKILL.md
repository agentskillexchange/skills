---
title: "Benchmark browser agents on repeatable Playwright web tasks with Bananalyzer"
description: "Run a repeatable evaluation suite for browser agents against static web task snapshots instead of judging them from demos or one-off tests."
verification: "listed"
source: "https://github.com/reworkd/bananalyzer"
author: "Reworkd"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "reworkd/bananalyzer"
  github_stars: 327
---

# Benchmark browser agents on repeatable Playwright web tasks with Bananalyzer

Run a repeatable evaluation suite for browser agents against static web task snapshots instead of judging them from demos or one-off tests.

## Prerequisites

Python environment, Playwright browser runtime, pytest-based test execution, a custom AgentRunner implementation, example web task snapshots

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the project dependencies, create a test file that implements the `AgentRunner` interface, then run `bananalyze` against that file or test directory to execute the evaluation suite.
```

## Documentation

- https://github.com/reworkd/bananalyzer

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-browser-agents-on-repeatable-playwright-web-tasks-with-bananalyzer/)
