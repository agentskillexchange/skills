---
title: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Validator

The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime.

The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes.

For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
