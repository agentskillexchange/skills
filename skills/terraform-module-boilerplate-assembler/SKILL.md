---
name: "Terraform Module Boilerplate Assembler"
description: "Generates Terraform module scaffolds with variables.tf, outputs.tf, and provider configurations from a module specification. Uses the Terraform Registry API to resolve provider schemas."
category: "41"
framework: "25"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-module-boilerplate-assembler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Module Boilerplate Assembler

Generates Terraform module scaffolds with variables.tf, outputs.tf, and provider configurations from a module specification. Uses the Terraform Registry API to resolve provider schemas.

## Overview

The Terraform Module Boilerplate Assembler generates production-ready Terraform module scaffolds from high-level specifications. Given a target cloud provider and resource type, it queries the Terraform Registry API at registry.terraform.io to fetch provider schemas and resource documentation, then generates a complete module structure including main.tf, variables.tf, outputs.tf, versions.tf, and a README.md following HashiCorp’s standard module structure guidelines. Variable definitions are generated with appropriate types, descriptions, default values, and validation blocks inferred from the provider schema. The skill creates example/ directories with sample tfvars files and a working root module that references the generated child module. It adds pre-commit hooks configuration for terraform fmt, terraform validate, and tflint integration. Backend configuration templates are generated for popular backends including S3, GCS, and Azure Blob Storage with appropriate state locking configuration. The skill also generates GitHub Actions or GitLab CI pipeline templates for terraform plan and apply stages.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-boilerplate-assembler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-boilerplate-assembler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-boilerplate-assembler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-boilerplate-assembler -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-boilerplate-assembler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-module-boilerplate-assembler/
