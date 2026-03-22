---
name: "Terraform Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the output via the Terraform JSON plan format. Categorizes changes by resource type and severity, integrating with PagerDuty API for critical drift alerts."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: "verified_metadata"
rating: 4.3
reviews: 78
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/terraform-drift-detector-3/"
---

# Terraform Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the output via the Terraform JSON plan format. Categorizes changes by resource type and severity, integrating with PagerDuty API for critical drift alerts.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install terraform-drift-detector-3
```

### Claude Code
```bash
claude mcp add terraform-drift-detector-3
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "terraform-drift-detector-3": {
    "source": "agentskillexchange"
  }
}
```

### OpenClaw
```bash
clawhub install terraform-drift-detector-3
```

### Codex
```bash
codex install terraform-drift-detector-3
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | ✅ Verified |
| **Rating** | ⭐⭐⭐⭐ 4.3/5 (78 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-drift-detector-3/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
