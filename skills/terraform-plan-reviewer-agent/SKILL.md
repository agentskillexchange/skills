---
title: Terraform Plan Reviewer Agent
description: The Terraform Plan Reviewer Agent automates infrastructure-as-code review
  by parsing the structured JSON output from terraform plan -out=plan.json and terraform
  show -json plan.json. It categorizes changes into create, update, delete, and replace
  operations, flagging destructive actions like resource deletion or replacement that
  could cause downtime. The agent integrates with the Infracost API to estimate monthly
  cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing
  the cost breakdown response. For policy enforcement, it evaluates plans against
  Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing
  tags, oversized instances, or publicly accessible storage buckets. When connected
  to Terraform Cloud, it queries /api/v2/runs to compare the current plan against
  previous applies, identifying drift and unintended state changes. The reviewer generates
  human-readable summaries with risk scores and approval recommendations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/
category:
- CI/CD Integrations
framework:
- Gemini
---

# Terraform Plan Reviewer Agent

The Terraform Plan Reviewer Agent automates infrastructure-as-code review by parsing the structured JSON output from terraform plan -out=plan.json and terraform show -json plan.json. It categorizes changes into create, update, delete, and replace operations, flagging destructive actions like resource deletion or replacement that could cause downtime. The agent integrates with the Infracost API to estimate monthly cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing the cost breakdown response. For policy enforcement, it evaluates plans against Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing tags, oversized instances, or publicly accessible storage buckets. When connected to Terraform Cloud, it queries /api/v2/runs to compare the current plan against previous applies, identifying drift and unintended state changes. The reviewer generates human-readable summaries with risk scores and approval recommendations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
