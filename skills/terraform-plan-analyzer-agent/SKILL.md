---
title: "Terraform Plan Analyzer"
slug: "terraform-plan-analyzer-agent"
description: "Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Analyzer

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/)
