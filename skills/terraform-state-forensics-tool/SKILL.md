---
name: "Terraform State Forensics Tool"
description: "Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis."
category: "Runbooks &amp; Diagnostics"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
---
# Terraform State Forensics Tool

Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis.

## Overview

The Terraform State Forensics Tool provides deep analysis of Terraform infrastructure state for drift detection and resource management. It parses terraform state list and terraform state show outputs to build a complete resource dependency graph, identifying orphaned resources that exist in state but not in configuration.

The skill runs terraform plan with machine-readable JSON output to detect infrastructure drift, categorizing changes by resource type and severity. It integrates tfsec for security scanning of Terraform configurations, mapping findings to CIS benchmark controls and generating remediation code snippets.

Cost impact analysis uses the Infracost API to estimate financial impact of planned changes before apply, with breakdown by resource type and monthly projection. Advanced features include state migration planning for provider upgrades using terraform state mv commands, import block generation for adopting existing infrastructure, and workspace comparison for multi-environment drift analysis. The tool also generates Terraform dependency graphs using terraform graph with DOT format output for visualization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-forensics-tool -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-forensics-tool
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
