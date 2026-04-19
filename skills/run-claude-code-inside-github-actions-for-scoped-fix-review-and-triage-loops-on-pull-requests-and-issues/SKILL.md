---
title: "Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues"
description: "This skill is for teams that already use GitHub Actions and want Claude Code to enter the repo through a reviewable automation boundary instead of an ad hoc local session. It covers the operator workflow of wiring Claude Code into pull request, issue, and scheduled workflow triggers, then shaping prompts, permissions, and outputs so the run stays scoped to the event that invoked it. Invoke this instead of using Claude Code manually when the work should happen inside CI, on repository infrastructure, with durable logs and repeatable triggers. Typical cases include PR review passes, @claude comment handling, issue triage, and small bounded fix loops. The scope boundary is narrow: this is not a generic Claude Code product card or a general GitHub Actions listing. It is specifically about running the Claude Code Action as a guarded repository automation surface inside GitHub Actions."
source: "https://github.com/anthropics/claude-code-action"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-action"
  github_stars: 7136
---

# Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues

This skill is for teams that already use GitHub Actions and want Claude Code to enter the repo through a reviewable automation boundary instead of an ad hoc local session. It covers the operator workflow of wiring Claude Code into pull request, issue, and scheduled workflow triggers, then shaping prompts, permissions, and outputs so the run stays scoped to the event that invoked it. Invoke this instead of using Claude Code manually when the work should happen inside CI, on repository infrastructure, with durable logs and repeatable triggers. Typical cases include PR review passes, @claude comment handling, issue triage, and small bounded fix loops. The scope boundary is narrow: this is not a generic Claude Code product card or a general GitHub Actions listing. It is specifically about running the Claude Code Action as a guarded repository automation surface inside GitHub Actions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-code-inside-github-actions-for-scoped-fix-review-and-triage-loops-on-pull-requests-and-issues/)
