---
name: "Terraform Cloud Run Inspector"
description: "Queries the Terraform Cloud API to inspect plan outputs, apply logs, and state file changes. Analyzes resource diffs including module-level changes, provider version constraints, and Sentinel policy evaluation results."
category: "Integrations & Connectors"
framework: "OpenClaw"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-cloud-run-inspector-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Cloud Run Inspector

Queries the Terraform Cloud API to inspect plan outputs, apply logs, and state file changes. Analyzes resource diffs including module-level changes, provider version constraints, and Sentinel policy evaluation results.

## Overview

The Terraform Cloud Run Inspector skill connects to HashiCorp Terraform Cloud or Terraform Enterprise API to provide detailed infrastructure change analysis. It authenticates via team or user API tokens and queries workspace runs to fetch plan summaries, structured plan output in JSON, and apply logs. The skill parses terraform plan output to categorize changes by resource type, identify destructive operations like force replacements and deletions, and highlight sensitive attribute modifications. It analyzes module dependency graphs to trace how upstream module changes cascade to dependent resources, checks provider version constraints for compatibility issues, and reviews Sentinel policy check results for governance compliance. Supports VCS-driven and CLI-driven workflow analysis with cost estimation integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-inspector-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-inspector-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-inspector-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-inspector-2 -a codex
```

### OpenClaw

```bash
clawhub install terraform-cloud-run-inspector-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-cloud-run-inspector-2/
