---
title: "Terraform Plan Reviewer Agent"
description: "Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies."
verification: security_reviewed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-reviewer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-plan-reviewer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
