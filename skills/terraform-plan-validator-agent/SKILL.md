---
title: "Terraform Plan Validator Agent"
description: "Validates Terraform plans using terraform CLI, tfsec, and Checkov. Detects infrastructure misconfigurations, cost anomalies, and compliance violations before apply."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Terraform Plan Validator Agent

The Terraform Plan Validator Agent runs terraform plan with JSON output (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and Checkov for security and compliance validation. It catches misconfigurations before infrastructure changes are applied.

The agent parses the Terraform plan JSON to detect resource additions, modifications, and destructions. It flags high-risk changes like security group rule modifications, IAM policy changes, and public access enablement on storage resources. Cost estimation is performed via Infracost API integration.

Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption at rest, logging enablement, network isolation, and least-privilege IAM. Custom Checkov policies in Python or YAML target organization-specific compliance requirements.

Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted data stores, and missing resource tags. The agent generates pull request comments with severity-sorted findings, suggested fixes, and compliance framework mapping (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline integration.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-validator-agent/)
