---
name: "Terraform Module Registry Browser"
description: "Searches and evaluates Terraform modules from the HashiCorp Registry API and private registries. Uses hcl2json parser to analyze module input variables, outputs, and provider requirements."
category: "Templates & Workflows"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-module-registry-browser/"
tool_ecosystem:
  tool: terraform
  github_stars: 48003
  github_repo: hashicorp/terraform
  maintained: true
---

# Terraform Module Registry Browser

Searches and evaluates Terraform modules from the HashiCorp Registry API and private registries. Uses hcl2json parser to analyze module input variables, outputs, and provider requirements.

## Overview

The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-registry-browser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-registry-browser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-registry-browser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-registry-browser -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-registry-browser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-module-registry-browser/
