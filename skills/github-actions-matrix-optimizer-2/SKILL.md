---
title: GitHub Actions Matrix Optimizer
description: The GitHub Actions Matrix Optimizer connects to the GitHub REST API v3
  (/repos/{owner}/{repo}/actions/runs) to analyze historical workflow run data across
  matrix strategy builds. It identifies patterns of redundant matrix combinations
  that consistently pass together, suggesting matrix exclusion rules to reduce CI
  compute time. The skill examines timing data per matrix job to detect slow outliers,
  recommending targeted caching strategies or runner size adjustments. It supports
  multi-dimensional matrices (OS × Node version × test suite) and calculates potential
  minute savings based on your billing plan. The optimizer generates pull-ready YAML
  patches for workflow files, preserving existing matrix includes/excludes. It integrates
  with the GitHub Checks API to post optimization reports directly on PRs that modify
  workflow files.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# GitHub Actions Matrix Optimizer

The GitHub Actions Matrix Optimizer connects to the GitHub REST API v3 (/repos/{owner}/{repo}/actions/runs) to analyze historical workflow run data across matrix strategy builds. It identifies patterns of redundant matrix combinations that consistently pass together, suggesting matrix exclusion rules to reduce CI compute time. The skill examines timing data per matrix job to detect slow outliers, recommending targeted caching strategies or runner size adjustments. It supports multi-dimensional matrices (OS × Node version × test suite) and calculates potential minute savings based on your billing plan. The optimizer generates pull-ready YAML patches for workflow files, preserving existing matrix includes/excludes. It integrates with the GitHub Checks API to post optimization reports directly on PRs that modify workflow files.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/)
