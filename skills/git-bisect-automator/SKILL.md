---
title: Git Bisect Automator
description: The Git Bisect Automator skill streamlines regression hunting by automating
  git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect
  commands (start, good, bad, run, skip) with intelligent test script management,
  supporting unit tests, integration tests, and custom validation scripts as bisect
  criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on
  bisect candidate commits, collecting pass/fail results without local build requirements.
  Features include parallel bisect execution across multiple test suites, automatic
  skip of known-broken commits via git notes, and bisect log analysis for identifying
  flaky test interference. Supports repository submodule-aware bisection, worktree-based
  concurrent testing for faster narrowing, and automated blame annotation with commit
  message context extraction.
verification: security_reviewed
source: https://agentskillexchange.com/skills/git-bisect-automator/
category:
- Developer Tools
framework:
- Claude Code
---

# Git Bisect Automator

The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
