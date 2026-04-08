---
title: Terraform Provider Schema Explorer
description: The Terraform Provider Schema Explorer parses the JSON schema output
  from terraform providers schema to build a navigable map of all resource types,
  data sources, and their attributes. It identifies required versus optional arguments,
  computed attributes, and sensitive fields across any installed provider. The skill
  resolves cross-resource references by tracing attribute dependencies—for example,
  linking aws_subnet.id references to aws_vpc.id through proper data flow. It generates
  syntactically correct HCL blocks with proper attribute types including nested block
  structures, sets, and maps. For state management, it understands import block generation
  and moved block refactoring patterns. The explorer handles provider version constraints,
  feature flags, and experimental resource warnings. Supports multi-provider configurations
  with aliased providers and module-level variable passing with validation rules.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-provider-schema-explorer/
category:
- Library &amp; API Reference
framework:
- Gemini
---

# Terraform Provider Schema Explorer

The Terraform Provider Schema Explorer parses the JSON schema output from terraform providers schema to build a navigable map of all resource types, data sources, and their attributes. It identifies required versus optional arguments, computed attributes, and sensitive fields across any installed provider. The skill resolves cross-resource references by tracing attribute dependencies—for example, linking aws_subnet.id references to aws_vpc.id through proper data flow. It generates syntactically correct HCL blocks with proper attribute types including nested block structures, sets, and maps. For state management, it understands import block generation and moved block refactoring patterns. The explorer handles provider version constraints, feature flags, and experimental resource warnings. Supports multi-provider configurations with aliased providers and module-level variable passing with validation rules.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-provider-schema-explorer/)
