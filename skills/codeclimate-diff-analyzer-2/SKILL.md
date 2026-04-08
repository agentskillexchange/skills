---
title: CodeClimate Diff Analyzer
description: 'The CodeClimate Diff Analyzer skill runs targeted code quality analysis
  on pull request changesets using the CodeClimate CLI engine in diff mode. Instead
  of analyzing the entire codebase, it focuses on changed files to provide fast, relevant
  feedback on new code quality issues. The analyzer extracts the diff from GitHub
  or GitLab merge request APIs, identifies modified files and line ranges, then runs
  CodeClimate engines (structure, duplication, complexity) against only those files.
  Issue classification maps CodeClimate categories to actionable labels: refactoring
  opportunities, complexity warnings, duplication alerts, and style violations. Maintainability
  impact scoring calculates per-file and per-PR scores based on cognitive complexity
  changes, method length increases, and new duplication blocks. Inline reporting posts
  issue annotations directly on pull request diffs using the GitHub Checks API or
  GitLab inline notes API. Trend tracking compares PR quality scores against repository
  baselines to identify whether changes improve or degrade overall maintainability.
  Configuration supports .codeclimate.yml with custom engine settings and exclude
  patterns for generated code.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# CodeClimate Diff Analyzer

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues. The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations. Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
