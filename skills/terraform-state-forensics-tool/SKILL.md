---
name: "Terraform State Forensics Tool"
description: "Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-forensics-tool/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform State Forensics Tool

Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a cursor
```

### OpenClaw
```bash
clawhub install terraform-state-forensics-tool
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
