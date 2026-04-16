---
title: "Terraform Provider Schema Explorer"
description: "Explores HashiCorp Terraform provider schemas using terraform providers schema -json output. Maps resource attributes, computed fields, and cross-resource dependency references for HCL generation."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Provider Schema Explorer

The Terraform Provider Schema Explorer parses the JSON schema output from terraform providers schema to build a navigable map of all resource types, data sources, and their attributes. It identifies required versus optional arguments, computed attributes, and sensitive fields across any installed provider. The skill resolves cross-resource references by tracing attribute dependencies—for example, linking aws_subnet.id references to aws_vpc.id through proper data flow. It generates syntactically correct HCL blocks with proper attribute types including nested block structures, sets, and maps. For state management, it understands import block generation and moved block refactoring patterns. The explorer handles provider version constraints, feature flags, and experimental resource warnings. Supports multi-provider configurations with aliased providers and module-level variable passing with validation rules.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-provider-schema-explorer/)
