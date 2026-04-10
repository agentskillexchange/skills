---
name: Terraform Plan Diff Reviewer
description: Parses terraform plan JSON output to identify destructive changes, security
  group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace
  state comparison.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
