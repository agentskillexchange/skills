---
title: "Terraform Cloud Run Trigger"
slug: "terraform-cloud-run-trigger"
description: "Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines."
verification: security_reviewed
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

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-run-trigger/)
