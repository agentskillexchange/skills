---
title: "GitHub Actions Workflow Linter"
description: "The GitHub Actions Workflow Linter skill integrates actionlint with the GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses workflow YAML files and checks each step against the GitHub Marketplace API to verify action version availability and deprecation status. The skill inspects secrets references using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets) to ensure all referenced secrets exist. It validates matrix strategy configurations, detects circular job dependencies, and flags incorrect runner labels. Expression syntax is validated using a custom parser that checks github context references and function calls. The skill produces structured JSON reports compatible with GitHub Annotations API for inline PR feedback. It supports reusable workflow validation by resolving called workflow inputs and outputs across repositories via the Git Trees API."
source: "https://docs.github.com/en/actions"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions Workflow Linter

The GitHub Actions Workflow Linter skill integrates actionlint with the GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses workflow YAML files and checks each step against the GitHub Marketplace API to verify action version availability and deprecation status. The skill inspects secrets references using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets) to ensure all referenced secrets exist. It validates matrix strategy configurations, detects circular job dependencies, and flags incorrect runner labels. Expression syntax is validated using a custom parser that checks github context references and function calls. The skill produces structured JSON reports compatible with GitHub Annotations API for inline PR feedback. It supports reusable workflow validation by resolving called workflow inputs and outputs across repositories via the Git Trees API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-linter-2/)
