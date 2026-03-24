---
name: "Terraform Drift Detector"
description: "Detects infrastructure drift by running terraform plan with -detailed-exitcode and parsing state files using the Terraform CLI and HCP Terraform API. Reports resource-level changes with diff summaries."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.4
reviews: 63
creator: "Kai Nakamura"
creator_handle: "@kainakamura"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-drift-detector/"
---
# Terraform Drift Detector

Detects infrastructure drift by running terraform plan with -detailed-exitcode and parsing state files using the Terraform CLI and HCP Terraform API. Reports resource-level changes with diff summaries.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector -a cursor
```

### OpenClaw

```bash
clawhub install terraform-drift-detector
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.4/5 (63 reviews) |

## Creator

**Kai Nakamura** (Verified Creator ✓)
- Profile: [@kainakamura](https://agentskillexchange.com/browse-skills/?creator=kainakamura)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detector/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
