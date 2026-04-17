---
name: Prevent broken GitHub Actions workflows before CI runs with actionlint
description: Use actionlint when an agent needs to inspect GitHub Actions workflow
  files before a push or pull request lands. The skill checks syntax, expressions,
  action inputs, runner labels, cron patterns, and a few security footguns so the
  agent can stop bad workflow changes before CI burns time.
category: Code Quality & Review
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/rhysd/actionlint
tool_ecosystem:
  github_repo: rhysd/actionlint
  github_stars: 3782
  tool: actionlint
---
# Prevent broken GitHub Actions workflows before CI runs with actionlint
Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/)
