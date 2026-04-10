---
title: "CodeClimate Diff Analyzer"
description: "Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file."
slug: "codeclimate-diff-analyzer-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/"
---

# CodeClimate Diff Analyzer

Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file.

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
clawhub install codeclimate-diff-analyzer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues.
The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations.
Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
