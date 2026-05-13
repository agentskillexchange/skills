---
title: "Audit GitHub Actions workflows for insecure permissions and unpinned actions"
slug: "audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions"
description: "This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation."
github_stars: 4145
verification: "security_reviewed"
source: "https://github.com/zizmorcore/zizmor"
author: "zizmorcore"
publisher_type: "Open Source Project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4145
---

# Audit GitHub Actions workflows for insecure permissions and unpinned actions

This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation.

## Prerequisites

GitHub Actions workflow files or a GitHub repository, with a GitHub token only when auditing remote or private repos

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
brew install zizmor
```

## Documentation

- https://docs.zizmor.sh/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
