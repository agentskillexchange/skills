---
title: "Terraform Module Scaffold Generator"
description: "Generates production-ready Terraform module scaffolds with variables.tf, outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL). Integrates with terraform-docs for automatic README generation and includes pre-configured .terraform-version files."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Scaffold Generator

The Terraform Module Scaffold Generator automates the creation of well-structured Terraform modules following HashiCorp best practices. It generates complete module scaffolds including variables.tf with proper type constraints and validation rules, outputs.tf with meaningful descriptions, main.tf with provider configuration blocks, and versions.tf with terraform version constraints. The tool leverages terraform-docs to automatically generate comprehensive README files from your module code. It supports multi-environment setups with separate tfvars files for dev, staging, and production. Pre-configured .terraform-version files ensure consistent Terraform CLI versions across your team. The generator includes templates for common patterns like VPC modules, ECS services, RDS instances, and S3 bucket configurations. It also creates example directories with working usage examples and integrates with pre-commit hooks for terraform fmt and terraform validate checks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-module-scaffold-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-module-scaffold-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-module-scaffold-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-scaffold-generator/)
