---
title: "GitHub Actions Workflow Linter"
description: "Validates GitHub Actions YAML workflows using actionlint and the GitHub Actions REST API. Detects invalid step references, missing secrets declarations, and deprecated action versions before CI runs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-linter-2/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# GitHub Actions Workflow Linter

The GitHub Actions Workflow Linter skill integrates actionlint with the GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses workflow YAML files and checks each step against the GitHub Marketplace API to verify action version availability and deprecation status. The skill inspects secrets references using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets) to ensure all referenced secrets exist. It validates matrix strategy configurations, detects circular job dependencies, and flags incorrect runner labels. Expression syntax is validated using a custom parser that checks github context references and function calls. The skill produces structured JSON reports compatible with GitHub Annotations API for inline PR feedback. It supports reusable workflow validation by resolving called workflow inputs and outputs across repositories via the Git Trees API.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-workflow-linter-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-workflow-linter-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-linter-2/)
