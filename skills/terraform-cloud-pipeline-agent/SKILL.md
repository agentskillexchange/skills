---
name: "Terraform Cloud Pipeline Agent"
description: "Orchestrates Terraform Cloud run pipelines via the TFC API v2 and tfe provider. Manages workspace variables, Sentinel policy checks, and cost estimation hooks with automatic plan approval workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# Terraform Cloud Pipeline Agent

The Terraform Cloud Pipeline Agent skill provides end-to-end automation of infrastructure deployment pipelines through Terraform Cloud. It interfaces with the TFC API v2 endpoints for workspace management, run triggering, and state inspection.
This skill creates and configures TFC workspaces programmatically using the tfe Terraform provider, setting up VCS connections, variable sets, and run triggers between dependent workspaces. It manages sensitive variables through the Variables API with proper HCL vs string type handling.
For governance, the skill integrates Sentinel policy-as-code frameworks, generating policy sets that enforce tagging standards, allowed instance types, and cost thresholds. It hooks into TFC cost estimation to block runs exceeding budget limits.
The agent monitors run states through the Runs API, handling plan, policy-check, and apply phases. It supports speculative plans for PR previews, auto-apply configurations for staging environments, and manual approval gates for production workspaces with Slack notification integration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/)
