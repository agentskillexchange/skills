---
name: "Terraform Plan Reviewer"
description: "Analyzes Terraform plan output using the terraform show -json command and the hashicorp/terraform-json Go SDK. Identifies destructive changes, cost estimates via Infracost API, and policy violations via OPA Rego rules."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: listed
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-3/"
---
# Terraform Plan Reviewer

Analyzes Terraform plan output using the terraform show -json command and the hashicorp/terraform-json Go SDK. Identifies destructive changes, cost estimates via Infracost API, and policy violations via OPA Rego rules.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-3
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-3 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-3 -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-reviewer-3
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-3 -a codex
```
## Details

| Field | Value |
|-------|-------|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** |  |
| **Rating** | 0 |

## Creator

**Community**

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-reviewer-3/) · [Browse All Skills](https://agentskillexchange.com/)
