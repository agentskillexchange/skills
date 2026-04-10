---
title: "Pylint Baseline Manager"
description: "Manages Pylint baseline files for gradual code quality improvement using pylint –output-format=json and the pylint.reporters API. Tracks new violations per commit while suppressing pre-existing issues in legacy code."
slug: "pylint-baseline-manager-wave48"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/"
---

# Pylint Baseline Manager

Manages Pylint baseline files for gradual code quality improvement using pylint –output-format=json and the pylint.reporters API. Tracks new violations per commit while suppressing pre-existing issues in legacy code.

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
clawhub install pylint-baseline-manager-wave48
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations.
The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation.
During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement.
Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/)
