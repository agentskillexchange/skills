---
title: "Run only the relevant linters and formatters on changed files with Precious"
description: "Run just the applicable quality checks on changed files so pre-commit and CI feedback stays fast and targeted."
verification: "listed"
source: "https://github.com/houseabsolute/precious"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "houseabsolute/precious"
  github_stars: 152
---

# Run only the relevant linters and formatters on changed files with Precious

Use Precious when an agent needs to inspect a repository diff and run only the configured linters and formatters that apply to the changed files. A user should invoke this instead of running the full repo toolchain normally when the task is selective pre-commit or CI quality gating, not broad code review, static-analysis platform setup, or formatter authoring. The scope boundary is skill-shaped: it orchestrates changed-file quality checks from existing repo configuration and returns focused lint or format results, not a generic linting product or framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-only-the-relevant-linters-and-formatters-on-changed-files-with-precious/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-only-the-relevant-linters-and-formatters-on-changed-files-with-precious
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-only-the-relevant-linters-and-formatters-on-changed-files-with-precious`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-only-the-relevant-linters-and-formatters-on-changed-files-with-precious/)
