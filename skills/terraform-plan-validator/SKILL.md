---
name: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: "verified_metadata"
rating: "4.0"
reviews: "36"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/terraform-plan-validator/"
---

# Terraform Plan Validator

Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state.

## Installation

Install this skill in your agent with one of the following methods:

### Any Agent (npx)
```bash
npx @anthropic/skills install terraform-plan-validator
```

### Claude Code
```bash
claude mcp add terraform-plan-validator
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "terraform-plan-validator": {
    "source": "https://agentskillexchange.com/skill/terraform-plan-validator/"
  }
}
```

### OpenClaw
```bash
clawhub install terraform-plan-validator
```

### Codex
```bash
codex install terraform-plan-validator
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | MCP-compatible |
| **Verification** | Verified Metadata |
| **Rating** | ⭐⭐⭐⭐ 4.0/5 (36 reviews) |

## Creator

**Community**

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-validator/) · [Browse Skills](https://agentskillexchange.com/)
