---
title: "CodeClimate Diff Analyzer"
description: "Runs CodeClimate analysis on pull request diffs using the CLI engine and reports new issues inline. Calculates maintainability impact scores per changed file."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
---

# CodeClimate Diff Analyzer

The CodeClimate Diff Analyzer skill runs targeted code quality analysis on pull request changesets using the CodeClimate CLI engine in diff mode. Instead of analyzing the entire codebase, it focuses on changed files to provide fast, relevant feedback on new code quality issues.

The analyzer extracts the diff from GitHub or GitLab merge request APIs, identifies modified files and line ranges, then runs CodeClimate engines (structure, duplication, complexity) against only those files. Issue classification maps CodeClimate categories to actionable labels: refactoring opportunities, complexity warnings, duplication alerts, and style violations.

Maintainability impact scoring calculates per-file and per-PR scores based on cognitive complexity changes, method length increases, and new duplication blocks. Inline reporting posts issue annotations directly on pull request diffs using the GitHub Checks API or GitLab inline notes API. Trend tracking compares PR quality scores against repository baselines to identify whether changes improve or degrade overall maintainability. Configuration supports .codeclimate.yml with custom engine settings and exclude patterns for generated code.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codeclimate-diff-analyzer-2/)
