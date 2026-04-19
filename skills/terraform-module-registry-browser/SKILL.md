---
title: "Terraform Module Registry Browser"
description: "The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Registry Browser

The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-registry-browser/)
