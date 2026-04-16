---
title: "Git Bisect Automator"
description: "Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-bisect-automator/"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
---

# Git Bisect Automator

The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
