---
title: "GitHub Actions CI Builder"
description: "Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
author: "GitHub"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
---

# GitHub Actions CI Builder

Generate and manage GitHub Actions workflow YAML files using the GitHub Actions REST API and workflow_dispatch events. Supports matrix builds, reusable workflows, and composite actions.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-ci-builder/)
