---
title: "Terraform Drift Detector"
description: "The Terraform Drift Detector skill identifies configuration drift between Terraform-managed infrastructure state and actual cloud resource configurations. It runs terraform plan -detailed-exitcode to detect changes not managed by Terraform, parsing the plan output for resource additions, modifications, and deletions. The skill integrates with Terraform Cloud via the TFC API (workspaces/{id}/runs, state-versions) to access remote state, trigger speculative plans, and compare state versions over time. It supports multi-provider drift detection across AWS (using aws_instance, aws_security_group, aws_iam_role resources), GCP (google_compute_instance, google_project_iam_member), and Azure (azurerm_virtual_machine, azurerm_network_security_group). The detector generates drift reports categorized by severity—critical for security group changes, high for IAM modifications, medium for compute configuration changes—and correlates drift with CloudTrail/Audit Log events to identify the source of out-of-band changes. It supports workspace-level scanning across Terraform Cloud organizations and can trigger remediation runs."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Drift Detector

The Terraform Drift Detector skill identifies configuration drift between Terraform-managed infrastructure state and actual cloud resource configurations. It runs terraform plan -detailed-exitcode to detect changes not managed by Terraform, parsing the plan output for resource additions, modifications, and deletions. The skill integrates with Terraform Cloud via the TFC API (workspaces/{id}/runs, state-versions) to access remote state, trigger speculative plans, and compare state versions over time. It supports multi-provider drift detection across AWS (using aws_instance, aws_security_group, aws_iam_role resources), GCP (google_compute_instance, google_project_iam_member), and Azure (azurerm_virtual_machine, azurerm_network_security_group). The detector generates drift reports categorized by severity—critical for security group changes, high for IAM modifications, medium for compute configuration changes—and correlates drift with CloudTrail/Audit Log events to identify the source of out-of-band changes. It supports workspace-level scanning across Terraform Cloud organizations and can trigger remediation runs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detector-2/)
