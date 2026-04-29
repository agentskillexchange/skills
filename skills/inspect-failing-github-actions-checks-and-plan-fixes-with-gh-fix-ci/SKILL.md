---
title: "Inspect failing GitHub Actions checks and plan fixes with gh-fix-ci"
description: "Inspect failing GitHub Actions checks on the current PR, pull the actionable log snippet, and stop at an approval gate before implementing a fix."
verification: "listed"
source: "https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci"
author: "OpenAI"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
---

# Inspect failing GitHub Actions checks and plan fixes with gh-fix-ci

Inspect failing GitHub Actions checks on the current PR, pull the actionable log snippet, and stop at an approval gate before implementing a fix.

## Prerequisites

Codex, GitHub CLI (gh), repository with an open PR, GitHub auth with repo/workflow scopes

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the curated gh-fix-ci skill from the openai/skills catalog, make sure `gh auth status` succeeds with repo and workflow scopes, then run it inside the target repository so it can inspect the current PR's failing checks and logs.
```

## Documentation

- https://raw.githubusercontent.com/openai/skills/main/skills/.curated/gh-fix-ci/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-failing-github-actions-checks-and-plan-fixes-with-gh-fix-ci/)
