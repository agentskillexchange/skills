---
name: "Ruff Python Linter Configurator"
description: "Generates optimized Ruff configuration from existing Flake8, isort, and Black setups. Migrates pyproject.toml rules with automatic conflict resolution."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ruff-python-linter-configurator/"
---

# Ruff Python Linter Configurator

Generates optimized Ruff configuration from existing Flake8, isort, and Black setups. Migrates pyproject.toml rules with automatic conflict resolution.

## Overview

The Ruff Python Linter Configurator skill automates migration from legacy Python linting toolchains (Flake8, isort, Black, pylint, pycodestyle) to the Ruff linter by analyzing existing configuration files and generating equivalent ruff.toml or pyproject.toml [tool.ruff] sections.

The configurator parses .flake8, setup.cfg, tox.ini, and pyproject.toml to extract all active rules, per-file-ignores, max-line-length settings, and import sorting preferences. It maps Flake8 plugin codes to Ruff rule prefixes (E/W for pycodestyle, F for pyflakes, I for isort, UP for pyupgrade, B for flake8-bugbear) with automatic conflict resolution when rules contradict.

The output configuration includes select and ignore lists, fixable rules for auto-formatting, target Python version inference from pyproject.toml requires-python, and per-file overrides for test directories and scripts. Performance benchmarking compares Ruff execution time against the replaced tools to quantify the speedup. A migration checklist identifies rules that have no Ruff equivalent and suggests alternatives.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ruff-python-linter-configurator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ruff-python-linter-configurator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ruff-python-linter-configurator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ruff-python-linter-configurator -a codex
```

### OpenClaw

```bash
clawhub install ruff-python-linter-configurator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ruff-python-linter-configurator/
