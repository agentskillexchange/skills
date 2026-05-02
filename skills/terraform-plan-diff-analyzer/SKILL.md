---
title: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Diff Analyzer

This skill analyzes Terraform plan output to provide human-readable summaries and policy checks before applying infrastructure changes. It parses the JSON output from terraform show -json or retrieves plan artifacts from the Terraform Cloud API using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources by action type (create, update, delete, replace) and highlights destructive changes with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting the plan JSON to a configured OPA policy server or running rego policies locally via the opa eval command. Policy violations block the pipeline and generate detailed reports. The skill supports Terraform workspaces, remote backends, and module-level change summaries. Output formats include Markdown, JSON, and GitHub Pull Request comments via the GitHub Checks API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-diff-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-diff-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
