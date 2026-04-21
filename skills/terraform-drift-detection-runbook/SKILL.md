---
title: "Terraform Drift Detection Runbook"
slug: "terraform-drift-detection-runbook"
description: "Detects infrastructure drift using terraform plan -detailed-exitcode and the Terraform Cloud API. Compares state files against live resources across AWS, GCP, and Azure providers."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Drift Detection Runbook

Detects infrastructure drift using terraform plan -detailed-exitcode and the Terraform Cloud API. Compares state files against live resources across AWS, GCP, and Azure providers.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detection-runbook/)
