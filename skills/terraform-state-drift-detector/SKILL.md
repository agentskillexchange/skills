---
name: "Terraform State Drift Detector"
slug: "terraform-state-drift-detector"
description: "Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation."
github_stars: 48146
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

Basic usage or getting-started notes:
- Documentation is available on the [Terraform website](https://developer.hashicorp.com/terraform):
- [Introduction](https://developer.hashicorp.com/terraform/intro)
- [Documentation](https://developer.hashicorp.com/terraform/docs)

- Source: https://github.com/hashicorp/terraform
- Extracted from upstream docs: https://raw.githubusercontent.com/hashicorp/terraform/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-drift-detector/)
