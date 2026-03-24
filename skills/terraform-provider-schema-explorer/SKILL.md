---
name: "Terraform Provider Schema Explorer"
description: "Explores HashiCorp Terraform provider schemas using terraform providers schema -json output. Maps resource attributes, computed fields, and cross-resource dependency references for HCL generation."
category: "Library & API Reference"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-provider-schema-explorer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Provider Schema Explorer

Explores HashiCorp Terraform provider schemas using terraform providers schema -json output. Maps resource attributes, computed fields, and cross-resource dependency references for HCL generation.

## Overview

The Terraform Provider Schema Explorer parses the JSON schema output from terraform providers schema to build a navigable map of all resource types, data sources, and their attributes. It identifies required versus optional arguments, computed attributes, and sensitive fields across any installed provider. The skill resolves cross-resource references by tracing attribute dependencies—for example, linking aws_subnet.id references to aws_vpc.id through proper data flow. It generates syntactically correct HCL blocks with proper attribute types including nested block structures, sets, and maps. For state management, it understands import block generation and moved block refactoring patterns. The explorer handles provider version constraints, feature flags, and experimental resource warnings. Supports multi-provider configurations with aliased providers and module-level variable passing with validation rules.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-provider-schema-explorer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-provider-schema-explorer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-provider-schema-explorer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-provider-schema-explorer -a codex
```

### OpenClaw

```bash
clawhub install terraform-provider-schema-explorer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-provider-schema-explorer/
