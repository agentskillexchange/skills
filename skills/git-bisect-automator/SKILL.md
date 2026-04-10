---
title: "Git Bisect Automator"
description: "Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories."
slug: "git-bisect-automator"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-bisect-automator/"
listed: true
---

# Git Bisect Automator

Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install git-bisect-automator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
