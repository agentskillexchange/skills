---
title: "Terraform Module Template Generator"
description: "Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Template Generator

This skill automates the creation of Terraform infrastructure modules following HashiCorp best practices. It connects to the Terraform Registry API to discover existing module patterns and provider schemas, then generates complete module directories with main.tf, variables.tf, outputs.tf, and versions.tf files. The skill uses terraform-docs to automatically generate comprehensive README documentation including input/output tables, resource listings, and usage examples. It supports multi-environment configurations with workspace-aware variable files, integrates with terraform-validate for syntax checking before committing, and can scaffold CI/CD pipeline configurations for Terraform Cloud or Spacelift. Templates include pre-configured backend blocks for S3, GCS, and Azure Blob storage state management. The generator also creates example tfvars files with sensible defaults and inline documentation for every variable.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-module-template-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-module-template-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-generator/)
