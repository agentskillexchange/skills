---
title: GitHub Actions Pipeline Validator
description: The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD
  pipeline validation for GitHub Actions workflows. It parses workflow YAML files
  against the official GitHub Actions schema specification, identifying syntax errors,
  deprecated action references, and misconfigured triggers. The validator checks all
  uses directives against the GitHub Marketplace API to verify action version compatibility
  and flag deprecated versions. It integrates with the dorny/paths-filter API to validate
  path-based trigger configurations and uses the actions/checkout and actions/setup-node
  SDKs to verify proper setup step ordering. Security scanning identifies exposed
  secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN
  permissions. The skill generates detailed reports with suggested fixes, including
  automatic version pinning recommendations and workflow optimization tips for reducing
  build times.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-pipeline-validator/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# GitHub Actions Pipeline Validator

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-pipeline-validator/)
