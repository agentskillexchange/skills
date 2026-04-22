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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-workflow-debugger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-workflow-debugger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-debugger/)
