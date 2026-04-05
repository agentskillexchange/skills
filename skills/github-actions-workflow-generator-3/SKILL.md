---
name: "GitHub Actions Workflow Generator"
description: "Generates GitHub Actions workflow YAML files using the GitHub REST API v3 and Actions API. Supports matrix builds, reusable workflows, and composite actions with caching via actions/cache."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-generator-3/"
---
# GitHub Actions Workflow Generator

Generates GitHub Actions workflow YAML files using the GitHub REST API v3 and Actions API. Supports matrix builds, reusable workflows, and composite actions with caching via actions/cache.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-generator-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-generator-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-generator-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-generator-3 -a codex
```

### OpenClaw

```bash
clawhub install github-actions-workflow-generator-3
```

## Details

The GitHub Actions Workflow Generator skill creates production-ready CI/CD workflow files for GitHub repositories. Using the GitHub REST API v3 and the Actions-specific endpoints, it can list existing workflows, check run statuses, and programmatically dispatch workflow events. The skill generates YAML workflow definitions supporting matrix strategy builds across multiple OS versions and language runtimes. It implements reusable workflows with workflow_call triggers for organization-wide standardization. Composite actions are supported for encapsulating multi-step processes into single action references. The skill integrates actions/cache for dependency caching, actions/upload-artifact and actions/download-artifact for build artifact management, and supports environment secrets and variables configuration. OIDC token authentication for cloud provider deployments is also supported.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-generator-3/)
