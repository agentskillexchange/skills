---
title: "GitHub Actions Matrix Build Optimizer"
description: "Analyzes GitHub Actions workflow YAML files and optimizes matrix strategies using the actions/setup-node and actions/cache APIs. Reduces redundant job combinations by inspecting build dependency graphs via the GitHub REST API. Outputs a revised workflow with estimated CI time savings per commit."
verification: security_reviewed
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions Matrix Build Optimizer

This skill connects to your GitHub repository using the GitHub REST API (api.github.com) and reads existing workflow YAML configurations from the .github/workflows directory. It analyzes the matrix strategy blocks, identifying redundant OS/version combinations and caching opportunities using actions/cache@v3. The skill leverages the GitHub Actions billing API to compute per-minute costs and suggests removal of low-value matrix entries. It can also integrate with the GitHub Checks API to correlate flaky test patterns with specific matrix legs. Output includes a revised workflow file with savings annotations, a Markdown summary of estimated monthly cost reduction, and optional PR creation via the GitHub Pull Requests API. Supports both GitHub.com and GitHub Enterprise Server endpoints.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-matrix-build-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-matrix-build-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-build-optimizer/)
