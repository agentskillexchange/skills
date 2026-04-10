---
name: GitHub Actions Workflow Composer
description: Composes GitHub Actions workflow YAML files from modular job templates,
  resolving action version pins and secret references. Validates against the GitHub
  Actions schema and checks for known action CVEs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-workflow-composer-2/
category:
- Templates &amp; Workflows
framework:
- Claude Agents
---
# GitHub Actions Workflow Composer

This skill programmatically generates GitHub Actions workflow files from composable job and step templates. It resolves action references against the GitHub Marketplace API, pinning to specific commit SHAs rather than mutable tags for supply chain security. The composer validates workflow YAML against the official GitHub Actions JSON schema, catching syntax errors and unsupported runner labels before commit. Secret reference validation ensures all referenced secrets and variables exist in the repository or organization scope. Matrix strategy generation creates cross-platform test configurations with intelligent exclude rules. Reusable workflow composition supports the workflow_call trigger with typed inputs and secrets inheritance. The skill generates Dependabot configuration for automated action version updates. Concurrency group configuration prevents redundant workflow runs on rapid pushes. Artifact upload and download steps are optimized with path globbing and retention policies. The agent checks pinned action versions against the GitHub Advisory Database for known vulnerabilities.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-composer-2/)
