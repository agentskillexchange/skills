---
title: "Terraform State Forensics Tool"
description: "The Terraform State Forensics Tool provides deep analysis of Terraform infrastructure state for drift detection and resource management. It parses terraform state list and terraform state show outputs to build a complete resource dependency graph, identifying orphaned resources that exist in state but not in configuration. The skill runs terraform plan with machine-readable JSON output to detect infrastructure drift, categorizing changes by resource type and severity. It integrates tfsec for security scanning of Terraform configurations, mapping findings to CIS benchmark controls and generating remediation code snippets. Cost impact analysis uses the Infracost API to estimate financial impact of planned changes before apply, with breakdown by resource type and monthly projection. Advanced features include state migration planning for provider upgrades using terraform state mv commands, import block generation for adopting existing infrastructure, and workspace comparison for multi-environment drift analysis. The tool also generates Terraform dependency graphs using terraform graph with DOT format output for visualization."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Forensics Tool

The Terraform State Forensics Tool provides deep analysis of Terraform infrastructure state for drift detection and resource management. It parses terraform state list and terraform state show outputs to build a complete resource dependency graph, identifying orphaned resources that exist in state but not in configuration. The skill runs terraform plan with machine-readable JSON output to detect infrastructure drift, categorizing changes by resource type and severity. It integrates tfsec for security scanning of Terraform configurations, mapping findings to CIS benchmark controls and generating remediation code snippets. Cost impact analysis uses the Infracost API to estimate financial impact of planned changes before apply, with breakdown by resource type and monthly projection. Advanced features include state migration planning for provider upgrades using terraform state mv commands, import block generation for adopting existing infrastructure, and workspace comparison for multi-environment drift analysis. The tool also generates Terraform dependency graphs using terraform graph with DOT format output for visualization.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
