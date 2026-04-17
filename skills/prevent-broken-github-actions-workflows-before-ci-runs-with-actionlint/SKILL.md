---
title: "Prevent broken GitHub Actions workflows before CI runs with actionlint"
description: "Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time."
verification: security_reviewed
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

This ASE entry is built around actionlint, the open source static checker for GitHub Actions workflow files maintained at rhysd/actionlint. The agent behavior is narrow and concrete: scan one repository’s workflow YAML, explain what is broken, and block or repair bad workflow edits before they hit GitHub Actions. That is the job-to-be-done. The agent is not acting as a general CI platform, a generic linter catalog, or a framework listing. It is using actionlint specifically to catch invalid keys, broken expressions, wrong action inputs, risky inline-script patterns, runner-label mistakes, dependency graph errors, and cron syntax problems inside workflow files.

Invoke this skill when a user is changing .github/workflows/*.yml, reviewing a pull request that touched workflow automation, or trying to understand why a workflow definition is obviously wrong before GitHub even starts a run. It is especially useful in repository maintenance, release automation, reusable workflow authoring, and pre-merge review loops where an agent can lint, summarize failures, and propose exact YAML fixes. actionlint also integrates shellcheck and pyflakes checks for inline scripts, which gives the agent a stronger review pass than plain YAML validation.

The scope boundary matters. This is not “GitHub Actions” as a product card, and it is not a generic Go CLI listing. The skill is bounded to preflight validation of workflow definitions. Integration points are local repository checkouts, pre-commit hooks, CI guard jobs, reviewdog pipelines, and editor or PR review automation. Upstream evidence is strong: the official GitHub repo exists, tagged releases are available, the MIT license is published, installation and usage docs are maintained in the repo, and the project shows recent maintenance and broad adoption.

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
