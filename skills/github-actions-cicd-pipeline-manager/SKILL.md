---
name: "GitHub Actions CI/CD Pipeline Manager"
description: "Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---
# GitHub Actions CI/CD Pipeline Manager

Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates.

## Overview

The GitHub Actions CI/CD Pipeline Manager skill provides comprehensive automation for continuous integration and deployment workflows on GitHub. It leverages the GitHub REST API v3 and GraphQL API v4 to programmatically create, update, and monitor workflow files. The skill generates optimized YAML configurations for matrix builds across multiple OS and language versions, sets up dependency caching with actions/cache, and configures reusable workflow templates. It manages self-hosted runner registration via the Actions Runner API, handles artifact upload/download between jobs, and implements environment protection rules with required reviewers. The skill also integrates with GitHub Environments API for staging and production deployment gates, supports concurrency groups to prevent duplicate runs, and provides real-time status monitoring via the Checks API. Advanced features include automatic CODEOWNERS-based review assignment, branch protection rule synchronization, and composite action scaffolding for shared CI logic across repositories.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-cicd-pipeline-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-cicd-pipeline-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-cicd-pipeline-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-cicd-pipeline-manager -a codex
```

### OpenClaw

```bash
clawhub install github-actions-cicd-pipeline-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/)
