---
title: "Terraform Cloud Pipeline Agent"
description: "Orchestrates Terraform Cloud run pipelines via the TFC API v2 and tfe provider. Manages workspace variables, Sentinel policy checks, and cost estimation hooks with automatic plan approval workflows."
slug: "terraform-cloud-pipeline-agent"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/"
listed: true
---

# Terraform Cloud Pipeline Agent

Orchestrates Terraform Cloud run pipelines via the TFC API v2 and tfe provider. Manages workspace variables, Sentinel policy checks, and cost estimation hooks with automatic plan approval workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install terraform-cloud-pipeline-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Cloud Pipeline Agent skill provides end-to-end automation of infrastructure deployment pipelines through Terraform Cloud. It interfaces with the TFC API v2 endpoints for workspace management, run triggering, and state inspection.
This skill creates and configures TFC workspaces programmatically using the tfe Terraform provider, setting up VCS connections, variable sets, and run triggers between dependent workspaces. It manages sensitive variables through the Variables API with proper HCL vs string type handling.
For governance, the skill integrates Sentinel policy-as-code frameworks, generating policy sets that enforce tagging standards, allowed instance types, and cost thresholds. It hooks into TFC cost estimation to block runs exceeding budget limits.
The agent monitors run states through the Runs API, handling plan, policy-check, and apply phases. It supports speculative plans for PR previews, auto-apply configurations for staging environments, and manual approval gates for production workspaces with Slack notification integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/)
