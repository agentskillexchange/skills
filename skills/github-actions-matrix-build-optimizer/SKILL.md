---
name: "GitHub Actions Matrix Build Optimizer"
description: "Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/"
---

# GitHub Actions Matrix Build Optimizer

Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit.

## Overview

This skill connects to your GitHub repository using the GitHub REST API (api.github.com) and reads existing workflow YAML configurations from the .github/workflows directory. It analyzes the matrix strategy blocks, identifying redundant OS/version combinations and caching opportunities using actions/cache@v3. The skill leverages the GitHub Actions billing API to compute per-minute costs and suggests removal of low-value matrix entries. It can also integrate with the GitHub Checks API to correlate flaky test patterns with specific matrix legs. Output includes a revised workflow file with savings annotations, a Markdown summary of estimated monthly cost reduction, and optional PR creation via the GitHub Pull Requests API. Supports both GitHub.com and GitHub Enterprise Server endpoints.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-build-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-build-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-build-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-build-optimizer -a codex
```

### OpenClaw

```bash
clawhub install github-actions-matrix-build-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/
