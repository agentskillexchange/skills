---
title: "Terraform State Surgery Kit"
description: "Performs safe Terraform state operations using the terraform CLI state subcommands and the Terraform Cloud API. Handles state imports, resource moves, and taint operations with automatic backup and rollback."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Surgery Kit

Performs safe Terraform state operations using the terraform CLI state subcommands and the Terraform Cloud API. Handles state imports, resource moves, and taint operations with automatic backup and rollback.

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
