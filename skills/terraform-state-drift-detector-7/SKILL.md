---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform show and the AWS/GCP/Azure provider APIs. Generates remediation plans automatically."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "security_reviewed"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/terraform-state-drift-detector-7/"
---

# Terraform State Drift Detector

Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform show and the AWS/GCP/Azure provider APIs. Generates remediation plans automatically.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agentskill install terraform-state-drift-detector-7
```

### Claude Code
```bash
claude mcp add terraform-state-drift-detector-7
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "terraform-state-drift-detector-7": {
    "source": "agentskillexchange",
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install terraform-state-drift-detector-7
```

### Codex
```bash
codex install terraform-state-drift-detector-7
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | security_reviewed |
| **Rating** | 0 ⭐ (0 reviews) |

## Creator

**Community** 



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-drift-detector-7/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
