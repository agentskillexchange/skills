---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_stars: 48003
  github_repo: hashicorp/terraform
  maintained: true
---
# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Overview

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
