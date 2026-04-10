---
title: "GitHub Actions Workflow Debugger"
description: "Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues."
slug: "github-actions-workflow-debugger"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-workflow-debugger/"
listed: true
---

# GitHub Actions Workflow Debugger

Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues.

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
clawhub install github-actions-workflow-debugger
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitHub Actions Workflow Debugger automates the diagnosis of failing CI/CD workflows using the GitHub REST API v3. It queries the /repos/{owner}/{repo}/actions/runs endpoint to identify failed runs, then drills into individual jobs via /actions/jobs/{job_id}/logs to extract step-level error output.
The agent parses workflow YAML files against the GitHub Actions workflow schema, catching common issues like invalid on-trigger configurations, missing required inputs for reusable workflows, and incorrect uses declarations. It leverages the actions/runner-images repository metadata to verify runner OS compatibility and pre-installed tool versions.
For composite actions and reusable workflows, it traces the dependency graph across repositories using the GitHub GraphQL API v4. The debugger identifies race conditions in job dependency chains defined by needs, validates matrix strategy configurations, and checks for deprecated action versions by querying the GitHub Marketplace API. Results are formatted as GitHub Check Run annotations via the Checks API for inline PR feedback.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-debugger/)
