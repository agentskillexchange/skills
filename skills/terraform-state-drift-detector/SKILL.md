---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a cursor
```

### OpenClaw
```bash
clawhub install terraform-state-drift-detector
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
