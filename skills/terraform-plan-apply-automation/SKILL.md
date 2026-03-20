---
name: Terraform Plan & Apply Automation
description: Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with auto
category: CI/CD Integrations
framework: OpenClaw
verification: verified_metadata
rating: 4.8
reviews: 47
source: https://agentskillexchange.com/skill/terraform-plan-apply-automation/
---

# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Overview

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation
```

### OpenClaw

```bash
openclaw install terraform-plan-apply-automation
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (47 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-apply-automation/)*
