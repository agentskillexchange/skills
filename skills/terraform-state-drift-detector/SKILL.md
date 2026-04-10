---
title: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
slug: "terraform-state-drift-detector"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector/"
---

# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install terraform-state-drift-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift.
How It Works
The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius.
Key Features
- Drift categorization by resource type (compute, network, IAM, storage) with severity scoring
- Blast radius analysis estimating the impact of reconciliation applies
- Selective reconciliation plans using terraform apply -target for surgical fixes
- Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud
Scheduling
Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
