---
name: "Terraform Module Template Generator"
description: "Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-module-template-generator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
---

# Terraform Module Template Generator

This skill automates the creation of Terraform infrastructure modules following HashiCorp best practices. It connects to the Terraform Registry API to discover existing module patterns and provider schemas, then generates complete module directories with main.tf, variables.tf, outputs.tf, and versions.tf files. The skill uses terraform-docs to automatically generate comprehensive README documentation including input/output tables, resource listings, and usage examples. It supports multi-environment configurations with workspace-aware variable files, integrates with terraform-validate for syntax checking before committing, and can scaffold CI/CD pipeline configurations for Terraform Cloud or Spacelift. Templates include pre-configured backend blocks for S3, GCS, and Azure Blob storage state management. The generator also creates example tfvars files with sensible defaults and inline documentation for every variable.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-generator/)
