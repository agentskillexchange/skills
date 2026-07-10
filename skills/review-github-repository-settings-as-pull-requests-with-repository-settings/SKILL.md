---
title: "Review GitHub repository settings as pull requests with repository-settings"
description: "Use repository-settings when an operator wants GitHub repository configuration changes reviewed as code before branch protection, labels, teams, or other settings are applied."
verification: "security_reviewed"
source: "https://github.com/repository-settings/app"
author: "repository-settings"
publisher_type: "open_source"
category:
  - "Code Quality & Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "repository-settings/app"
  github_stars: 1043
  npm_package: "@repository-settings/app"
  npm_weekly_downloads: 0
---

# Review GitHub repository settings as pull requests with repository-settings

Use repository-settings when an operator wants GitHub repository configuration changes reviewed as code before branch protection, labels, teams, or other settings are applied.

## Prerequisites

GitHub App installation, .github/settings.yml, GitHub pull request review workflow

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the hosted GitHub App from https://github.com/apps/settings or self-host from https://github.com/repository-settings/app, then define repository settings in .github/settings.yml and review changes through pull requests before merging.
```

## Documentation

- https://github.com/apps/settings

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-github-repository-settings-as-pull-requests-with-repository-settings/)
