---
title: "Terraform State Inspector"
description: "The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Inspector

The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
