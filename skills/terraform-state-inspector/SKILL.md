---
name: "Terraform State Inspector"
description: "Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data."
category: "Runbooks &amp; Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
---
# Terraform State Inspector

Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data.

## Overview

The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-state-inspector -a codex
```

### OpenClaw

```bash
clawhub install terraform-state-inspector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
