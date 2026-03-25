---
name: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 48003
  github_repo: "hashicorp/terraform"
  maintained: true
---

# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Overview

This skill analyzes Terraform plan output to provide human-readable summaries and policy checks before applying infrastructure changes. It parses the JSON output from terraform show -json or retrieves plan artifacts from the Terraform Cloud API using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources by action type (create, update, delete, replace) and highlights destructive changes with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting the plan JSON to a configured OPA policy server or running rego policies locally via the opa eval command. Policy violations block the pipeline and generate detailed reports. The skill supports Terraform workspaces, remote backends, and module-level change summaries. Output formats include Markdown, JSON, and GitHub Pull Request comments via the GitHub Checks API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-diff-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/
