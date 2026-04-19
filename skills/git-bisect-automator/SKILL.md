---
title: "Git Bisect Automator"
description: "The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction."
source: "https://agentskillexchange.com/skills/git-bisect-automator/"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
---

# Git Bisect Automator

The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
