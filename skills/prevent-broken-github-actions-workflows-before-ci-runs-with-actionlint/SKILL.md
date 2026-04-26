---
title: "Prevent broken GitHub Actions workflows before CI runs with actionlint"
description: "Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time."
verification: "security_reviewed"
source: "https://github.com/rhysd/actionlint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rhysd/actionlint"
  github_stars: 3782
---

# Prevent broken GitHub Actions workflows before CI runs with actionlint

Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/)
