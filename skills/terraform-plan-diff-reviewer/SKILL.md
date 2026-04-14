---
title: "Terraform Plan Diff Reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Terraform Plan Diff Reviewer

The Terraform Plan Diff Reviewer skill ingests terraform plan -json output and performs semantic analysis on proposed infrastructure changes. It categorizes each resource change by risk level, flagging destructive operations like database deletions, security group rule removals, and IAM policy modifications. The skill integrates with the Terraform Cloud API v2 to compare planned changes against the current workspace state and previous successful applies. It detects drift between the plan and actual cloud provider state using terraform show output. For AWS resources, it cross-references security group changes against known CIDR ranges and flags overly permissive ingress rules. The tool generates a human-readable diff summary with color-coded risk indicators, affected resource dependency graphs, and rollback plan suggestions. It supports HCL module analysis to trace changes back to their source module definitions.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
