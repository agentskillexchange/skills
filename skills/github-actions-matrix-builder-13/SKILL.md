---
name: "GitHub Actions Matrix Builder"
description: "Generates dynamic GitHub Actions CI/CD matrix strategies using the GitHub REST API and YAML AST parsing via js-yaml. Automatically detects language versions, OS targets, and dependency variations from repository configuration files."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-matrix-builder-13/"
---
# GitHub Actions Matrix Builder

Generates dynamic GitHub Actions CI/CD matrix strategies using the GitHub REST API and YAML AST parsing via js-yaml. Automatically detects language versions, OS targets, and dependency variations from repository configuration files.

The GitHub Actions Matrix Builder skill automates the creation of complex CI/CD matrix configurations for GitHub Actions workflows. It leverages the GitHub REST API to analyze repository structure, detecting package.json, setup.py, Gemfile, and other dependency manifests to determine which language versions and operating systems should be included in the test matrix.



Using js-yaml for YAML abstract syntax tree manipulation, the skill can programmatically modify existing workflow files or generate new ones from scratch. It supports include/exclude rules, fail-fast strategies, and max-parallel configurations based on repository size and complexity.



The skill integrates with the GitHub Checks API to monitor matrix job outcomes and can automatically suggest matrix optimizations based on historical failure patterns. It also supports reusable workflow generation following GitHub’s composite action specification, enabling teams to share matrix strategies across repositories.



Key capabilities include Node.js version detection from .nvmrc and engines fields, Python version extraction from pyproject.toml, Ruby version parsing from .ruby-version, and Go version detection from go.mod files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-builder-13
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-builder-13 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-builder-13 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-builder-13 -a codex
```

### OpenClaw

```bash
clawhub install github-actions-matrix-builder-13
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-builder-13/)
