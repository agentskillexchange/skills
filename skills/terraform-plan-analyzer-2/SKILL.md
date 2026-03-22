---
name: "Terraform Plan Analyzer"
description: "Parses terraform plan JSON output to identify destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) Rego rules. Generates human-readable ch..."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: "security_reviewed"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/terraform-plan-analyzer-2/"
---

# Terraform Plan Analyzer

Parses terraform plan JSON output to identify destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) Rego rules. Generates human-readable change summaries for PR reviews.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/skills install terraform-plan-analyzer-2
```

### Claude Code
```bash
claude mcp add terraform-plan-analyzer-2
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "terraform-plan-analyzer-2": {
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install terraform-plan-analyzer-2
```

### Codex
```bash
codex install terraform-plan-analyzer-2
```

## Details

| Field | Value |
|-------|-------|
| **Category** | CI/CD Integrations |
| **Framework** | ChatGPT Agents |
| **Verification** | security_reviewed |
| **Rating** | 0 (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-analyzer-2/)
- [Browse All Skills](https://agentskillexchange.com/)
