---
title: "GitHub Actions Workflow Debugger"
description: "Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-debugger/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# GitHub Actions Workflow Debugger

The GitHub Actions Workflow Debugger automates the diagnosis of failing CI/CD workflows using the GitHub REST API v3. It queries the /repos/{owner}/{repo}/actions/runs endpoint to identify failed runs, then drills into individual jobs via /actions/jobs/{job_id}/logs to extract step-level error output.

The agent parses workflow YAML files against the GitHub Actions workflow schema, catching common issues like invalid on-trigger configurations, missing required inputs for reusable workflows, and incorrect uses declarations. It leverages the actions/runner-images repository metadata to verify runner OS compatibility and pre-installed tool versions.

For composite actions and reusable workflows, it traces the dependency graph across repositories using the GitHub GraphQL API v4. The debugger identifies race conditions in job dependency chains defined by needs, validates matrix strategy configurations, and checks for deprecated action versions by querying the GitHub Marketplace API. Results are formatted as GitHub Check Run annotations via the Checks API for inline PR feedback.

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
