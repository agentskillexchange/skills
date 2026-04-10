---
name: Terraform Module Registry Browser
description: Searches and evaluates Terraform modules from the HashiCorp Registry
  API and private registries. Uses hcl2json parser to analyze module input variables,
  outputs, and provider requirements.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-module-registry-browser/
category:
- Templates &amp; Workflows
framework:
- MCP
---
# Terraform Module Registry Browser

The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-registry-browser/)
