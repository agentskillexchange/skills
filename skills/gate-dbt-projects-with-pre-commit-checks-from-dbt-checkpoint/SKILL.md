---
title: "Gate dbt projects with pre-commit checks from dbt-checkpoint"
description: "Use dbt-checkpoint when an agent should catch dbt naming, dependency, metadata, and model-hygiene issues before review or merge."
verification: "listed"
source: "https://github.com/dbt-checkpoint/dbt-checkpoint"
author: "dbt-checkpoint"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "dbt-checkpoint/dbt-checkpoint"
  github_stars: 738
---

# Gate dbt projects with pre-commit checks from dbt-checkpoint

Use dbt-checkpoint when an agent should catch dbt naming, dependency, metadata, and model-hygiene issues before review or merge.

## Prerequisites

Python, pre-commit, dbt project files, and dbt-checkpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install dbt-checkpoint`, add the documented hooks to `.pre-commit-config.yaml`, and run them locally or in CI before dbt changes merge.
```

## Documentation

- https://github.com/dbt-checkpoint/dbt-checkpoint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-dbt-projects-with-pre-commit-checks-from-dbt-checkpoint/)
