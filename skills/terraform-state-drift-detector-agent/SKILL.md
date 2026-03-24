---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift between Terraform state and actual cloud resources using terraform plan -json output and AWS Config / Azure Resource Graph APIs for cross-validation."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.3
reviews: 16
creator: "Ryan O'Malley"
creator_handle: "@ryanomalley"
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector-agent/"
---

# Terraform State Drift Detector

Detects infrastructure drift between Terraform state and actual cloud resources using terraform plan -json output and AWS Config / Azure Resource Graph APIs for cross-validation.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-agent -a cursor
```

### OpenClaw
```bash
clawhub install terraform-state-drift-detector-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-agent -a codex
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Agents |
| **Verification** | Security Reviewed |
| **Rating** | ⭐ 4.3 (16 reviews) |

## Creator

**Ryan O'Malley**

- Handle: `@ryanomalley`
- Profile: [View on ASE](https://agentskillexchange.com/creator/ryanomalley/)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
