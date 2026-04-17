---
title: "Terraform Plan Analyzer"
description: "The Terraform Plan Analyzer Agent processes Terraform execution plans to identify risks before infrastructure changes are applied. It uses the terraform show -json command to parse plan files into structured JSON, then analyzes resource changes across create, update, and destroy operations.\nThe agent integrates with the Infracost API to estimate cost implications of planned changes, comparing monthly costs before and after modifications across AWS, GCP, and Azure resources. It evaluates plans against organizational policies defined in Open Policy Agent (OPA) Rego rules, checking for compliance with tagging standards, network security group configurations, and IAM permission boundaries.\nFor state management, it queries the Terraform Cloud API /api/v2/state-versions to compare plan changes against current state, detecting potential state lock conflicts and workspace dependency issues. The agent validates provider version constraints using the Terraform Registry API, checks module source integrity via Git commit SHA verification, and produces detailed change summaries compatible with GitHub PR comments via the GitHub Checks API."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Analyzer

The Terraform Plan Analyzer Agent processes Terraform execution plans to identify risks before infrastructure changes are applied. It uses the terraform show -json command to parse plan files into structured JSON, then analyzes resource changes across create, update, and destroy operations.
The agent integrates with the Infracost API to estimate cost implications of planned changes, comparing monthly costs before and after modifications across AWS, GCP, and Azure resources. It evaluates plans against organizational policies defined in Open Policy Agent (OPA) Rego rules, checking for compliance with tagging standards, network security group configurations, and IAM permission boundaries.
For state management, it queries the Terraform Cloud API /api/v2/state-versions to compare plan changes against current state, detecting potential state lock conflicts and workspace dependency issues. The agent validates provider version constraints using the Terraform Registry API, checks module source integrity via Git commit SHA verification, and produces detailed change summaries compatible with GitHub PR comments via the GitHub Checks API.

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
