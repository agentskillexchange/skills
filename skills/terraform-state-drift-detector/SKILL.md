---
name: Terraform State Drift Detector
description: Detects infrastructure drift by running terraform plan -detailed-exitcode
  and parsing the JSON output via terraform show -json. Categorizes drift by resource
  type and generates targeted terraform apply plans for reconciliation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-drift-detector/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
