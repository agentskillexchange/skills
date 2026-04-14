---
title: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
---

# Terraform Plan Validator

The Terraform Plan Validator agent processes the JSON output of terraform plan using the Terraform CLI (terraform show -json planfile) to perform pre-apply validation of infrastructure changes. It identifies destructive operations including resource deletions, replacements, and in-place updates that could cause downtime.

The agent integrates with the Infracost API to estimate cost impacts of planned infrastructure changes, flagging unexpected cost increases above configurable thresholds. It compares the planned state against the desired state defined in HCL files to detect configuration drift and unauthorized manual changes.

For security validation, the agent checks planned resources against Open Policy Agent (OPA) Rego policies to enforce guardrails like encryption requirements, network exposure rules, and tagging compliance. It supports Terraform workspaces, remote state backends (S3, GCS, Azure Blob), and module-level change isolation. Output includes a structured approval report with risk scores per resource change.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
