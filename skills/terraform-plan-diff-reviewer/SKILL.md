---
name: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Plan Diff Reviewer

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Overview

The Terraform Plan Diff Reviewer skill ingests terraform plan -json output and performs semantic analysis on proposed infrastructure changes. It categorizes each resource change by risk level, flagging destructive operations like database deletions, security group rule removals, and IAM policy modifications. The skill integrates with the Terraform Cloud API v2 to compare planned changes against the current workspace state and previous successful applies. It detects drift between the plan and actual cloud provider state using terraform show output. For AWS resources, it cross-references security group changes against known CIDR ranges and flags overly permissive ingress rules. The tool generates a human-readable diff summary with color-coded risk indicators, affected resource dependency graphs, and rollback plan suggestions. It supports HCL module analysis to trace changes back to their source module definitions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-diff-reviewer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/
