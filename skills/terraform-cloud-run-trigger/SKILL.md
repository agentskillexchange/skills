---
name: "Terraform Cloud Run Trigger"
description: "Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-cloud-run-trigger/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Cloud Run Trigger

Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a cursor
```

### OpenClaw
```bash
clawhub install terraform-cloud-run-trigger
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Custom Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-run-trigger/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
