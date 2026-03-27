---
name: "Ruff Linter and Formatter"
description: "Ultra-fast Python linting and formatting using Ruff CLI with pyproject.toml configuration. Supports auto-fix, import sorting (isort-compatible), and rule selection from 800+ built-in rules."
category: "Code Quality & Review"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ruff-linter-formatter-agent/"
---

# Ruff Linter and Formatter

Ultra-fast Python linting and formatting using Ruff CLI with pyproject.toml configuration. Supports auto-fix, import sorting (isort-compatible), and rule selection from 800+ built-in rules.

## Overview

The Ruff Linter and Formatter Agent skill provides high-performance Python code quality enforcement using Ruff, the Rust-based linter and formatter. It executes ruff check for linting with –fix for auto-correction and ruff format for Black-compatible code formatting, operating 10-100x faster than traditional Python linters. Configuration is managed through pyproject.toml [tool.ruff] sections with select/ignore lists for rule codes spanning pyflakes (F), pycodestyle (E/W), isort (I), pep8-naming (N), flake8-bugbear (B), and pylint (PL) rule families. The skill handles per-file-ignores for test directories, target-version for Python version-specific rules, and line-length configuration. Import sorting follows isort-compatible behavior with known-first-party and known-third-party sections. The agent supports ruff check –diff for preview mode, –output-format=json for programmatic processing, and –statistics for rule violation summaries. It manages .ruff.toml and ruff.toml alternative config locations, handles noqa comment management with ruff check –add-noqa, and supports pre-commit hook integration through the ruff-pre-commit mirror repository.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-formatter-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-formatter-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-formatter-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-formatter-agent -a codex
```

### OpenClaw

```bash
clawhub install ruff-linter-formatter-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ruff-linter-formatter-agent/
