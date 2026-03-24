---
name: "Terraform Plan & Apply Automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-apply-automation/"
tool_ecosystem:
  tool: "terraform"
  github_stars: 47996
  npm_weekly_downloads: 0
  github_repo: "hashicorp/terraform"
  license: "NOASSERTION"
  maintained: true
---

# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a cursor
```

### OpenClaw
```bash
clawhub install terraform-plan-apply-automation
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | [terraform](https://github.com/hashicorp/terraform) — ⭐ 48.0k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
