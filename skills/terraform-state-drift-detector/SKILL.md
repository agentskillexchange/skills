---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: verified_metadata
rating: 4.6
reviews: 86
creator: "Rachel Green"
creator_handle: "@rachelgreen"
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector/"
---
# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Verified Metadata |
| Rating | 4.6/5 (86 reviews) |

## Creator

**Rachel Green**
- Profile: [@rachelgreen](https://agentskillexchange.com/browse-skills/?creator=rachelgreen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-drift-detector/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
