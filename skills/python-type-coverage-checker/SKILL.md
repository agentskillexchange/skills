---
name: "Python Type Coverage Checker"
description: "Measures and enforces Python type annotation coverage using mypy –html-report and pyright with strict mode. Generates per-module coverage reports via mypy-coverage and integrates with pre-commit hooks for incremental enforcement."
category: "Code Quality & Review"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/python-type-coverage-checker/"
---

# Python Type Coverage Checker

Measures and enforces Python type annotation coverage using mypy –html-report and pyright with strict mode. Generates per-module coverage reports via mypy-coverage and integrates with pre-commit hooks for incremental enforcement.

## Overview

The Python Type Coverage Checker skill monitors and enforces type annotation coverage across Python codebases. It uses mypy and pyright as complementary type checkers to provide thorough analysis of type safety and annotation completeness.

The skill runs mypy with –html-report and –any-exprs-report flags to generate detailed per-module statistics on typed vs untyped expressions, function signatures, and variable annotations. It configures pyright in strict mode to catch additional type issues that mypy may miss, particularly around TypedDict, Protocol, and ParamSpec usage.

Coverage enforcement uses configurable thresholds per package or module, allowing teams to set higher standards for critical code paths while gradually improving coverage in legacy modules. The skill integrates with pre-commit hooks to block commits that decrease type coverage below the configured baseline. It generates trend reports showing coverage progression over time using mypy-coverage data stored in CI artifacts. For large codebases, it supports incremental adoption by generating per-file mypy configuration overrides and prioritizing modules by import frequency and bug density for typing efforts.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-checker -a codex
```

### OpenClaw

```bash
clawhub install python-type-coverage-checker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/python-type-coverage-checker/
