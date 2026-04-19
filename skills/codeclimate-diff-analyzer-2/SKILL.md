---
title: "CodeClimate Diff Analyzer"
description: "The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues. The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations. Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code."
source: "https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
---

# CodeClimate Diff Analyzer

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues. The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations. Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
