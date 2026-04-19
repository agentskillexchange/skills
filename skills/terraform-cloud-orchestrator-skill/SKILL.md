---
title: "Terraform Cloud Orchestrator"
description: "Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Cloud Orchestrator

Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-cloud-orchestrator-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-cloud-orchestrator-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-cloud-orchestrator-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-orchestrator-skill/)
