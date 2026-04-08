---
title: Terraform Plan Validator
description: The Terraform Plan Validator agent processes the JSON output of terraform
  plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply
  validation of infrastructure changes. It identifies destructive operations including
  resource deletions, replacements, and in-place updates that could cause downtime.
  The agent integrates with the Infracost API to estimate cost impacts of planned
  infrastructure changes, flagging unexpected cost increases above configurable thresholds.
  It compares the planned state against the desired state defined in HCL files to
  detect configuration drift and unauthorized manual changes. For security validation,
  the agent checks planned resources against Open Policy Agent (OPA) Rego policies
  to enforce guardrails like encryption requirements, network exposure rules, and
  tagging compliance. It supports Terraform workspaces, remote state backends (S3,
  GCS, Azure Blob), and module-level change isolation. Output includes a structured
  approval report with risk scores per resource change.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-validator/
category:
- CI/CD Integrations
framework:
- MCP
---

# Terraform Plan Validator

The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime. The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes. For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
