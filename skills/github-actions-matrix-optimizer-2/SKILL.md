---
name: "GitHub Actions Matrix Optimizer"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/)
