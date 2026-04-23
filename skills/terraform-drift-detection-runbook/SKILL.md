---
title: "Terraform Drift Detection Runbook"
description: "Detects infrastructure drift using terraform plan -detailed-exitcode and the Terraform Cloud API. Compares state files against live resources across AWS, GCP, and Azure providers."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Drift Detection Runbook

Detects infrastructure drift using terraform plan -detailed-exitcode and the Terraform Cloud API. Compares state files against live resources across AWS, GCP, and Azure providers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-drift-detection-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-drift-detection-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-drift-detection-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
