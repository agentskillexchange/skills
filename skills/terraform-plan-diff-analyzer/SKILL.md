---
name: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-diff-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
