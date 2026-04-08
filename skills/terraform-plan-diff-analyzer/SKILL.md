---
title: Terraform Plan Diff Analyzer
description: This skill analyzes Terraform plan output to provide human-readable summaries
  and policy checks before applying infrastructure changes. It parses the JSON output
  from terraform show -json or retrieves plan artifacts from the Terraform Cloud API
  using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources
  by action type (create, update, delete, replace) and highlights destructive changes
  with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting
  the plan JSON to a configured OPA policy server or running rego policies locally
  via the opa eval command. Policy violations block the pipeline and generate detailed
  reports. The skill supports Terraform workspaces, remote backends, and module-level
  change summaries. Output formats include Markdown, JSON, and GitHub Pull Request
  comments via the GitHub Checks API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/
category:
- CI/CD Integrations
framework:
- Cursor
---

# Terraform Plan Diff Analyzer

This skill analyzes Terraform plan output to provide human-readable summaries and policy checks before applying infrastructure changes. It parses the JSON output from terraform show -json or retrieves plan artifacts from the Terraform Cloud API using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources by action type (create, update, delete, replace) and highlights destructive changes with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting the plan JSON to a configured OPA policy server or running rego policies locally via the opa eval command. Policy violations block the pipeline and generate detailed reports. The skill supports Terraform workspaces, remote backends, and module-level change summaries. Output formats include Markdown, JSON, and GitHub Pull Request comments via the GitHub Checks API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
