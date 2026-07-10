---
title: "Generate and validate conventional commits and semver release bumps with Commitizen"
description: "Standardize commit messages, validate commit history, and calculate semver-aware release bumps without hand-rolled repo rules."
verification: "listed"
source: "https://github.com/commitizen-tools/commitizen"
author: "commitizen-tools"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "commitizen-tools/commitizen"
  github_stars: 3382
---

# Generate and validate conventional commits and semver release bumps with Commitizen

Standardize commit messages, validate commit history, and calculate semver-aware release bumps without hand-rolled repo rules.

## Prerequisites

Git, Python 3.9+, and the Commitizen CLI in a repository with a defined commit convention.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install -U commitizen or your preferred Python environment manager, add Commitizen configuration in pyproject.toml, .cz.toml, or equivalent, then run commands such as cz commit, cz check, and cz bump inside the target repository.
```

## Documentation

- https://commitizen-tools.github.io/commitizen/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-validate-conventional-commits-and-semver-release-bumps-with-commitizen/)
