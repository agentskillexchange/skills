---
title: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
slug: "terraform-plan-validator"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-plan-validator/"
listed: true
---

# Terraform Plan Validator

Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state.

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
clawhub install terraform-plan-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime.
The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes.
For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
