---
title: "Terraform Plan &amp; Apply Automation"
slug: "terraform-plan-apply-automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
tool_ecosystem:
  github_repo: "https://github.com/hashicorp/terraform"
  github_stars: 48121
---

# Terraform Plan &amp; Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
