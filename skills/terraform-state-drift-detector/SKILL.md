---
title: "Terraform State Drift Detector"
description: "Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift. How It Works The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius. Key Features Drift categorization by resource type (compute, network, IAM, storage) with severity scoring Blast radius analysis estimating the impact of reconciliation applies Selective reconciliation plans using terraform apply -target for surgical fixes Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud Scheduling Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Drift Detector

Terraform State Drift Detector identifies discrepancies between your Terraform state and actual cloud infrastructure to prevent configuration drift. How It Works The skill runs terraform plan -detailed-exitcode to detect changes, then parses the structured output via terraform show -json to categorize and prioritize drift by resource type, severity, and blast radius. Key Features Drift categorization by resource type (compute, network, IAM, storage) with severity scoring Blast radius analysis estimating the impact of reconciliation applies Selective reconciliation plans using terraform apply -target for surgical fixes Support for Terraform workspaces, remote backends (S3, GCS, Azure Blob), and Terraform Cloud Scheduling Designed for scheduled drift detection runs. Maintains a drift history log for trend analysis. Alerts on critical drift like IAM policy changes or security group modifications. Compatible with OpenTofu and Terragrunt configurations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
