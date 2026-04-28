---
title: Terraform Plan Reviewer
description: Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec
  Go SDK. Identifies destructive changes, cost implications via Infracost API, and
  generates approval summaries.
verification: security_reviewed
source: https://github.com/hashicorp/terraform
category:
- CI/CD Integrations
framework:
- Claude Code
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48146
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-reviewer-4/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-reviewer-4
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-reviewer-4`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
