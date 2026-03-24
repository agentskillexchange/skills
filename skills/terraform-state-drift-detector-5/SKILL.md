---
name: "Terraform State Drift Detector"
description: "Identifies infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the AWS/GCP provider APIs. Generates targeted remediation plans for out-of-sync resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 4.7
reviews: 32
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skills/terraform-state-drift-detector-5/"
---
# Terraform State Drift Detector

Identifies infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the AWS/GCP provider APIs. Generates targeted remediation plans for out-of-sync resources.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-5
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-5 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-5 -a cursor
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector-5
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-5 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.7/5 (32 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector-5/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
