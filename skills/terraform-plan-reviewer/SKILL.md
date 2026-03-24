---
name: "Terraform Plan Reviewer"
description: "Reviews Terraform plan output to detect risky resource changes, IAM policy drift, and cost anomalies. Parses terraform show JSON output and cross-references with AWS Pricing API."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.9
reviews: 84
creator: "Leo Park"
creator_handle: "@leopark"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer/"
---
# Terraform Plan Reviewer

Reviews Terraform plan output to detect risky resource changes, IAM policy drift, and cost anomalies. Parses terraform show JSON output and cross-references with AWS Pricing API.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer -a cursor
```

### OpenClaw

```bash
clawhub install terraform-plan-reviewer
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.9/5 (84 reviews) |

## Creator

**Leo Park** (Verified Creator ✓)
- Profile: [@leopark](https://agentskillexchange.com/browse-skills/?creator=leopark)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-reviewer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
