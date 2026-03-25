---
name: "Terraform Module Template Generator"
description: "Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-module-template-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 48003  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Module Template Generator

Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files.

## Overview

This skill automates the creation of Terraform infrastructure modules following HashiCorp best practices. It connects to the Terraform Registry API to discover existing module patterns and provider schemas, then generates complete module directories with main.tf, variables.tf, outputs.tf, and versions.tf files. The skill uses terraform-docs to automatically generate comprehensive README documentation including input/output tables, resource listings, and usage examples. It supports multi-environment configurations with workspace-aware variable files, integrates with terraform-validate for syntax checking before committing, and can scaffold CI/CD pipeline configurations for Terraform Cloud or Spacelift. Templates include pre-configured backend blocks for S3, GCS, and Azure Blob storage state management. The generator also creates example tfvars files with sensible defaults and inline documentation for every variable.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-generator -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-template-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-module-template-generator/
