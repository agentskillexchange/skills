---
title: "Ruff Linter and Formatter"
description: "Ultra-fast Python linting and formatting using Ruff CLI with pyproject.toml configuration. Supports auto-fix, import sorting (isort-compatible), and rule selection from 800+ built-in rules."
verification: "security_reviewed"
source: "https://github.com/astral-sh/ruff"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "astral-sh/ruff"
  github_stars: 47173
---

# Ruff Linter and Formatter

The Ruff Linter and Formatter Agent skill provides high-performance Python code quality enforcement using Ruff, the Rust-based linter and formatter. It executes ruff check for linting with –fix for auto-correction and ruff format for Black-compatible code formatting, operating 10-100x faster than traditional Python linters. Configuration is managed through pyproject.toml [tool.ruff] sections with select/ignore lists for rule codes spanning pyflakes (F), pycodestyle (E/W), isort (I), pep8-naming (N), flake8-bugbear (B), and pylint (PL) rule families. The skill handles per-file-ignores for test directories, target-version for Python version-specific rules, and line-length configuration. Import sorting follows isort-compatible behavior with known-first-party and known-third-party sections. The agent supports ruff check –diff for preview mode, –output-format=json for programmatic processing, and –statistics for rule violation summaries. It manages .ruff.toml and ruff.toml alternative config locations, handles noqa comment management with ruff check –add-noqa, and supports pre-commit hook integration through the ruff-pre-commit mirror repository.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ruff-linter-formatter-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ruff-linter-formatter-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ruff-linter-formatter-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ruff-linter-formatter-agent/)
