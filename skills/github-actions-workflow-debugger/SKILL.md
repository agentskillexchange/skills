---
title: GitHub Actions Workflow Debugger
description: The GitHub Actions Workflow Debugger automates the diagnosis of failing
  CI/CD workflows using the GitHub REST API v3. It queries the /repos/{owner}/{repo}/actions/runs
  endpoint to identify failed runs, then drills into individual jobs via /actions/jobs/{job_id}/logs
  to extract step-level error output. The agent parses workflow YAML files against
  the GitHub Actions workflow schema, catching common issues like invalid on-trigger
  configurations, missing required inputs for reusable workflows, and incorrect uses
  declarations. It leverages the actions/runner-images repository metadata to verify
  runner OS compatibility and pre-installed tool versions. For composite actions and
  reusable workflows, it traces the dependency graph across repositories using the
  GitHub GraphQL API v4. The debugger identifies race conditions in job dependency
  chains defined by needs, validates matrix strategy configurations, and checks for
  deprecated action versions by querying the GitHub Marketplace API. Results are formatted
  as GitHub Check Run annotations via the Checks API for inline PR feedback.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-workflow-debugger/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# GitHub Actions Workflow Debugger

The GitHub Actions Workflow Debugger automates the diagnosis of failing CI/CD workflows using the GitHub REST API v3. It queries the /repos/{owner}/{repo}/actions/runs endpoint to identify failed runs, then drills into individual jobs via /actions/jobs/{job_id}/logs to extract step-level error output. The agent parses workflow YAML files against the GitHub Actions workflow schema, catching common issues like invalid on-trigger configurations, missing required inputs for reusable workflows, and incorrect uses declarations. It leverages the actions/runner-images repository metadata to verify runner OS compatibility and pre-installed tool versions. For composite actions and reusable workflows, it traces the dependency graph across repositories using the GitHub GraphQL API v4. The debugger identifies race conditions in job dependency chains defined by needs, validates matrix strategy configurations, and checks for deprecated action versions by querying the GitHub Marketplace API. Results are formatted as GitHub Check Run annotations via the Checks API for inline PR feedback.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-debugger/)
