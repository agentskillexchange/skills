---
title: "GitHub Actions Matrix Optimizer"
description: "Analyzes GitHub Actions workflow matrix strategies using the GitHub REST API v3 workflow runs endpoint. Identifies redundant matrix combinations and suggests fail-fast optimizations to reduce CI minutes."
slug: "github-actions-matrix-optimizer-2"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/"
---

# GitHub Actions Matrix Optimizer

Analyzes GitHub Actions workflow matrix strategies using the GitHub REST API v3 workflow runs endpoint. Identifies redundant matrix combinations and suggests fail-fast optimizations to reduce CI minutes.

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
clawhub install github-actions-matrix-optimizer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitHub Actions Matrix Optimizer connects to the GitHub REST API v3 (/repos/{owner}/{repo}/actions/runs) to analyze historical workflow run data across matrix strategy builds. It identifies patterns of redundant matrix combinations that consistently pass together, suggesting matrix exclusion rules to reduce CI compute time. The skill examines timing data per matrix job to detect slow outliers, recommending targeted caching strategies or runner size adjustments. It supports multi-dimensional matrices (OS × Node version × test suite) and calculates potential minute savings based on your billing plan. The optimizer generates pull-ready YAML patches for workflow files, preserving existing matrix includes/excludes. It integrates with the GitHub Checks API to post optimization reports directly on PRs that modify workflow files.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/)
