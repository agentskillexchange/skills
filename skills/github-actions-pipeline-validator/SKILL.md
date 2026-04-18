---
title: "GitHub Actions Pipeline Validator"
description: "Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs."
verification: security_reviewed
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions Pipeline Validator

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-pipeline-validator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-pipeline-validator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-pipeline-validator/)
