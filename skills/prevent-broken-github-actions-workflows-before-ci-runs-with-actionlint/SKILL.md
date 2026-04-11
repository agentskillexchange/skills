---
title: "Prevent broken GitHub Actions workflows before CI runs with actionlint"
description: "Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time."
verification: "listed"
source: "https://github.com/rhysd/actionlint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rhysd/actionlint"
  github_stars: 3779
---

# Prevent broken GitHub Actions workflows before CI runs with actionlint

Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/)
