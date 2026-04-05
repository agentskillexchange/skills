---
name: "GitHub Actions Workflow Linter"
description: "Validates GitHub Actions YAML workflows using actionlint and the GitHub Actions REST API. Detects invalid step references, missing secrets declarations, and deprecated action versions before CI runs."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-workflow-linter-2/"
---
# GitHub Actions Workflow Linter

Validates GitHub Actions YAML workflows using actionlint and the GitHub Actions REST API. Detects invalid step references, missing secrets declarations, and deprecated action versions before CI runs.

The GitHub Actions Workflow Linter skill integrates actionlint with the GitHub Actions REST API to provide comprehensive CI/CD pipeline validation. It parses workflow YAML files and checks each step against the GitHub Marketplace API to verify action version availability and deprecation status. The skill inspects secrets references using the GitHub Repository Secrets API endpoint (GET /repos/{owner}/{repo}/actions/secrets) to ensure all referenced secrets exist. It validates matrix strategy configurations, detects circular job dependencies, and flags incorrect runner labels. Expression syntax is validated using a custom parser that checks github context references and function calls. The skill produces structured JSON reports compatible with GitHub Annotations API for inline PR feedback. It supports reusable workflow validation by resolving called workflow inputs and outputs across repositories via the Git Trees API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter-2 -a codex
```

### OpenClaw

```bash
clawhub install github-actions-workflow-linter-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-workflow-linter-2/)
