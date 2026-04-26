---
title: "Terraform Plan Validator"
description: "Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Validator

Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
