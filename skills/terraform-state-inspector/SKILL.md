---
title: Terraform State Inspector
description: Inspects and diagnoses Terraform state files using terraform CLI commands
  and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency
  cycles in state data.
verification: security_reviewed
source: https://github.com/hashicorp/terraform
category:
- Runbooks & Diagnostics
framework:
- Gemini
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48146
---

# Terraform State Inspector

Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-state-inspector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-inspector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-state-inspector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
