---
title: Terraform State Drift Detector
description: Terraform State Drift Detector identifies discrepancies between your
  Terraform state and actual cloud infrastructure to prevent configuration drift.
  How It Works The skill runs terraform plan -detailed-exitcode to detect changes,
  then parses the structured output via terraform show -json to categorize and prioritize
  drift by resource type, severity, and blast radius. Key Features Drift categorization
  by resource type (compute, network, IAM, storage) with severity scoring Blast radius
  analysis estimating the impact of reconciliation applies Selective reconciliation
  plans using terraform apply -target for surgical fixes Support for Terraform workspaces,
  remote backends (S3, GCS, Azure Blob), and Terraform Cloud Scheduling Designed for
  scheduled drift detection runs. Maintains a drift history log for trend analysis.
  Alerts on critical drift like IAM policy changes or security group modifications.
  Compatible with OpenTofu and Terragrunt configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-drift-detector/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Terraform State Drift Detector

Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift. How It Works The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius. Key Features Drift categorization by resource type (compute, network, IAM, storage) with severity scoring Blast radius analysis estimating the impact of reconciliation applies Selective reconciliation plans using terraform apply -target for surgical fixes Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud Scheduling Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
