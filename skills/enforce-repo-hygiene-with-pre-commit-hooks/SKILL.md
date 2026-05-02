---
title: "Enforce repo hygiene with pre-commit hooks"
description: "Run a repeatable pre-commit gate that catches formatting, lint, secret, and policy issues before they land in the repo."
verification: "security_reviewed"
source: "https://github.com/pre-commit/pre-commit"
author: "pre-commit maintainers"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pre-commit/pre-commit"
  github_stars: 15163
---

# Enforce repo hygiene with pre-commit hooks

Run a repeatable pre-commit gate that catches formatting, lint, secret, and policy issues before they land in the repo.

## Prerequisites

pre-commit

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pre-commit, add a .pre-commit-config.yaml file, then run `pre-commit install` and `pre-commit run --all-files`.
```

## Documentation

- https://pre-commit.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-repo-hygiene-with-pre-commit-hooks/)
