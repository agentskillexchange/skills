---
title: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Diff Reviewer

The Terraform Plan Diff Reviewer skill ingests terraform plan -json output and performs semantic analysis on proposed infrastructure changes. It categorizes each resource change by risk level, flagging destructive operations like database deletions, security group rule removals, and IAM policy modifications. The skill integrates with the Terraform Cloud API v2 to compare planned changes against the current workspace state and previous successful applies. It detects drift between the plan and actual cloud provider state using terraform show output. For AWS resources, it cross-references security group changes against known CIDR ranges and flags overly permissive ingress rules. The tool generates a human-readable diff summary with color-coded risk indicators, affected resource dependency graphs, and rollback plan suggestions. It supports HCL module analysis to trace changes back to their source module definitions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-diff-reviewer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-diff-reviewer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
