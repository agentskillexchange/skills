---
title: "Terraform Plan Validator"
description: "The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime. The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes. For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Validator

The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime. The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes. For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
