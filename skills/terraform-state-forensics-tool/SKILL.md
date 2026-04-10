---
name: Terraform State Forensics Tool
description: Analyzes Terraform state files and plan outputs to detect drift, orphaned
  resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for
  security scanning, and Infracost API for cost impact analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-forensics-tool/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---
# Terraform State Forensics Tool

The Terraform State Forensics Tool provides deep analysis of Terraform infrastructure state for drift detection and resource management. It parses terraform state list and terraform state show outputs to build a complete resource dependency graph, identifying orphaned resources that exist in state but not in configuration.
The skill runs terraform plan with machine-readable JSON output to detect infrastructure drift, categorizing changes by resource type and severity. It integrates tfsec for security scanning of Terraform configurations, mapping findings to CIS benchmark controls and generating remediation code snippets.
Cost impact analysis uses the Infracost API to estimate financial impact of planned changes before apply, with breakdown by resource type and monthly projection. Advanced features include state migration planning for provider upgrades using terraform state mv commands, import block generation for adopting existing infrastructure, and workspace comparison for multi-environment drift analysis. The tool also generates Terraform dependency graphs using terraform graph with DOT format output for visualization.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
