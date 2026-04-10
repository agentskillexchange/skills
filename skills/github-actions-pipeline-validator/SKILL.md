---
title: "GitHub Actions Pipeline Validator"
description: "Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs."
slug: "github-actions-pipeline-validator"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-pipeline-validator/"
listed: true
---

# GitHub Actions Pipeline Validator

Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs.

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
clawhub install github-actions-pipeline-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-pipeline-validator/)
