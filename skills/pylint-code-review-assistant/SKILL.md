---
title: "Pylint Code Review Assistant"
description: "Perform automated Python code reviews using Pylint programmatic API and pylint-json2html for report generation. Supports custom checker plugins and per-project rcfile configurations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pylint-code-review-assistant/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
---

# Pylint Code Review Assistant

The Pylint Code Review Assistant skill automates Python code quality reviews using the Pylint linter through both CLI and programmatic API (pylint.lint.Run, pylint.reporters). It executes targeted analysis on changed files, generating detailed reports with message IDs (C0114 missing-module-docstring, W0611 unused-import, E1101 no-member, R0902 too-many-instance-attributes) and scoring on Pylint 10-point scale. The skill manages .pylintrc and pyproject.toml [tool.pylint] configurations for project-specific rules, handles disable/enable directives for baseline management, and supports custom checker plugins extending BaseChecker for project-specific patterns. Report generation uses pylint-json2html for HTML output and JSON reporter for programmatic processing. The assistant integrates with diff-based workflows to review only modified code, compares scores between branches for quality gate enforcement, and generates inline code review comments mapped to specific file locations. It supports parallel execution with –jobs flag, handles virtual environment path configuration via init-hook, and manages message confidence levels (HIGH, INFERENCE, UNDEFINED) for finding prioritization.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-code-review-assistant/)
