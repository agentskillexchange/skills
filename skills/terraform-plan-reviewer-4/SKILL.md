---
name: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-4/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-reviewer-4
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
