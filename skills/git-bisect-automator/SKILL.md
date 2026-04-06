---
name: Git Bisect Automator
description: Automates git bisect workflows with custom test scripts and CI pipeline
  integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing
  commits across large repositories.
category: Developer Tools
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-bisect-automator/"
---
# Git Bisect Automator

Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories.

The Git Bisect Automator skill streamlines regression hunting by automating git bisect sessions with configurable test harnesses. It wraps the Git CLI bisect commands (start, good, bad, run, skip) with intelligent test script management, supporting unit tests, integration tests, and custom validation scripts as bisect criteria. The skill integrates with GitHub Actions API to trigger CI pipelines on bisect candidate commits, collecting pass/fail results without local build requirements. Features include parallel bisect execution across multiple test suites, automatic skip of known-broken commits via git notes, and bisect log analysis for identifying flaky test interference. Supports repository submodule-aware bisection, worktree-based concurrent testing for faster narrowing, and automated blame annotation with commit message context extraction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automator -a codex
```

### OpenClaw

```bash
clawhub install git-bisect-automator
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
