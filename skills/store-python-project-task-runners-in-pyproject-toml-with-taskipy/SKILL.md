---
title: "Store Python project task runners in pyproject.toml with taskipy"
description: "Define short Python project commands in pyproject.toml so agents and maintainers can run the same test, lint, docs, and release tasks without hunting through shell notes."
verification: "security_reviewed"
source: "https://github.com/taskipy/taskipy"
author: "taskipy"
publisher_type: "community"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "taskipy/taskipy"
  github_stars: 714
---

# Store Python project task runners in pyproject.toml with taskipy

Define short Python project commands in pyproject.toml so agents and maintainers can run the same test, lint, docs, and release tasks without hunting through shell notes.

## Prerequisites

Python, pip or Poetry, pyproject.toml

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install taskipy or add it through the project's Python package manager, define tasks under [tool.taskipy.tasks] in pyproject.toml, then run them with task <name> or poetry run task <name>.
```

## Documentation

- https://github.com/taskipy/taskipy

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/store-python-project-task-runners-in-pyproject-toml-with-taskipy/)
