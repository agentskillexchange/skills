---
title: "Terraform Plan &amp; Apply Automation"
slug: "terraform-plan-apply-automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48121
---

# Terraform Plan &amp; Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
