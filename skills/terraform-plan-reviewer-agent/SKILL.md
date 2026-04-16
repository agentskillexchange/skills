---
title: "Terraform Plan Reviewer Agent"
description: "Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
