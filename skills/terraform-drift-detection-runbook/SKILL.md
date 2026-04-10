---
name: Terraform Drift Detection Runbook
description: Detects infrastructure drift using terraform plan -detailed-exitcode
  and the Terraform Cloud API. Compares state files against live resources across
  AWS, GCP, and Azure providers.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-drift-detection-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---
# Terraform Drift Detection Runbook

The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode to detect infrastructure drift between Terraform state files and actual cloud resources. It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace management and the AWS, GCP, and Azure provider APIs for resource verification.
The skill executes structured drift detection workflows: terraform init with backend configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable change analysis. It parses the plan JSON to categorize changes as create, update, delete, or replace operations.
Key runbook procedures include: state file analysis using terraform state list and terraform state show for resource inspection, import workflows using terraform import for unmanaged resources, targeted plans with -target for specific resource investigation, and state manipulation using terraform state mv and terraform state rm for state corrections. The runbook supports multi-workspace drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only mode), Sentinel policy check integration, and automated remediation plan generation with approval workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
