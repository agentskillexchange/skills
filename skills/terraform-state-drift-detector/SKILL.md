---
title: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Drift Detector

Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift. How It Works The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius. Key Features Drift categorization by resource type (compute, network, IAM, storage) with severity scoring Blast radius analysis estimating the impact of reconciliation applies Selective reconciliation plans using terraform apply -target for surgical fixes Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud Scheduling Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-state-drift-detector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-drift-detector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-state-drift-detector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
