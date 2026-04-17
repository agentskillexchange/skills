---
name: Terraform Plan Analyzer
description: Analyzes Terraform plan output using the terraform show -json command
  and HCL2 parser library. Detects destructive changes, cost implications via Infracost
  API, and policy violations against Open Policy Agent (OPA) rules.
category: CI/CD Integrations
framework: Claude Code
verification: security_reviewed
source: https://github.com/hashicorp/terraform
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48146
  tool: terraform
  maintained: true
---
# Terraform Plan Analyzer
Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-analyzer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-plan-analyzer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/)
