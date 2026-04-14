---
title: "Terraform State Diagnostics"
description: "Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Terraform State Diagnostics

The Terraform State Diagnostics skill provides comprehensive analysis of Terraform state files and workspace configurations. It uses terraform state list, terraform state show, and terraform plan -detailed-exitcode to detect infrastructure drift between declared and actual state.

The skill integrates with the Terraform Cloud API v2 for workspace management, state version retrieval, and run queue inspection. It parses HCL configuration files using the hcl2json converter to map resource dependencies and identify potential circular references or implicit ordering issues.

Key diagnostic capabilities include state lock conflict resolution by inspecting DynamoDB lock tables for AWS backends or Azure Blob lease states, orphaned resource detection by comparing state entries against provider API inventory, and module version compatibility checking against the Terraform Registry API. The skill generates remediation scripts using terraform state mv and terraform state rm with safety confirmations.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-diagnostics/)
