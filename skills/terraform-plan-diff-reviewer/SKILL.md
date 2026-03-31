---
name: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
