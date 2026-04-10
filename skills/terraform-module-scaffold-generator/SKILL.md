---
title: "Terraform Module Scaffold Generator"
description: "Generates production-ready Terraform module scaffolds with variables.tf, outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL). Integrates with terraform-docs for automatic README generation and includes pre-configured .terraform-version files."
slug: "terraform-module-scaffold-generator"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-module-scaffold-generator/"
---

# Terraform Module Scaffold Generator

Generates production-ready Terraform module scaffolds with variables.tf, outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL). Integrates with terraform-docs for automatic README generation and includes pre-configured .terraform-version files.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install terraform-module-scaffold-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Module Scaffold Generator automates the creation of well-structured Terraform modules following HashiCorp best practices. It generates complete module scaffolds including variables.tf with proper type constraints and validation rules, outputs.tf with meaningful descriptions, main.tf with provider configuration blocks, and versions.tf with terraform version constraints. The tool leverages terraform-docs to automatically generate comprehensive README files from your module code. It supports multi-environment setups with separate tfvars files for dev, staging, and production. Pre-configured .terraform-version files ensure consistent Terraform CLI versions across your team. The generator includes templates for common patterns like VPC modules, ECS services, RDS instances, and S3 bucket configurations. It also creates example directories with working usage examples and integrates with pre-commit hooks for terraform fmt and terraform validate checks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-scaffold-generator/)
