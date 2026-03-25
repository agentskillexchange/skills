---
name: "Pylint Baseline Manager"
description: "Manages Pylint baseline files for gradual code quality improvement using pylint –output-format=json and the pylint.reporters API. Tracks new violations per commit while suppressing pre-existing issues in legacy code."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/"
---

# Pylint Baseline Manager

Manages Pylint baseline files for gradual code quality improvement using pylint –output-format=json and the pylint.reporters API. Tracks new violations per commit while suppressing pre-existing issues in legacy code.

## Overview

The Pylint Baseline Manager skill implements a ratchet-based approach to Python code quality improvement. It uses pylint with JSON output format and the pylint.reporters API to create, maintain, and enforce baselines that distinguish between pre-existing code quality issues and newly introduced violations.

The skill generates baseline files by running pylint across the entire codebase and recording each violation with its file path, line number, message ID, and a content hash of the surrounding code context. This hash-based matching ensures baselines remain valid even when lines shift due to unrelated edits above or below the violation.

During CI runs, the skill compares current pylint output against the baseline, reporting only net-new violations. It supports per-module baselines for large codebases, allowing teams to set different quality standards for legacy versus new code. The skill uses pylint message categories (convention, refactor, warning, error, fatal) to prioritize enforcement.

Advanced features include automatic baseline updates when violations are fixed (ratchet down), tracking of violation trends over time with matplotlib chart generation, and integration with pre-commit hooks to prevent baseline regressions. It also generates per-developer violation reports using git blame correlation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pylint-baseline-manager-wave48
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pylint-baseline-manager-wave48 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pylint-baseline-manager-wave48 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pylint-baseline-manager-wave48 -a codex
```

### OpenClaw

```bash
clawhub install pylint-baseline-manager-wave48
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pylint-baseline-manager-wave48/
