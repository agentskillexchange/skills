---
name: Terraform Module Scaffold Generator
description: Generates production-ready Terraform module scaffolds with variables.tf,
  outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL).
  Integrates with terraform-docs for automatic README generation and includes pre-configured
  .terraform-version files.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-module-scaffold-generator/
category:
- Templates &amp; Workflows
framework:
- OpenClaw
---
# Terraform Module Scaffold Generator

The Terraform Module Scaffold Generator automates the creation of well-structured Terraform modules following HashiCorp best practices. It generates complete module scaffolds including variables.tf with proper type constraints and validation rules, outputs.tf with meaningful descriptions, main.tf with provider configuration blocks, and versions.tf with terraform version constraints. The tool leverages terraform-docs to automatically generate comprehensive README files from your module code. It supports multi-environment setups with separate tfvars files for dev, staging, and production. Pre-configured .terraform-version files ensure consistent Terraform CLI versions across your team. The generator includes templates for common patterns like VPC modules, ECS services, RDS instances, and S3 bucket configurations. It also creates example directories with working usage examples and integrates with pre-commit hooks for terraform fmt and terraform validate checks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-scaffold-generator/)
