---
name: "Terraform Module Template Generator"
description: "Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files."
category: "Templates &amp; Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-module-template-generator/"
---
# Terraform Module Template Generator

Scaffolds production-ready Terraform modules with HCL templates, variable definitions, and output blocks. Uses the Terraform Registry API to pull module schemas and terraform-docs for auto-generating README files.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-generator/)
