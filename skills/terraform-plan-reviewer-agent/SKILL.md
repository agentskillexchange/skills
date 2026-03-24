---
name: "Terraform Plan Reviewer Agent"
description: "Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
rating: 4.6
reviews: 38
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-agent/"
---
# Terraform Plan Reviewer Agent

Parses terraform plan -json output and queries the Terraform Cloud API /runs endpoint to review infrastructure changes. Detects destructive operations, estimates cost impact via Infracost API, and validates against OPA policies.

## Installation

### Any Agent (npx)
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

### OpenClaw
```bash
clawhub install terraform-plan-reviewer-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-agent -a codex
```
## Details

| Field | Value |
|-------|-------|
| **Category** | CI/CD Integrations |
| **Framework** | Gemini |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.6/5 (38 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-reviewer-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
