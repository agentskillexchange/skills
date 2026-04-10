---
title: "GitHub Actions Workflow Composer"
description: "Composes GitHub Actions workflow YAML files from modular job templates, resolving action version pins and secret references. Validates against the GitHub Actions schema and checks for known action CVEs."
slug: "github-actions-workflow-composer-2"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-workflow-composer-2/"
listed: true
---

# GitHub Actions Workflow Composer

Composes GitHub Actions workflow YAML files from modular job templates, resolving action version pins and secret references. Validates against the GitHub Actions schema and checks for known action CVEs.

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
clawhub install github-actions-workflow-composer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill programmatically generates GitHub Actions workflow files from composable job and step templates. It resolves action references against the GitHub Marketplace API, pinning to specific commit SHAs rather than mutable tags for supply chain security. The composer validates workflow YAML against the official GitHub Actions JSON schema, catching syntax errors and unsupported runner labels before commit. Secret reference validation ensures all referenced secrets and variables exist in the repository or organization scope. Matrix strategy generation creates cross-platform test configurations with intelligent exclude rules. Reusable workflow composition supports the workflow_call trigger with typed inputs and secrets inheritance. The skill generates Dependabot configuration for automated action version updates. Concurrency group configuration prevents redundant workflow runs on rapid pushes. Artifact upload and download steps are optimized with path globbing and retention policies. The agent checks pinned action versions against the GitHub Advisory Database for known vulnerabilities.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-composer-2/)
