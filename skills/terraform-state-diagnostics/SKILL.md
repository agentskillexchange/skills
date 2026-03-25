---
name: "Terraform State Diagnostics"
description: "Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-diagnostics/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform State Diagnostics

Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces.

## Overview

The Terraform State Diagnostics skill provides comprehensive analysis of Terraform state files and workspace configurations. It uses terraform state list, terraform state show, and terraform plan -detailed-exitcode to detect infrastructure drift between declared and actual state.

The skill integrates with the Terraform Cloud API v2 for workspace management, state version retrieval, and run queue inspection. It parses HCL configuration files using the hcl2json converter to map resource dependencies and identify potential circular references or implicit ordering issues.

Key diagnostic capabilities include state lock conflict resolution by inspecting DynamoDB lock tables for AWS backends or Azure Blob lease states, orphaned resource detection by comparing state entries against provider API inventory, and module version compatibility checking against the Terraform Registry API. The skill generates remediation scripts using terraform state mv and terraform state rm with safety confirmations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-diagnostics
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-state-diagnostics/
