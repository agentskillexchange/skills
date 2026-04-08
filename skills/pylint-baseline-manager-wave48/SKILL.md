---
title: Pylint Baseline Manager
description: The Pylint Baseline Manager skill implements a ratchet-based approach
  to Python code quality improvement. It uses pylint with JSON output format and the
  pylint.reporters API to create, maintain, and enforce baselines that distinguish
  between pre-existing code quality issues and newly introduced violations. The skill
  generates baseline files by running pylint across the entire codebase and recording
  each violation with its file path, line number, message ID, and a content hash of
  the surrounding code context. This hash-based matching ensures baselines remain
  valid even when lines shift due to unrelated edits above or below the violation.
  During CI runs, the skill compares current pylint output against the baseline, reporting
  only net-new violations. It supports per-module baselines for large codebases, allowing
  teams to set different quality standards for legacy versus new code. The skill uses
  pylint message categories (convention, refactor, warning, error, fatal) to prioritize
  enforcement. Advanced features include automatic baseline updates when violations
  are fixed (ratchet down), tracking of violation trends over time with matplotlib
  chart generation, and integration with pre-commit hooks to prevent baseline regressions.
  It also generates per-developer violation reports using git blame correlation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/
category:
- Code Quality &amp; Review
framework:
- Custom Agents
---

# Pylint Baseline Manager

The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations. The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation. During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement. Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/)
