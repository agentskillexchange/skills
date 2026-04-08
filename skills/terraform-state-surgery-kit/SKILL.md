---
title: Terraform State Surgery Kit
description: The Terraform State Surgery Kit skill provides safe, guided state manipulation
  operations for Terraform-managed infrastructure. It wraps terraform state subcommands
  (mv, rm, import, pull, push) with safety checks, automatic backups, and rollback
  capabilities. Before any state modification, the skill creates a backup using terraform
  state pull and stores it with a timestamped filename. It then validates the planned
  operation by running terraform plan to preview the impact of the state change. For
  terraform state mv operations, it verifies both the source and destination resource
  addresses exist in the configuration to prevent orphaned resources. The skill handles
  complex scenarios like refactoring resources across modules (terraform state mv
  module.old.aws_instance.web module.new.aws_instance.web), importing existing infrastructure
  (terraform import with provider-specific import ID formats), and removing resources
  from state without destroying them (terraform state rm for resources managed outside
  Terraform). For teams using Terraform Cloud, the skill integrates with the TFC API
  (v2/workspaces and v2/state-versions endpoints) to lock workspaces during operations,
  download current state versions, and upload modified state. It also supports the
  terraform state replace-provider command for provider migration scenarios, with
  automatic configuration file updates to match the new provider source.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-surgery-kit/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---

# Terraform State Surgery Kit

The Terraform State Surgery Kit skill provides safe, guided state manipulation operations for Terraform-managed infrastructure. It wraps terraform state subcommands (mv, rm, import, pull, push) with safety checks, automatic backups, and rollback capabilities. Before any state modification, the skill creates a backup using terraform state pull and stores it with a timestamped filename. It then validates the planned operation by running terraform plan to preview the impact of the state change. For terraform state mv operations, it verifies both the source and destination resource addresses exist in the configuration to prevent orphaned resources. The skill handles complex scenarios like refactoring resources across modules (terraform state mv module.old.aws_instance.web module.new.aws_instance.web), importing existing infrastructure (terraform import with provider-specific import ID formats), and removing resources from state without destroying them (terraform state rm for resources managed outside Terraform). For teams using Terraform Cloud, the skill integrates with the TFC API (v2/workspaces and v2/state-versions endpoints) to lock workspaces during operations, download current state versions, and upload modified state. It also supports the terraform state replace-provider command for provider migration scenarios, with automatic configuration file updates to match the new provider source.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-surgery-kit/)
