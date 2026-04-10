---
title: "Terraform Module Boilerplate Assembler"
description: "Generates Terraform module scaffolds with variables.tf, outputs.tf, and provider configurations from a module specification. Uses the Terraform Registry API to resolve provider schemas."
slug: "terraform-module-boilerplate-assembler"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48004
---

# Terraform Module Boilerplate Assembler

Generates Terraform module scaffolds with variables.tf, outputs.tf, and provider configurations from a module specification. Uses the Terraform Registry API to resolve provider schemas.

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
clawhub install terraform-module-boilerplate-assembler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Module Boilerplate Assembler generates production-ready Terraform module scaffolds from high-level specifications. Given a target cloud provider and resource type, it queries the Terraform Registry API at registry.terraform.io to fetch provider schemas and resource documentation, then generates a complete module structure including main.tf, variables.tf, outputs.tf, versions.tf, and a README.md following HashiCorp’s standard module structure guidelines. Variable definitions are generated with appropriate types, descriptions, default values, and validation blocks inferred from the provider schema. The skill creates example/ directories with sample tfvars files and a working root module that references the generated child module. It adds pre-commit hooks configuration for terraform fmt, terraform validate, and tflint integration. Backend configuration templates are generated for popular backends including S3, GCS, and Azure Blob Storage with appropriate state locking configuration. The skill also generates GitHub Actions or GitLab CI pipeline templates for terraform plan and apply stages.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-boilerplate-assembler/)
