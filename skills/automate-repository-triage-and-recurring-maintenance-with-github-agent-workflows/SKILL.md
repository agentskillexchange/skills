---
title: "Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows"
description: "Use GitHub Agentic Workflows to let an agent triage issues, inspect CI failures, or deliver scheduled repository upkeep inside GitHub Actions with explicit workflow definitions and reviewable runs. This is for bounded, repeatable repository operations, not for listing GitHub as a general coding platform."
verification: "security_reviewed"
source: "https://github.com/github/gh-aw"
author: "GitHub"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/gh-aw"
  github_stars: 4286
---

# Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows

Use GitHub Agentic Workflows to let an agent triage issues, inspect CI failures, or deliver scheduled repository upkeep inside GitHub Actions with explicit workflow definitions and reviewable runs. This is for bounded, repeatable repository operations, not for listing GitHub as a general coding platform.

## Prerequisites

GitHub Actions, gh CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the gh-aw GitHub CLI extension, initialize agentic workflows in a repository, define workflow markdown files, then compile and run them through GitHub Actions.
```

## Documentation

- https://github.github.com/gh-aw/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automate-repository-triage-and-recurring-maintenance-with-github-agent-workflows/)
