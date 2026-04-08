---
title: Terraform State Diagnostics
description: The Terraform State Diagnostics skill provides comprehensive analysis
  of Terraform state files and workspace configurations. It uses terraform state list,
  terraform state show, and terraform plan -detailed-exitcode to detect infrastructure
  drift between declared and actual state. The skill integrates with the Terraform
  Cloud API v2 for workspace management, state version retrieval, and run queue inspection.
  It parses HCL configuration files using the hcl2json converter to map resource dependencies
  and identify potential circular references or implicit ordering issues. Key diagnostic
  capabilities include state lock conflict resolution by inspecting DynamoDB lock
  tables for AWS backends or Azure Blob lease states, orphaned resource detection
  by comparing state entries against provider API inventory, and module version compatibility
  checking against the Terraform Registry API. The skill generates remediation scripts
  using terraform state mv and terraform state rm with safety confirmations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-diagnostics/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Terraform State Diagnostics

The Terraform State Diagnostics skill provides comprehensive analysis of Terraform state files and workspace configurations. It uses terraform state list, terraform state show, and terraform plan -detailed-exitcode to detect infrastructure drift between declared and actual state. The skill integrates with the Terraform Cloud API v2 for workspace management, state version retrieval, and run queue inspection. It parses HCL configuration files using the hcl2json converter to map resource dependencies and identify potential circular references or implicit ordering issues. Key diagnostic capabilities include state lock conflict resolution by inspecting DynamoDB lock tables for AWS backends or Azure Blob lease states, orphaned resource detection by comparing state entries against provider API inventory, and module version compatibility checking against the Terraform Registry API. The skill generates remediation scripts using terraform state mv and terraform state rm with safety confirmations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-diagnostics/)
