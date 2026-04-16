---
title: "Terraform Module Template Generator"
description: "Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Template Generator

This skill automates the creation of Terraform infrastructure modules following HashiCorp best practices. It connects to the Terraform Registry API to discover existing module patterns and provider schemas, then generates complete module directories with main.tf, variables.tf, outputs.tf, and versions.tf files. The skill uses terraform-docs to automatically generate comprehensive README documentation including input/output tables, resource listings, and usage examples. It supports multi-environment configurations with workspace-aware variable files, integrates with terraform-validate for syntax checking before committing, and can scaffold CI/CD pipeline configurations for Terraform Cloud or Spacelift. Templates include pre-configured backend blocks for S3, GCS, and Azure Blob storage state management. The generator also creates example tfvars files with sensible defaults and inline documentation for every variable.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-generator/)
