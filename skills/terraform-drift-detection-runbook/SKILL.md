---
title: "Terraform Drift Detection Runbook"
description: "Detects infrastructure drift using terraform plan -detailed-exitcode and the Terraform Cloud API. Compares state files against live resources across AWS, GCP, and Azure providers."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
---

# Terraform Drift Detection Runbook

The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode to detect infrastructure drift between Terraform state files and actual cloud resources. It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace management and the AWS, GCP, and Azure provider APIs for resource verification.

The skill executes structured drift detection workflows: terraform init with backend configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable change analysis. It parses the plan JSON to categorize changes as create, update, delete, or replace operations.

Key runbook procedures include: state file analysis using terraform state list and terraform state show for resource inspection, import workflows using terraform import for unmanaged resources, targeted plans with -target for specific resource investigation, and state manipulation using terraform state mv and terraform state rm for state corrections. The runbook supports multi-workspace drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only mode), Sentinel policy check integration, and automated remediation plan generation with approval workflows.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
