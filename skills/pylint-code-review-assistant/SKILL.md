---
name: "Pylint Code Review Assistant"
description: "Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pylint-code-review-assistant/"
---

# Pylint Code Review Assistant

Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations.

## Overview

The Pylint Code Review Assistant skill automates Python code quality reviews using the Pylint linter through both CLI and programmatic API (pylint.lint.Run, pylint.reporters). It executes targeted analysis on changed files, generating detailed reports with message IDs (C0114 missing-module-docstring, W0611 unused-import, E1101 no-member, R0902 too-many-instance-attributes) and scoring on Pylint 10-point scale. The skill manages .pylintrc and pyproject.toml [tool.pylint] configurations for project-specific rules, handles disable/enable directives for baseline management, and supports custom checker plugins extending BaseChecker for project-specific patterns. Report generation uses pylint-json2html for HTML output and JSON reporter for programmatic processing. The assistant integrates with diff-based workflows to review only modified code, compares scores between branches for quality gate enforcement, and generates inline code review comments mapped to specific file locations. It supports parallel execution with –jobs flag, handles virtual environment path configuration via init-hook, and manages message confidence levels (HIGH, INFERENCE, UNDEFINED) for finding prioritization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pylint-code-review-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pylint-code-review-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pylint-code-review-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pylint-code-review-assistant -a codex
```

### OpenClaw

```bash
clawhub install pylint-code-review-assistant
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pylint-code-review-assistant/
