---
name: "Terraform Plan & Apply Automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: verified_metadata
rating: 4.8
reviews: 47
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-plan-apply-automation/"
---
# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Verified Metadata |
| Rating | 4.8/5 (47 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-apply-automation/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
