---
name: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: "Security Reviewed"
rating: "4.9"
reviews: "86"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/terraform-plan-reviewer-4/"
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

Install this skill across different AI coding agents:

### Any Agent (npx)
```bash
npx @anthropic/skills install terraform-plan-reviewer-4
```

### Claude Code
```bash
claude skills add terraform-plan-reviewer-4
```

### Cursor
Add to your `.cursor/skills` configuration:
```json
{
  "skills": ["terraform-plan-reviewer-4"]
}
```

### OpenClaw
```bash
clawhub install terraform-plan-reviewer-4
```

### Codex
```bash
codex skills add terraform-plan-reviewer-4
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



[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-reviewer-4/) · [Browse All Skills](https://agentskillexchange.com/)
