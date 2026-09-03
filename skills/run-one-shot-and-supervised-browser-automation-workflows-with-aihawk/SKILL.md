---
name: "Run one-shot and supervised browser automation workflows with AIHawk"
slug: "run-one-shot-and-supervised-browser-automation-workflows-with-aihawk"
description: "Use AIHawk when an agent needs a real browser for bounded web research, extraction, and task execution with visible UI or one-shot command output."
github_stars: 30305
verification: "security_reviewed"
source: "https://github.com/feder-cr/AIHawk"
author: "feder-cr"
publisher_type: "individual"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "feder-cr/AIHawk"
  github_stars: 30305
---

# Run one-shot and supervised browser automation workflows with AIHawk

Use AIHawk when an agent needs a real browser for bounded web research, extraction, and task execution with visible UI or one-shot command output.

## Prerequisites

Python 3.11+, uv/uvx, AIHawk, OpenRouter API key for model-backed runs, local browser storage, optional proxy or persistent profile directory

## Installation

Install or set up from the source-backed instructions:

Install uv, then run `uvx aihawk ui --openrouter-key sk-or-...` and open `http://127.0.0.1:8765` for supervised work, or run `uvx aihawk do "Open and ..." --openrouter-key sk-or-...` for one-shot automation. Use the documented `--proxy`, `--seed`, and `--profile-dir` options when a repeatable browser identity or persistent login state is required.

- Source: https://github.com/feder-cr/AIHawk

## Documentation

- https://github.com/feder-cr/AIHawk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-one-shot-and-supervised-browser-automation-workflows-with-aihawk/)
