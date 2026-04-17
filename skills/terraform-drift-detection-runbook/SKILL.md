---
title: "Terraform Drift Detection Runbook"
description: "The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode to detect infrastructure drift between Terraform state files and actual cloud resources. It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace management and the AWS, GCP, and Azure provider APIs for resource verification.\nThe skill executes structured drift detection workflows: terraform init with backend configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable change analysis. It parses the plan JSON to categorize changes as create, update, delete, or replace operations.\nKey runbook procedures include: state file analysis using terraform state list and terraform state show for resource inspection, import workflows using terraform import for unmanaged resources, targeted plans with -target for specific resource investigation, and state manipulation using terraform state mv and terraform state rm for state corrections. The runbook supports multi-workspace drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only mode), Sentinel policy check integration, and automated remediation plan generation with approval workflows."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Drift Detection Runbook

The Terraform Drift Detection Runbook skill uses terraform plan -detailed-exitcode to detect infrastructure drift between Terraform state files and actual cloud resources. It integrates with the Terraform Cloud API (app.terraform.io/api/v2) for workspace management and the AWS, GCP, and Azure provider APIs for resource verification.
The skill executes structured drift detection workflows: terraform init with backend configuration (S3, GCS, Azure Blob), terraform plan -out=drift.plan -detailed-exitcode (exit code 2 indicates drift), and terraform show -json drift.plan for machine-readable change analysis. It parses the plan JSON to categorize changes as create, update, delete, or replace operations.
Key runbook procedures include: state file analysis using terraform state list and terraform state show for resource inspection, import workflows using terraform import for unmanaged resources, targeted plans with -target for specific resource investigation, and state manipulation using terraform state mv and terraform state rm for state corrections. The runbook supports multi-workspace drift scanning via the Terraform Cloud API (GET /workspaces, POST /runs with plan-only mode), Sentinel policy check integration, and automated remediation plan generation with approval workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-drift-detection-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-drift-detection-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
