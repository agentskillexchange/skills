---
title: "Terraform Cloud Run Trigger"
description: "Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Cloud Run Trigger

Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-cloud-run-trigger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-cloud-run-trigger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-cloud-run-trigger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-run-trigger/)
