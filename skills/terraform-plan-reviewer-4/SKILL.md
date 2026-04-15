---
title: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-reviewer-4
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-plan-reviewer-4` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
