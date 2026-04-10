---
name: "Terraform Provider Schema Explorer"
description: "Explores HashiCorp Terraform provider schemas using terraform providers schema -json output. Maps resource attributes, computed fields, and cross-resource dependency references for HCL generation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-provider-schema-explorer/"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
---

# Terraform Provider Schema Explorer

The Terraform Provider Schema Explorer parses the JSON schema output from terraform providers schema to build a navigable map of all resource types, data sources, and their attributes. It identifies required versus optional arguments, computed attributes, and sensitive fields across any installed provider. The skill resolves cross-resource references by tracing attribute dependencies—for example, linking aws_subnet.id references to aws_vpc.id through proper data flow. It generates syntactically correct HCL blocks with proper attribute types including nested block structures, sets, and maps. For state management, it understands import block generation and moved block refactoring patterns. The explorer handles provider version constraints, feature flags, and experimental resource warnings. Supports multi-provider configurations with aliased providers and module-level variable passing with validation rules.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-provider-schema-explorer/)
