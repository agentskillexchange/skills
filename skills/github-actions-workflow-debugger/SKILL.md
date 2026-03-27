---
name: "GitHub Actions Workflow Debugger"
description: "Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-debugger/"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---

# GitHub Actions Workflow Debugger

Diagnoses failing GitHub Actions workflows using the GitHub REST API v3 /actions/runs and /actions/jobs endpoints. Parses step logs, identifies YAML syntax errors, and suggests fixes for runner environment issues.

## Overview

The GitHub Actions Workflow Debugger automates the diagnosis of failing CI/CD workflows using the GitHub REST API v3. It queries the /repos/{owner}/{repo}/actions/runs endpoint to identify failed runs, then drills into individual jobs via /actions/jobs/{job_id}/logs to extract step-level error output.

The agent parses workflow YAML files against the GitHub Actions workflow schema, catching common issues like invalid on-trigger configurations, missing required inputs for reusable workflows, and incorrect uses declarations. It leverages the actions/runner-images repository metadata to verify runner OS compatibility and pre-installed tool versions.

For composite actions and reusable workflows, it traces the dependency graph across repositories using the GitHub GraphQL API v4. The debugger identifies race conditions in job dependency chains defined by needs, validates matrix strategy configurations, and checks for deprecated action versions by querying the GitHub Marketplace API. Results are formatted as GitHub Check Run annotations via the Checks API for inline PR feedback.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-debugger -a codex
```

### OpenClaw

```bash
clawhub install github-actions-workflow-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-workflow-debugger/
