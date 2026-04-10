---
title: "Terraform Plan Reviewer Agent"
description: "Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies."
slug: "terraform-plan-reviewer-agent"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/"
---

# Terraform Plan Reviewer Agent

Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies.

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
clawhub install terraform-plan-reviewer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Plan Reviewer Agent automates infrastructure-as-code review by parsing the structured JSON output from terraform plan -out=plan.json and terraform show -json plan.json. It categorizes changes into create, update, delete, and replace operations, flagging destructive actions like resource deletion or replacement that could cause downtime. The agent integrates with the Infracost API to estimate monthly cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing the cost breakdown response. For policy enforcement, it evaluates plans against Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing tags, oversized instances, or publicly accessible storage buckets. When connected to Terraform Cloud, it queries /api/v2/runs to compare the current plan against previous applies, identifying drift and unintended state changes. The reviewer generates human-readable summaries with risk scores and approval recommendations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
