---
name: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-validator/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan Validator

Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-validator
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | MCP-compatible |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
