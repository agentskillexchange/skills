---
name: "Terraform State Forensics Tool"
description: "Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: "Verified"
rating: 4.2
reviews: 69
creator: "Elena Rodriguez"
creator_handle: "@elena_dev"
creator_verified: true
source: "https://agentskillexchange.com/skill/terraform-state-forensics-tool/"
---

# Terraform State Forensics Tool

Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis.

## Installation

Install this skill with your preferred agent:

### Any Agent (npx)
```bash
npx @anthropic/skills install terraform-state-forensics-tool
```

### Claude Code
```bash
claude skills add terraform-state-forensics-tool
```

### Cursor
Add to your `.cursor/skills.json`:
```json
{
  "skills": ["terraform-state-forensics-tool"]
}
```

### OpenClaw
```bash
clawhub install terraform-state-forensics-tool
```

### Codex
```bash
codex skills add terraform-state-forensics-tool
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | Verified |
| **Rating** | ⭐⭐⭐⭐ 4.2/5 (69 reviews) |

## Creator

**Elena Rodriguez** @elena_dev
✓ Verified Creator

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-forensics-tool/) · [Browse All Skills](https://agentskillexchange.com/)
