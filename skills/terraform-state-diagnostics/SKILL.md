---
name: "Terraform State Diagnostics"
description: "Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
---
# Terraform State Diagnostics

Diagnoses Terraform state issues using terraform state commands, the Terraform Cloud API, and HCL parser. Detects drift, orphaned resources, and state lock conflicts across workspaces.

## Overview

The Terraform State Diagnostics skill provides comprehensive analysis of Terraform state files and workspace configurations. It uses terraform state list, terraform state show, and terraform plan -detailed-exitcode to detect infrastructure drift between declared and actual state.

The skill integrates with the Terraform Cloud API v2 for workspace management, state version retrieval, and run queue inspection. It parses HCL configuration files using the hcl2json converter to map resource dependencies and identify potential circular references or implicit ordering issues.

Key diagnostic capabilities include state lock conflict resolution by inspecting DynamoDB lock tables for AWS backends or Azure Blob lease states, orphaned resource detection by comparing state entries against provider API inventory, and module version compatibility checking against the Terraform Registry API. The skill generates remediation scripts using terraform state mv and terraform state rm with safety confirmations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-diagnostics
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-diagnostics/)
