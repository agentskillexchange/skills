---
title: Terraform State Forensics Tool
description: The Terraform State Forensics Tool provides deep analysis of Terraform
  infrastructure state for drift detection and resource management. It parses terraform
  state list and terraform state show outputs to build a complete resource dependency
  graph, identifying orphaned resources that exist in state but not in configuration.
  The skill runs terraform plan with machine-readable JSON output to detect infrastructure
  drift, categorizing changes by resource type and severity. It integrates tfsec for
  security scanning of Terraform configurations, mapping findings to CIS benchmark
  controls and generating remediation code snippets. Cost impact analysis uses the
  Infracost API to estimate financial impact of planned changes before apply, with
  breakdown by resource type and monthly projection. Advanced features include state
  migration planning for provider upgrades using terraform state mv commands, import
  block generation for adopting existing infrastructure, and workspace comparison
  for multi-environment drift analysis. The tool also generates Terraform dependency
  graphs using terraform graph with DOT format output for visualization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-forensics-tool/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---

# Terraform State Forensics Tool

The Terraform State Forensics Tool provides deep analysis of Terraform infrastructure state for drift detection and resource management. It parses terraform state list and terraform state show outputs to build a complete resource dependency graph, identifying orphaned resources that exist in state but not in configuration. The skill runs terraform plan with machine-readable JSON output to detect infrastructure drift, categorizing changes by resource type and severity. It integrates tfsec for security scanning of Terraform configurations, mapping findings to CIS benchmark controls and generating remediation code snippets. Cost impact analysis uses the Infracost API to estimate financial impact of planned changes before apply, with breakdown by resource type and monthly projection. Advanced features include state migration planning for provider upgrades using terraform state mv commands, import block generation for adopting existing infrastructure, and workspace comparison for multi-environment drift analysis. The tool also generates Terraform dependency graphs using terraform graph with DOT format output for visualization.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
