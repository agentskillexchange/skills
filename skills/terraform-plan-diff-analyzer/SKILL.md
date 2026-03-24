---
name: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
rating: 4.1
reviews: 80
creator: "Priya Sharma"
creator_handle: "@priyasharma"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
---
# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | 4.1/5 (80 reviews) |

## Creator

**Priya Sharma** (Verified Creator ✓)
- Profile: [@priyasharma](https://agentskillexchange.com/browse-skills/?creator=priyasharma)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-diff-analyzer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
