---
title: "Pylint Code Review Assistant"
description: "Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations."
slug: "pylint-code-review-assistant"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pylint-code-review-assistant/"
listed: true
---

# Pylint Code Review Assistant

Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations.

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
clawhub install pylint-code-review-assistant
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Pylint Code Review Assistant skill automates Python code quality reviews using the Pylint linter through both CLI and programmatic API (pylint.lint.Run, pylint.reporters). It executes targeted analysis on changed files, generating detailed reports with message IDs (C0114 missing-module-docstring, W0611 unused-import, E1101 no-member, R0902 too-many-instance-attributes) and scoring on Pylint 10-point scale. The skill manages .pylintrc and pyproject.toml [tool.pylint] configurations for project-specific rules, handles disable/enable directives for baseline management, and supports custom checker plugins extending BaseChecker for project-specific patterns. Report generation uses pylint-json2html for HTML output and JSON reporter for programmatic processing. The assistant integrates with diff-based workflows to review only modified code, compares scores between branches for quality gate enforcement, and generates inline code review comments mapped to specific file locations. It supports parallel execution with –jobs flag, handles virtual environment path configuration via init-hook, and manages message confidence levels (HIGH, INFERENCE, UNDEFINED) for finding prioritization.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-code-review-assistant/)
