---
title: Terraform Plan Validator Agent
description: The Terraform Plan Validator Agent runs terraform plan with JSON output
  (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and
  Checkov for security and compliance validation. It catches misconfigurations before
  infrastructure changes are applied. The agent parses the Terraform plan JSON to
  detect resource additions, modifications, and destructions. It flags high-risk changes
  like security group rule modifications, IAM policy changes, and public access enablement
  on storage resources. Cost estimation is performed via Infracost API integration.
  Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption
  at rest, logging enablement, network isolation, and least-privilege IAM. Custom
  Checkov policies in Python or YAML target organization-specific compliance requirements.
  Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted
  data stores, and missing resource tags. The agent generates pull request comments
  with severity-sorted findings, suggested fixes, and compliance framework mapping
  (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline
  integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-validator-agent/
category:
- CI/CD Integrations
framework:
- Cursor
---

# Terraform Plan Validator Agent

The Terraform Plan Validator Agent runs terraform plan with JSON output (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and Checkov for security and compliance validation. It catches misconfigurations before infrastructure changes are applied. The agent parses the Terraform plan JSON to detect resource additions, modifications, and destructions. It flags high-risk changes like security group rule modifications, IAM policy changes, and public access enablement on storage resources. Cost estimation is performed via Infracost API integration. Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption at rest, logging enablement, network isolation, and least-privilege IAM. Custom Checkov policies in Python or YAML target organization-specific compliance requirements. Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted data stores, and missing resource tags. The agent generates pull request comments with severity-sorted findings, suggested fixes, and compliance framework mapping (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator-agent/)
