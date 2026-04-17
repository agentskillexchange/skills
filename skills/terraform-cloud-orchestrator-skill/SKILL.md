---
name: Terraform Cloud Orchestrator
description: Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with
  plan-only and auto-apply modes. Manages workspace variables through /vars API, parses
  plan output for resource drift detection, and integrates Sentinel policy checks.
category: CI/CD Integrations
framework: Gemini
verification: security_reviewed
source: https://github.com/hashicorp/terraform
tool_ecosystem:
  github_repo: hashicorp/terraform
  github_stars: 48146
  tool: terraform
  maintained: true
---
# Terraform Cloud Orchestrator
Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-cloud-orchestrator-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-cloud-orchestrator-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-orchestrator-skill/)
