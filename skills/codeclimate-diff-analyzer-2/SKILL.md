---
title: "CodeClimate Diff Analyzer"
description: "Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file."
verification: "security_reviewed"
source: "https://codeclimate.com/"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
---

# CodeClimate Diff Analyzer

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues.

The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations.

Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codeclimate-diff-analyzer-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/codeclimate-diff-analyzer-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
