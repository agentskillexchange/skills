---
name: GitHub Actions Workflow Generator
description: Generates GitHub Actions workflow YAML files using the GitHub REST API
  v3 and Actions API. Supports matrix builds, reusable workflows, and composite actions
  with caching via actions/cache.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-workflow-generator-3/
category:
- CI/CD Integrations
framework:
- Claude Code
---
# GitHub Actions Workflow Generator

The GitHub Actions Workflow Generator skill creates production-ready CI/CD workflow files for GitHub repositories. Using the GitHub REST API v3 and the Actions-specific endpoints, it can list existing workflows, check run statuses, and programmatically dispatch workflow events. The skill generates YAML workflow definitions supporting matrix strategy builds across multiple OS versions and language runtimes. It implements reusable workflows with workflow_call triggers for organization-wide standardization. Composite actions are supported for encapsulating multi-step processes into single action references. The skill integrates actions/cache for dependency caching, actions/upload-artifact and actions/download-artifact for build artifact management, and supports environment secrets and variables configuration. OIDC token authentication for cloud provider deployments is also supported.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-generator-3/)
