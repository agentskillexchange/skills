---
title: "Terraform Module Registry Browser"
description: "Searches and evaluates Terraform modules from the HashiCorp Registry API and private registries. Uses hcl2json parser to analyze module input variables, outputs, and provider requirements."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates & Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Registry Browser

The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-module-registry-browser
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-module-registry-browser` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-registry-browser/)
