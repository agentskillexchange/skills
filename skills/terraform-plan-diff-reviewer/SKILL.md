---
name: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan Diff Reviewer

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-diff-reviewer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
