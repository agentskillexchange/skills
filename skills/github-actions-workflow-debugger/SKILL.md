---
name: "GitHub Actions Workflow Debugger"
slug: "github-actions-workflow-debugger"
description: "Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
author: "GitHub"
category: "CI/CD Integrations"
framework: "Claude Agents"
---

# GitHub Actions Workflow Debugger

Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-debugger/)
