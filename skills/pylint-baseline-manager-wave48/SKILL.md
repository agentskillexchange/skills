---
title: "Pylint Baseline Manager"
description: "The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations. The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation. During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement. Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation."
source: "https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
---

# Pylint Baseline Manager

The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations. The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation. During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement. Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/)
