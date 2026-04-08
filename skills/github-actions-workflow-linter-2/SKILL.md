---
title: GitHub Actions Workflow Linter
description: The GitHub Actions Workflow Linter skill integrates actionlint with the
  GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses
  workflow YAML files and checks each step against the GitHub Marketplace API to verify
  action version availability and deprecation status. The skill inspects secrets references
  using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets)
  to ensure all referenced secrets exist. It validates matrix strategy configurations,
  detects circular job dependencies, and flags incorrect runner labels. Expression
  syntax is validated using a custom parser that checks github context references
  and function calls. The skill produces structured JSON reports compatible with GitHub
  Annotations API for inline PR feedback. It supports reusable workflow validation
  by resolving called workflow inputs and outputs across repositories via the Git
  Trees API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-workflow-linter-2/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# GitHub Actions Workflow Linter

The GitHub Actions Workflow Linter skill integrates actionlint with the GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses workflow YAML files and checks each step against the GitHub Marketplace API to verify action version availability and deprecation status. The skill inspects secrets references using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets) to ensure all referenced secrets exist. It validates matrix strategy configurations, detects circular job dependencies, and flags incorrect runner labels. Expression syntax is validated using a custom parser that checks github context references and function calls. The skill produces structured JSON reports compatible with GitHub Annotations API for inline PR feedback. It supports reusable workflow validation by resolving called workflow inputs and outputs across repositories via the Git Trees API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-linter-2/)
