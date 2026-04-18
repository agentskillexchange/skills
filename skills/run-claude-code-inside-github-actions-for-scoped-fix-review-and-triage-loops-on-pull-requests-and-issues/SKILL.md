---
title: "Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues"
description: "Use Claude Code as a bounded GitHub Actions worker for PR reviews, issue follow-up, and repository automation that stays inside normal workflow triggers and runner policy."
verification: security_reviewed
source: "https://github.com/anthropics/claude-code-action"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-action"
  github_stars: 7136
---

# Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues

This skill is for teams that already use GitHub Actions and want Claude Code to enter the repo through a reviewable automation boundary instead of an ad hoc local session. It covers the operator workflow of wiring Claude Code into pull request, issue, and scheduled workflow triggers, then shaping prompts, permissions, and outputs so the run stays scoped to the event that invoked it.

Invoke this instead of using Claude Code manually when the work should happen inside CI, on repository infrastructure, with durable logs and repeatable triggers. Typical cases include PR review passes, @claude comment handling, issue triage, and small bounded fix loops.

The scope boundary is narrow: this is not a generic Claude Code product card or a general GitHub Actions listing. It is specifically about running the Claude Code Action as a guarded repository automation surface inside GitHub Actions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-claude-code-inside-github-actions-for-scoped-fix-review-and-triage-loops-on-pull-requests-and-issues
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/run-claude-code-inside-github-actions-for-scoped-fix-review-and-triage-loops-on-pull-requests-and-issues` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-code-inside-github-actions-for-scoped-fix-review-and-triage-loops-on-pull-requests-and-issues/)
