---
name: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Terraform Plan Diff Analyzer

This skill analyzes Terraform plan output to provide human-readable summaries and policy checks before applying infrastructure changes. It parses the JSON output from terraform show -json or retrieves plan artifacts from the Terraform Cloud API using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources by action type (create, update, delete, replace) and highlights destructive changes with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting the plan JSON to a configured OPA policy server or running rego policies locally via the opa eval command. Policy violations block the pipeline and generate detailed reports. The skill supports Terraform workspaces, remote backends, and module-level change summaries. Output formats include Markdown, JSON, and GitHub Pull Request comments via the GitHub Checks API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
