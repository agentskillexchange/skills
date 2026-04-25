---
title: "Inspect failing GitHub Actions checks and plan fixes with gh-fix-ci"
description: "Inspect failing GitHub Actions checks on the current PR, pull the actionable log snippet, and stop at an approval gate before implementing a fix."
verification: "listed"
source: "https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "openai/skills"
  github_stars: 17293
---

# Inspect failing GitHub Actions checks and plan fixes with gh-fix-ci

Use gh-fix-ci when the agent should inspect the current PR’s failing GitHub Actions checks, pull the relevant logs, summarize the real failure, and propose a fix plan before touching code. Invoke it instead of using GitHub or gh manually when you want a bounded failure-triage workflow with an explicit approval checkpoint. The scope boundary is clear and skill-shaped: GitHub Actions failure inspection and plan-first remediation for one PR, not a generic GitHub or CI product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/inspect-failing-github-actions-checks-and-plan-fixes-with-gh-fix-ci/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-failing-github-actions-checks-and-plan-fixes-with-gh-fix-ci
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/inspect-failing-github-actions-checks-and-plan-fixes-with-gh-fix-ci`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-failing-github-actions-checks-and-plan-fixes-with-gh-fix-ci/)
