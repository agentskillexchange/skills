---
title: "Terraform Plan Analyzer"
description: "Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Analyzer

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-analyzer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-analyzer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/)
