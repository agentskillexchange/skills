---
name: "Terraform State Drift Detector"
description: "Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the Terraform Cloud API v2. Generates drift reports with resource-level diffs via terraform show -json output."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.1
reviews: 58
creator: "Marcus Rivera"
creator_handle: "@mrivera"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector-4/"
---
# Terraform State Drift Detector

Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the Terraform Cloud API v2. Generates drift reports with resource-level diffs via terraform show -json output.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-4 -a cursor
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector-4
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-4 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | 4.1/5 (58 reviews) |

## Creator

**Marcus Rivera** (Verified Creator ✓)
- Profile: [@mrivera](https://agentskillexchange.com/browse-skills/?creator=mrivera)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector-4/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
