---
name: "Ruff Linter Configuration Architect"
description: "Configures and optimizes Ruff Python linter settings using the ruff CLI and pyproject.toml schema. Migrates from Flake8, isort, and Black configurations with automatic rule mapping."
category: "Code Quality & Review"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ruff-linter-configuration-architect/"
---

# Ruff Linter Configuration Architect

Configures and optimizes Ruff Python linter settings using the ruff CLI and pyproject.toml schema. Migrates from Flake8, isort, and Black configurations with automatic rule mapping.

## Overview

The Ruff Linter Configuration Architect automates the setup and optimization of Ruff — the high-performance Python linter and formatter written in Rust. It uses the ruff CLI for analysis and generates comprehensive pyproject.toml configurations.

The skill handles migration from legacy Python tooling by mapping Flake8 plugins and rules to their Ruff equivalents, converting isort configurations to Ruff isort settings, and translating Black formatting options to Ruff formatter settings. It analyzes existing codebases to recommend appropriate rule selections from Ruff’s extensive rule set including pyflakes, pycodestyle, isort, pep8-naming, flake8-bugbear, and pylint rules.

Configuration optimization includes per-file-ignores for test files and migration scripts, target-version settings based on project Python version requirements, and line-length coordination between linting and formatting. The architect generates pre-commit hook configurations and CI pipeline integrations with caching strategies optimized for Ruff’s fast execution speed.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-configuration-architect
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-configuration-architect -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-configuration-architect -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ruff-linter-configuration-architect -a codex
```

### OpenClaw

```bash
clawhub install ruff-linter-configuration-architect
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ruff-linter-configuration-architect/
