---
name: GitHub Actions Matrix Build Optimizer
description: Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies
  using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations
  by inspecting build dependency graphs via the GitHub REST API. Outputs a revised
  workflow with estimated CI time savings per commit.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/
category:
- CI/CD Integrations
framework:
- Claude Code
---
# GitHub Actions Matrix Build Optimizer

This skill connects to your GitHub repository using the GitHub REST API (api.github.com) and reads existing workflow YAML configurations from the .github/workflows directory. It analyzes the matrix strategy blocks, identifying redundant OS/version combinations and caching opportunities using actions/cache@v3. The skill leverages the GitHub Actions billing API to compute per-minute costs and suggests removal of low-value matrix entries. It can also integrate with the GitHub Checks API to correlate flaky test patterns with specific matrix legs. Output includes a revised workflow file with savings annotations, a Markdown summary of estimated monthly cost reduction, and optional PR creation via the GitHub Pull Requests API. Supports both GitHub.com and GitHub Enterprise Server endpoints.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/)
