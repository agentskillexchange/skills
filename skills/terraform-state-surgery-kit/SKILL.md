---
title: "Terraform State Surgery Kit"
description: "The Terraform State Surgery Kit skill provides safe, guided state manipulation operations for Terraform-managed infrastructure. It wraps terraform state subcommands (mv, rm, import, pull, push) with safety checks, automatic backups, and rollback capabilities.\nBefore any state modification, the skill creates a backup using terraform state pull and stores it with a timestamped filename. It then validates the planned operation by running terraform plan to preview the impact of the state change. For terraform state mv operations, it verifies both the source and destination resource addresses exist in the configuration to prevent orphaned resources.\nThe skill handles complex scenarios like refactoring resources across modules (terraform state mv module.old.aws_instance.web module.new.aws_instance.web), importing existing infrastructure (terraform import with provider-specific import ID formats), and removing resources from state without destroying them (terraform state rm for resources managed outside Terraform).\nFor teams using Terraform Cloud, the skill integrates with the TFC API (v2/workspaces and v2/state-versions endpoints) to lock workspaces during operations, download current state versions, and upload modified state. It also supports the terraform state replace-provider command for provider migration scenarios, with automatic configuration file updates to match the new provider source."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Surgery Kit

The Terraform State Surgery Kit skill provides safe, guided state manipulation operations for Terraform-managed infrastructure. It wraps terraform state subcommands (mv, rm, import, pull, push) with safety checks, automatic backups, and rollback capabilities.
Before any state modification, the skill creates a backup using terraform state pull and stores it with a timestamped filename. It then validates the planned operation by running terraform plan to preview the impact of the state change. For terraform state mv operations, it verifies both the source and destination resource addresses exist in the configuration to prevent orphaned resources.
The skill handles complex scenarios like refactoring resources across modules (terraform state mv module.old.aws_instance.web module.new.aws_instance.web), importing existing infrastructure (terraform import with provider-specific import ID formats), and removing resources from state without destroying them (terraform state rm for resources managed outside Terraform).
For teams using Terraform Cloud, the skill integrates with the TFC API (v2/workspaces and v2/state-versions endpoints) to lock workspaces during operations, download current state versions, and upload modified state. It also supports the terraform state replace-provider command for provider migration scenarios, with automatic configuration file updates to match the new provider source.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-surgery-kit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-state-surgery-kit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-surgery-kit/)
