---
title: "Pylint Code Review Assistant"
description: "Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations."
verification: "security_reviewed"
source: "https://github.com/pylint-dev/pylint"
category:
  - "Code Quality & Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "pylint-dev/pylint"
  github_stars: 5676
---

# Pylint Code Review Assistant

The Pylint Code Review Assistant skill automates Python code quality reviews using the Pylint linter through both CLI and programmatic API (pylint.lint.Run, pylint.reporters). It executes targeted analysis on changed files, generating detailed reports with message IDs (C0114 missing-module-docstring, W0611 unused-import, E1101 no-member, R0902 too-many-instance-attributes) and scoring on Pylint 10-point scale. The skill manages .pylintrc and pyproject.toml [tool.pylint] configurations for project-specific rules, handles disable/enable directives for baseline management, and supports custom checker plugins extending BaseChecker for project-specific patterns. Report generation uses pylint-json2html for HTML output and JSON reporter for programmatic processing. The assistant integrates with diff-based workflows to review only modified code, compares scores between branches for quality gate enforcement, and generates inline code review comments mapped to specific file locations. It supports parallel execution with –jobs flag, handles virtual environment path configuration via init-hook, and manages message confidence levels (HIGH, INFERENCE, UNDEFINED) for finding prioritization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pylint-code-review-assistant/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pylint-code-review-assistant
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pylint-code-review-assistant`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-code-review-assistant/)
