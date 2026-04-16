---
title: "Terraform Module Boilerplate Assembler"
description: "Generates Terraform module scaffolds with variables.tf, outputs.tf, and provider configurations from a module specification. Uses the Terraform Registry API to resolve provider schemas."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates & Workflows"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48004
---

# Terraform Module Boilerplate Assembler

The Terraform Module Boilerplate Assembler generates production-ready Terraform module scaffolds from high-level specifications. Given a target cloud provider and resource type, it queries the Terraform Registry API at registry.terraform.io to fetch provider schemas and resource documentation, then generates a complete module structure including main.tf, variables.tf, outputs.tf, versions.tf, and a README.md following HashiCorp’s standard module structure guidelines. Variable definitions are generated with appropriate types, descriptions, default values, and validation blocks inferred from the provider schema. The skill creates example/ directories with sample tfvars files and a working root module that references the generated child module. It adds pre-commit hooks configuration for terraform fmt, terraform validate, and tflint integration. Backend configuration templates are generated for popular backends including S3, GCS, and Azure Blob Storage with appropriate state locking configuration. The skill also generates GitHub Actions or GitLab CI pipeline templates for terraform plan and apply stages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-boilerplate-assembler/)
