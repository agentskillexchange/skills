---
name: "fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs"
title: "Fix failing pull requests by analyzing CI errors and pushing targeted repairs"
description: "Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history."
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md"
---

# Fix failing pull requests by analyzing CI errors and pushing targeted repairs

Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs/)
