---
title: "Terraform Plan & Apply Automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-plan-apply-automation/"
categories:
  - "CI/CD Integrations"
frameworks:
  - "OpenClaw"
---

# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Installation

You can install this skill using one of these methods:

1. Install from Agent Skill Exchange in OpenClaw
2. Install from ClawHub
3. Copy the skill folder into your local skills directory
4. Add it as a git submodule or synced folder in your workspace
5. Use your team or org skill distribution workflow

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
