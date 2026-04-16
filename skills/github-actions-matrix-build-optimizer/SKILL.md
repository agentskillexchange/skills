---
title: "GitHub Actions Matrix Build Optimizer"
description: "Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions Matrix Build Optimizer

This skill connects to your GitHub repository using the GitHub REST API (api.github.com) and reads existing workflow YAML configurations from the .github/workflows directory. It analyzes the matrix strategy blocks, identifying redundant OS/version combinations and caching opportunities using actions/cache@v3. The skill leverages the GitHub Actions billing API to compute per-minute costs and suggests removal of low-value matrix entries. It can also integrate with the GitHub Checks API to correlate flaky test patterns with specific matrix legs. Output includes a revised workflow file with savings annotations, a Markdown summary of estimated monthly cost reduction, and optional PR creation via the GitHub Pull Requests API. Supports both GitHub.com and GitHub Enterprise Server endpoints.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/)
