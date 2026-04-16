---
title: "GitHub Actions Workflow Composer"
description: "Composes GitHub Actions workflow YAML files from modular job templates, resolving action version pins and secret references. Validates against the GitHub Actions schema and checks for known action CVEs."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-workflow-composer-2/"
category:
  - "Templates & Workflows"
framework:
  - "Claude Agents"
---

# GitHub Actions Workflow Composer

This skill programmatically generates GitHub Actions workflow files from composable job and step templates. It resolves action references against the GitHub Marketplace API, pinning to specific commit SHAs rather than mutable tags for supply chain security. The composer validates workflow YAML against the official GitHub Actions JSON schema, catching syntax errors and unsupported runner labels before commit. Secret reference validation ensures all referenced secrets and variables exist in the repository or organization scope. Matrix strategy generation creates cross-platform test configurations with intelligent exclude rules. Reusable workflow composition supports the workflow_call trigger with typed inputs and secrets inheritance. The skill generates Dependabot configuration for automated action version updates. Concurrency group configuration prevents redundant workflow runs on rapid pushes. Artifact upload and download steps are optimized with path globbing and retention policies. The agent checks pinned action versions against the GitHub Advisory Database for known vulnerabilities.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-composer-2/)
