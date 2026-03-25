---
name: "Terraform Plan & Apply Automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-apply-automation/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Overview

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-apply-automation
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-apply-automation/
