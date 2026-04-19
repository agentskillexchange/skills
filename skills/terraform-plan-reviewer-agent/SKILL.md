---
title: "Terraform Plan Reviewer Agent"
description: "The Terraform Plan Reviewer Agent automates infrastructure-as-code review by parsing the structured JSON output from terraform plan -out=plan.json and terraform show -json plan.json. It categorizes changes into create, update, delete, and replace operations, flagging destructive actions like resource deletion or replacement that could cause downtime. The agent integrates with the Infracost API to estimate monthly cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing the cost breakdown response. For policy enforcement, it evaluates plans against Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing tags, oversized instances, or publicly accessible storage buckets. When connected to Terraform Cloud, it queries /api/v2/runs to compare the current plan against previous applies, identifying drift and unintended state changes. The reviewer generates human-readable summaries with risk scores and approval recommendations."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Reviewer Agent

The Terraform Plan Reviewer Agent automates infrastructure-as-code review by parsing the structured JSON output from terraform plan -out=plan.json and terraform show -json plan.json. It categorizes changes into create, update, delete, and replace operations, flagging destructive actions like resource deletion or replacement that could cause downtime. The agent integrates with the Infracost API to estimate monthly cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing the cost breakdown response. For policy enforcement, it evaluates plans against Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing tags, oversized instances, or publicly accessible storage buckets. When connected to Terraform Cloud, it queries /api/v2/runs to compare the current plan against previous applies, identifying drift and unintended state changes. The reviewer generates human-readable summaries with risk scores and approval recommendations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
