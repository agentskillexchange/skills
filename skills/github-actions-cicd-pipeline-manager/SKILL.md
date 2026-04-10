---
name: "GitHub Actions CI/CD Pipeline Manager"
description: "Automates GitHub Actions workflow creation, runner management, and artifact caching using the GitHub REST API and YAML generation. Supports matrix builds, reusable workflows, and environment-specific deployment gates."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions CI/CD Pipeline Manager

The GitHub Actions CI/CD Pipeline Manager skill provides comprehensive automation for continuous integration and deployment workflows on GitHub. It leverages the GitHub REST API v3 and GraphQL API v4 to programmatically create, update, and monitor workflow files. The skill generates optimized YAML configurations for matrix builds across multiple OS and language versions, sets up dependency caching with actions/cache, and configures reusable workflow templates. It manages self-hosted runner registration via the Actions Runner API, handles artifact upload/download between jobs, and implements environment protection rules with required reviewers. The skill also integrates with GitHub Environments API for staging and production deployment gates, supports concurrency groups to prevent duplicate runs, and provides real-time status monitoring via the Checks API. Advanced features include automatic CODEOWNERS-based review assignment, branch protection rule synchronization, and composite action scaffolding for shared CI logic across repositories.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-cicd-pipeline-manager/)
