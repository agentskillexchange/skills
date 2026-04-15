---
title: "GitHub Actions Matrix Optimizer"
description: "Analyzes GitHub Actions workflow matrix strategies using the GitHub REST API v3 workflow runs endpoint. Identifies redundant matrix combinations and suggests fail-fast optimizations to reduce CI minutes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions Matrix Optimizer

The GitHub Actions Matrix Optimizer connects to the GitHub REST API v3 (/repos/{owner}/{repo}/actions/runs) to analyze historical workflow run data across matrix strategy builds. It identifies patterns of redundant matrix combinations that consistently pass together, suggesting matrix exclusion rules to reduce CI compute time. The skill examines timing data per matrix job to detect slow outliers, recommending targeted caching strategies or runner size adjustments. It supports multi-dimensional matrices (OS × Node version × test suite) and calculates potential minute savings based on your billing plan. The optimizer generates pull-ready YAML patches for workflow files, preserving existing matrix includes/excludes. It integrates with the GitHub Checks API to post optimization reports directly on PRs that modify workflow files.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-matrix-optimizer-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-matrix-optimizer-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/)
