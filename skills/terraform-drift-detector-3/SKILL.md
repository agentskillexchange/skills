---
name: "Terraform Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the output via the Terraform JSON plan format. Categorizes changes by resource type and severity, integrating with PagerDuty API for critical drift alerts."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: verified_metadata
rating: 4.3
reviews: 78
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-drift-detector-3/"
---
# Terraform Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the output via the Terraform JSON plan format. Categorizes changes by resource type and severity, integrating with PagerDuty API for critical drift alerts.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-3
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-3 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-3 -a cursor
```

### OpenClaw
```bash
clawhub install terraform-drift-detector-3
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-3 -a codex
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

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detector-3/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
