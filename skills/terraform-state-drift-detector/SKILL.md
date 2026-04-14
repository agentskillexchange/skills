---
title: "Terraform State Drift Detector"
slug: "terraform-state-drift-detector"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---
# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
