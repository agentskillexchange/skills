---
name: Terraform Plan & Apply Automation
description: Runs terraform plan against changed modules, posts a structured diff
  as a PR comment via GitHub API, and gates terraform apply on reviewer approval.
  Supports S3 and GCS remote state backends with automatic workspace detection. Integrates
  with AWS STS and GCP Workload Identity for short-lived credential injection.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
source: https://github.com/hashicorp/terraform
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48121
  tool: terraform
---
# Terraform Plan & Apply Automation
Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-apply-automation
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-plan-apply-automation` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
