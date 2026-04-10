---
name: "Ruff Linter Configuration Architect"
description: "Configures and optimizes Ruff Python linter settings using the ruff CLI and pyproject.toml schema. Migrates from Flake8, isort, and Black configurations with automatic rule mapping."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ruff-linter-configuration-architect/"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
---

# Ruff Linter Configuration Architect

The Ruff Linter Configuration Architect automates the setup and optimization of Ruff — the high-performance Python linter and formatter written in Rust. It uses the ruff CLI for analysis and generates comprehensive pyproject.toml configurations.
The skill handles migration from legacy Python tooling by mapping Flake8 plugins and rules to their Ruff equivalents, converting isort configurations to Ruff isort settings, and translating Black formatting options to Ruff formatter settings. It analyzes existing codebases to recommend appropriate rule selections from Ruff's extensive rule set including pyflakes, pycodestyle, isort, pep8-naming, flake8-bugbear, and pylint rules.
Configuration optimization includes per-file-ignores for test files and migration scripts, target-version settings based on project Python version requirements, and line-length coordination between linting and formatting. The architect generates pre-commit hook configurations and CI pipeline integrations with caching strategies optimized for Ruff's fast execution speed.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ruff-linter-configuration-architect/)
