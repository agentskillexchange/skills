---
title: Terraform Drift Detection Runbook
description: 'The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode
  to detect infrastructure drift between Terraform state files and actual cloud resources.
  It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace
  management and the AWS, GCP, and Azure provider APIs for resource verification.
  The skill executes structured drift detection workflows: terraform init with backend
  configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode
  (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable
  change analysis. It parses the plan JSON to categorize changes as create, update,
  delete, or replace operations. Key runbook procedures include: state file analysis
  using terraform state list and terraform state show for resource inspection, import
  workflows using terraform import for unmanaged resources, targeted plans with -target
  for specific resource investigation, and state manipulation using terraform state
  mv and terraform state rm for state corrections. The runbook supports multi-workspace
  drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only
  mode), Sentinel policy check integration, and automated remediation plan generation
  with approval workflows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-drift-detection-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# Terraform Drift Detection Runbook

The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode to detect infrastructure drift between Terraform state files and actual cloud resources. It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace management and the AWS, GCP, and Azure provider APIs for resource verification. The skill executes structured drift detection workflows: terraform init with backend configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable change analysis. It parses the plan JSON to categorize changes as create, update, delete, or replace operations. Key runbook procedures include: state file analysis using terraform state list and terraform state show for resource inspection, import workflows using terraform import for unmanaged resources, targeted plans with -target for specific resource investigation, and state manipulation using terraform state mv and terraform state rm for state corrections. The runbook supports multi-workspace drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only mode), Sentinel policy check integration, and automated remediation plan generation with approval workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
