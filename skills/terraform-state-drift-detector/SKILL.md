---
title: "Terraform State Drift Detector"
description: "Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift.\nHow It Works\nThe skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius.\nKey Features\n\nDrift categorization by resource type (compute, network, IAM, storage) with severity scoring\nBlast radius analysis estimating the impact of reconciliation applies\nSelective reconciliation plans using terraform apply -target for surgical fixes\nSupport for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud\n\nScheduling\nDesigned for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Drift Detector

Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift.
How It Works
The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius.
Key Features

Drift categorization by resource type (compute, network, IAM, storage) with severity scoring
Blast radius analysis estimating the impact of reconciliation applies
Selective reconciliation plans using terraform apply -target for surgical fixes
Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud

Scheduling
Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-drift-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-state-drift-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
