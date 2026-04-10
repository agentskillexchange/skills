---
title: "GitHub Actions Matrix Build Optimizer"
description: "Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit."
slug: "github-actions-matrix-build-optimizer"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/"
---

# GitHub Actions Matrix Build Optimizer

Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit.

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
clawhub install github-actions-matrix-build-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill connects to your GitHub repository using the GitHub REST API (api.github.com) and reads existing workflow YAML configurations from the .github/workflows directory. It analyzes the matrix strategy blocks, identifying redundant OS/version combinations and caching opportunities using actions/cache@v3. The skill leverages the GitHub Actions billing API to compute per-minute costs and suggests removal of low-value matrix entries. It can also integrate with the GitHub Checks API to correlate flaky test patterns with specific matrix legs. Output includes a revised workflow file with savings annotations, a Markdown summary of estimated monthly cost reduction, and optional PR creation via the GitHub Pull Requests API. Supports both GitHub.com and GitHub Enterprise Server endpoints.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/)
