---
title: "GitHub Actions CI/CD Pipeline Manager"
description: "Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates."
slug: "github-actions-cicd-pipeline-manager"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/"
listed: true
---

# GitHub Actions CI/CD Pipeline Manager

Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates.

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
clawhub install github-actions-cicd-pipeline-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitHub Actions CI/CD Pipeline Manager skill provides comprehensive automation for continuous integration and deployment workflows on GitHub. It leverages the GitHub REST API v3 and GraphQL API v4 to programmatically create, update, and monitor workflow files. The skill generates optimized YAML configurations for matrix builds across multiple OS and language versions, sets up dependency caching with actions/cache, and configures reusable workflow templates. It manages self-hosted runner registration via the Actions Runner API, handles artifact upload/download between jobs, and implements environment protection rules with required reviewers. The skill also integrates with GitHub Environments API for staging and production deployment gates, supports concurrency groups to prevent duplicate runs, and provides real-time status monitoring via the Checks API. Advanced features include automatic CODEOWNERS-based review assignment, branch protection rule synchronization, and composite action scaffolding for shared CI logic across repositories.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/)
