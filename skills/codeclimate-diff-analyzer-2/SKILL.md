---
name: "CodeClimate Diff Analyzer"
description: "Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/"
---
# CodeClimate Diff Analyzer

Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file.

## Overview

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues.

The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations.

Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codeclimate-diff-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codeclimate-diff-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codeclimate-diff-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codeclimate-diff-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install codeclimate-diff-analyzer-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
