---
name: "Terraform Module Scaffold Generator"
description: "Generates production-ready Terraform module scaffolds with variables.tf, outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL). Integrates with terraform-docs for automatic README generation and includes pre-configured .terraform-version files."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-module-scaffold-generator/"
---
# Terraform Module Scaffold Generator

Generates production-ready Terraform module scaffolds with variables.tf, outputs.tf, and provider blocks using the HashiCorp Configuration Language (HCL). Integrates with terraform-docs for automatic README generation and includes pre-configured .terraform-version files.

The Terraform Module Scaffold Generator automates the creation of well-structured Terraform modules following HashiCorp best practices. It generates complete module scaffolds including variables.tf with proper type constraints and validation rules, outputs.tf with meaningful descriptions, main.tf with provider configuration blocks, and versions.tf with terraform version constraints. The tool leverages terraform-docs to automatically generate comprehensive README files from your module code. It supports multi-environment setups with separate tfvars files for dev, staging, and production. Pre-configured .terraform-version files ensure consistent Terraform CLI versions across your team. The generator includes templates for common patterns like VPC modules, ECS services, RDS instances, and S3 bucket configurations. It also creates example directories with working usage examples and integrates with pre-commit hooks for terraform fmt and terraform validate checks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffold-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffold-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffold-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffold-generator -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-scaffold-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-scaffold-generator/)
