---
name: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.0
reviews: 85
creator: "Luna Martinez"
creator_handle: "@lunamartinez"
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/"
---
# Terraform Plan Diff Reviewer

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.0/5 (85 reviews) |

## Creator

**Luna Martinez**
- Profile: [@lunamartinez](https://agentskillexchange.com/browse-skills/?creator=lunamartinez)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
