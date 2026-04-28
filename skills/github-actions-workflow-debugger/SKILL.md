---
title: "GitHub Actions Workflow Debugger"
description: "Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues."
verification: security_reviewed
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# GitHub Actions Workflow Debugger

Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/github-actions-workflow-debugger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-workflow-debugger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/github-actions-workflow-debugger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-debugger/)
