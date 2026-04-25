---
title: "GitHub Actions Pipeline Validator"
description: "Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions Pipeline Validator

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/github-actions-pipeline-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-pipeline-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/github-actions-pipeline-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-pipeline-validator/)
