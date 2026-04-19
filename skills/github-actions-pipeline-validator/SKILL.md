---
title: "GitHub Actions Pipeline Validator"
description: "The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times."
source: "https://docs.github.com/en/actions"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions Pipeline Validator

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-pipeline-validator/)
