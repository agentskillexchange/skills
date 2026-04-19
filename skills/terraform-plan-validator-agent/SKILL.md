---
title: "Terraform Plan Validator Agent"
description: "The Terraform Plan Validator Agent runs terraform plan with JSON output (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and Checkov for security and compliance validation. It catches misconfigurations before infrastructure changes are applied. The agent parses the Terraform plan JSON to detect resource additions, modifications, and destructions. It flags high-risk changes like security group rule modifications, IAM policy changes, and public access enablement on storage resources. Cost estimation is performed via Infracost API integration. Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption at rest, logging enablement, network isolation, and least-privilege IAM. Custom Checkov policies in Python or YAML target organization-specific compliance requirements. Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted data stores, and missing resource tags. The agent generates pull request comments with severity-sorted findings, suggested fixes, and compliance framework mapping (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline integration."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Validator Agent

The Terraform Plan Validator Agent runs terraform plan with JSON output (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and Checkov for security and compliance validation. It catches misconfigurations before infrastructure changes are applied. The agent parses the Terraform plan JSON to detect resource additions, modifications, and destructions. It flags high-risk changes like security group rule modifications, IAM policy changes, and public access enablement on storage resources. Cost estimation is performed via Infracost API integration. Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption at rest, logging enablement, network isolation, and least-privilege IAM. Custom Checkov policies in Python or YAML target organization-specific compliance requirements. Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted data stores, and missing resource tags. The agent generates pull request comments with severity-sorted findings, suggested fixes, and compliance framework mapping (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline integration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator-agent/)
