---
title: Terraform Plan Diff Reviewer
description: The Terraform Plan Diff Reviewer skill ingests terraform plan -json output
  and performs semantic analysis on proposed infrastructure changes. It categorizes
  each resource change by risk level, flagging destructive operations like database
  deletions, security group rule removals, and IAM policy modifications. The skill
  integrates with the Terraform Cloud API v2 to compare planned changes against the
  current workspace state and previous successful applies. It detects drift between
  the plan and actual cloud provider state using terraform show output. For AWS resources,
  it cross-references security group changes against known CIDR ranges and flags overly
  permissive ingress rules. The tool generates a human-readable diff summary with
  color-coded risk indicators, affected resource dependency graphs, and rollback plan
  suggestions. It supports HCL module analysis to trace changes back to their source
  module definitions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Terraform Plan Diff Reviewer

The Terraform Plan Diff Reviewer skill ingests terraform plan -json output and performs semantic analysis on proposed infrastructure changes. It categorizes each resource change by risk level, flagging destructive operations like database deletions, security group rule removals, and IAM policy modifications. The skill integrates with the Terraform Cloud API v2 to compare planned changes against the current workspace state and previous successful applies. It detects drift between the plan and actual cloud provider state using terraform show output. For AWS resources, it cross-references security group changes against known CIDR ranges and flags overly permissive ingress rules. The tool generates a human-readable diff summary with color-coded risk indicators, affected resource dependency graphs, and rollback plan suggestions. It supports HCL module analysis to trace changes back to their source module definitions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
