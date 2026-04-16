---
title: "GitHub Actions CI/CD Pipeline Manager"
description: "Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions CI/CD Pipeline Manager

The GitHub Actions CI/CD Pipeline Manager skill provides comprehensive automation for continuous integration and deployment workflows on GitHub. It leverages the GitHub REST API v3 and GraphQL API v4 to programmatically create, update, and monitor workflow files. The skill generates optimized YAML configurations for matrix builds across multiple OS and language versions, sets up dependency caching with actions/cache, and configures reusable workflow templates. It manages self-hosted runner registration via the Actions Runner API, handles artifact upload/download between jobs, and implements environment protection rules with required reviewers. The skill also integrates with GitHub Environments API for staging and production deployment gates, supports concurrency groups to prevent duplicate runs, and provides real-time status monitoring via the Checks API. Advanced features include automatic CODEOWNERS-based review assignment, branch protection rule synchronization, and composite action scaffolding for shared CI logic across repositories.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/)
