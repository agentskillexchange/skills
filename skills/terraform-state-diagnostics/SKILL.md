---
title: "Terraform State Diagnostics"
description: "Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Diagnostics

The Terraform State Diagnostics skill provides comprehensive analysis of Terraform state files and workspace configurations. It uses terraform state list, terraform state show, and terraform plan -detailed-exitcode to detect infrastructure drift between declared and actual state. The skill integrates with the Terraform Cloud API v2 for workspace management, state version retrieval, and run queue inspection. It parses HCL configuration files using the hcl2json converter to map resource dependencies and identify potential circular references or implicit ordering issues. Key diagnostic capabilities include state lock conflict resolution by inspecting DynamoDB lock tables for AWS backends or Azure Blob lease states, orphaned resource detection by comparing state entries against provider API inventory, and module version compatibility checking against the Terraform Registry API. The skill generates remediation scripts using terraform state mv and terraform state rm with safety confirmations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-state-diagnostics/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-diagnostics
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-state-diagnostics`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-diagnostics/)
