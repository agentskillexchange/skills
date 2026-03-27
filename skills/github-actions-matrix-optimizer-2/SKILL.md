---
name: "GitHub Actions Matrix Optimizer"
description: "Analyzes GitHub Actions workflow matrix strategies using the GitHub REST API v3 workflow runs endpoint. Identifies redundant matrix combinations and suggests fail-fast optimizations to reduce CI minutes."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/"
---

# GitHub Actions Matrix Optimizer

Analyzes GitHub Actions workflow matrix strategies using the GitHub REST API v3 workflow runs endpoint. Identifies redundant matrix combinations and suggests fail-fast optimizations to reduce CI minutes.

## Overview

The GitHub Actions Matrix Optimizer connects to the GitHub REST API v3 (/repos/{owner}/{repo}/actions/runs) to analyze historical workflow run data across matrix strategy builds. It identifies patterns of redundant matrix combinations that consistently pass together, suggesting matrix exclusion rules to reduce CI compute time. The skill examines timing data per matrix job to detect slow outliers, recommending targeted caching strategies or runner size adjustments. It supports multi-dimensional matrices (OS × Node version × test suite) and calculates potential minute savings based on your billing plan. The optimizer generates pull-ready YAML patches for workflow files, preserving existing matrix includes/excludes. It integrates with the GitHub Checks API to post optimization reports directly on PRs that modify workflow files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-optimizer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-optimizer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-optimizer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-matrix-optimizer-2 -a codex
```

### OpenClaw

```bash
clawhub install github-actions-matrix-optimizer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/
