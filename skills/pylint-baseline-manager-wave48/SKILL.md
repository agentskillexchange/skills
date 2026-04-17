---
title: "Pylint Baseline Manager"
description: "The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations.\nThe skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation.\nDuring CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement.\nAdvanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/"
framework:
  - "Custom Agents"
---

# Pylint Baseline Manager

The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations.
The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation.
During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement.
Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pylint-baseline-manager-wave48
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pylint-baseline-manager-wave48` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/)
