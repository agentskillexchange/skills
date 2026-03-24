---
name: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
rating: 4.9
reviews: 86
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-4/"
---
# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-reviewer-4
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a codex
```
## Details

| Property | Value |
|----------|-------|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Code |
| **Verification** | Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.9/5 (86 reviews) |

## Creator

**Community**



[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/) · [Browse All Skills](https://agentskillexchange.com/)
