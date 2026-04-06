---
name: Terraform Plan Reviewer Agent
description: Parses terraform plan -json output and queries the Terraform Cloud API
  /runs endpoint to review infrastructure changes. Detects destructive operations,
  estimates cost impact via Infracost API, and validates against OPA policies.
category: CI/CD Integrations
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/"
---
# Terraform Plan Reviewer Agent

Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies.

The Terraform Plan Reviewer Agent automates infrastructure-as-code review by parsing the structured JSON output from terraform plan -out=plan.json and terraform show -json plan.json. It categorizes changes into create, update, delete, and replace operations, flagging destructive actions like resource deletion or replacement that could cause downtime. The agent integrates with the Infracost API to estimate monthly cost impact of proposed changes by submitting plan files to /api/v2/plan and parsing the cost breakdown response. For policy enforcement, it evaluates plans against Open Policy Agent (OPA) Rego rules, checking for compliance violations like missing tags, oversized instances, or publicly accessible storage buckets. When connected to Terraform Cloud, it queries /api/v2/runs to compare the current plan against previous applies, identifying drift and unintended state changes. The reviewer generates human-readable summaries with risk scores and approval recommendations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-agent -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-reviewer-agent
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/)
