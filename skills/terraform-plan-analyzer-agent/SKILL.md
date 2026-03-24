---
name: "Terraform Plan Analyzer"
description: "Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan Analyzer

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-analyzer-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
