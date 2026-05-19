---
name: "Terraform Plan & Apply Automation"
slug: "terraform-plan-apply-automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
github_stars: 48121
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
author: "HashiCorp"
category: "CI/CD Integrations"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48121
---

# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

Basic usage or getting-started notes:
- Documentation is available on the [Terraform website](https://developer.hashicorp.com/terraform):
- [Introduction](https://developer.hashicorp.com/terraform/intro)
- [Documentation](https://developer.hashicorp.com/terraform/docs)

- Source: https://github.com/hashicorp/terraform
- Extracted from upstream docs: https://raw.githubusercontent.com/hashicorp/terraform/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
