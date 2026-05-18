---
name: "GitHub Actions Matrix Build Optimizer"
slug: "github-actions-matrix-build-optimizer"
description: "Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
author: "GitHub"
category: "CI/CD Integrations"
framework: "Claude Code"
---

# GitHub Actions Matrix Build Optimizer

Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit.

## Prerequisites

GitHub repository with Actions enabled

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a workflow file under .github/workflows/ in your repository, then configure triggers, jobs, and runners according to the GitHub Actions documentation.
```

## Documentation

- https://docs.github.com/en/actions

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/)
