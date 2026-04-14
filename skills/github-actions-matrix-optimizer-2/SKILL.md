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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-optimizer-2/)
