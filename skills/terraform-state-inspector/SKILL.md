---
name: "Terraform State Inspector"
description: "Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-state-inspector/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 48003  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform State Inspector

Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data.

## Overview

The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-inspector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-state-inspector/
