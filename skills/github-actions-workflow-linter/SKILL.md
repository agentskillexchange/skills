---
name: GitHub Actions Workflow Linter
description: Validates GitHub Actions workflow YAML files using actionlint and checks for security anti-patterns like script injection via ${{ github.event }}. Suggests pinned action versions using SHA hashes from the GitHub API.
category: CI/CD Integrations
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 25
source: https://agentskillexchange.com/skill/github-actions-workflow-linter/
---

# GitHub Actions Workflow Linter

Validates GitHub Actions workflow YAML files using actionlint and checks for security anti-patterns like script injection via ${{ github.event }}. Suggests pinned action versions using SHA hashes from the GitHub API.

## Overview

Validates GitHub Actions workflow YAML files using actionlint and checks for security anti-patterns like script injection via ${{ github.event }}. Suggests pinned action versions using SHA hashes from the GitHub API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter
```

### OpenClaw

```bash
clawhub install github-actions-workflow-linter
```

### Claude Code

```bash
claude mcp add github-actions-workflow-linter
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/github-actions-workflow-linter/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.3/5 (25 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/github-actions-workflow-linter/)
