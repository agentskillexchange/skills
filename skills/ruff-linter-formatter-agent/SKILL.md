---
title: "Ruff Linter and Formatter"
description: "The Ruff Linter and Formatter Agent skill provides high-performance Python code quality enforcement using Ruff, the Rust-based linter and formatter. It executes ruff check for linting with &#8211;fix for auto-correction and ruff format for Black-compatible code formatting, operating 10-100x faster than traditional Python linters. Configuration is managed through pyproject.toml [tool.ruff] sections with select/ignore lists for rule codes spanning pyflakes (F), pycodestyle (E/W), isort (I), pep8-naming (N), flake8-bugbear (B), and pylint (PL) rule families. The skill handles per-file-ignores for test directories, target-version for Python version-specific rules, and line-length configuration. Import sorting follows isort-compatible behavior with known-first-party and known-third-party sections. The agent supports ruff check &#8211;diff for preview mode, &#8211;output-format=json for programmatic processing, and &#8211;statistics for rule violation summaries. It manages .ruff.toml and ruff.toml alternative config locations, handles noqa comment management with ruff check &#8211;add-noqa, and supports pre-commit hook integration through the ruff-pre-commit mirror repository."
source: "https://agentskillexchange.com/skills/ruff-linter-formatter-agent/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
---

# Ruff Linter and Formatter

The Ruff Linter and Formatter Agent skill provides high-performance Python code quality enforcement using Ruff, the Rust-based linter and formatter. It executes ruff check for linting with &#8211;fix for auto-correction and ruff format for Black-compatible code formatting, operating 10-100x faster than traditional Python linters. Configuration is managed through pyproject.toml [tool.ruff] sections with select/ignore lists for rule codes spanning pyflakes (F), pycodestyle (E/W), isort (I), pep8-naming (N), flake8-bugbear (B), and pylint (PL) rule families. The skill handles per-file-ignores for test directories, target-version for Python version-specific rules, and line-length configuration. Import sorting follows isort-compatible behavior with known-first-party and known-third-party sections. The agent supports ruff check &#8211;diff for preview mode, &#8211;output-format=json for programmatic processing, and &#8211;statistics for rule violation summaries. It manages .ruff.toml and ruff.toml alternative config locations, handles noqa comment management with ruff check &#8211;add-noqa, and supports pre-commit hook integration through the ruff-pre-commit mirror repository.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ruff-linter-formatter-agent/)
