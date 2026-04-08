---
title: Terraform Plan Analyzer
description: The Terraform Plan Analyzer Agent processes Terraform execution plans
  to identify risks before infrastructure changes are applied. It uses the terraform
  show -json command to parse plan files into structured JSON, then analyzes resource
  changes across create, update, and destroy operations. The agent integrates with
  the Infracost API to estimate cost implications of planned changes, comparing monthly
  costs before and after modifications across AWS, GCP, and Azure resources. It evaluates
  plans against organizational policies defined in Open Policy Agent (OPA) Rego rules,
  checking for compliance with tagging standards, network security group configurations,
  and IAM permission boundaries. For state management, it queries the Terraform Cloud
  API /api/v2/state-versions to compare plan changes against current state, detecting
  potential state lock conflicts and workspace dependency issues. The agent validates
  provider version constraints using the Terraform Registry API, checks module source
  integrity via Git commit SHA verification, and produces detailed change summaries
  compatible with GitHub PR comments via the GitHub Checks API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# Terraform Plan Analyzer

The Terraform Plan Analyzer Agent processes Terraform execution plans to identify risks before infrastructure changes are applied. It uses the terraform show -json command to parse plan files into structured JSON, then analyzes resource changes across create, update, and destroy operations. The agent integrates with the Infracost API to estimate cost implications of planned changes, comparing monthly costs before and after modifications across AWS, GCP, and Azure resources. It evaluates plans against organizational policies defined in Open Policy Agent (OPA) Rego rules, checking for compliance with tagging standards, network security group configurations, and IAM permission boundaries. For state management, it queries the Terraform Cloud API /api/v2/state-versions to compare plan changes against current state, detecting potential state lock conflicts and workspace dependency issues. The agent validates provider version constraints using the Terraform Registry API, checks module source integrity via Git commit SHA verification, and produces detailed change summaries compatible with GitHub PR comments via the GitHub Checks API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/)
