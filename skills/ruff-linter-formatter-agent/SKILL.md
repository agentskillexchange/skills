---
title: "Ruff Linter and Formatter"
description: "Ultra-fast Python linting and formatting using Ruff CLI with pyproject.toml configuration. Supports auto-fix, import sorting (isort-compatible), and rule selection from 800+ built-in rules."
slug: "ruff-linter-formatter-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ruff-linter-formatter-agent/"
---

# Ruff Linter and Formatter

Ultra-fast Python linting and formatting using Ruff CLI with pyproject.toml configuration. Supports auto-fix, import sorting (isort-compatible), and rule selection from 800+ built-in rules.

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
clawhub install ruff-linter-formatter-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Ruff Linter and Formatter Agent skill provides high-performance Python code quality enforcement using Ruff, the Rust-based linter and formatter. It executes ruff check for linting with –fix for auto-correction and ruff format for Black-compatible code formatting, operating 10-100x faster than traditional Python linters. Configuration is managed through pyproject.toml [tool.ruff] sections with select/ignore lists for rule codes spanning pyflakes (F), pycodestyle (E/W), isort (I), pep8-naming (N), flake8-bugbear (B), and pylint (PL) rule families. The skill handles per-file-ignores for test directories, target-version for Python version-specific rules, and line-length configuration. Import sorting follows isort-compatible behavior with known-first-party and known-third-party sections. The agent supports ruff check –diff for preview mode, –output-format=json for programmatic processing, and –statistics for rule violation summaries. It manages .ruff.toml and ruff.toml alternative config locations, handles noqa comment management with ruff check –add-noqa, and supports pre-commit hook integration through the ruff-pre-commit mirror repository.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ruff-linter-formatter-agent/)
