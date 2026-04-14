---
title: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
