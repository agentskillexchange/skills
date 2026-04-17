---
name: Terraform Plan Validator
description: Parses terraform plan JSON output via the Terraform CLI (terraform show
  -json) to validate infrastructure changes before apply. Detects destructive operations,
  cost estimate impacts via Infracost API, and drift from desired state.
category: CI/CD Integrations
framework: MCP
verification: security_reviewed
source: https://github.com/hashicorp/terraform
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48146
  tool: terraform
  maintained: true
---
# Terraform Plan Validator
Parses terraform plan JSON output via the Terraform CLI (terraform show -json) to validate infrastructure changes before apply. Detects destructive operations, cost estimate impacts via Infracost API, and drift from desired state.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-validator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-plan-validator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator/)
