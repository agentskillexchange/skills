---
title: Terraform Cloud Pipeline Agent
description: The Terraform Cloud Pipeline Agent skill provides end-to-end automation
  of infrastructure deployment pipelines through Terraform Cloud. It interfaces with
  the TFC API v2 endpoints for workspace management, run triggering, and state inspection.
  This skill creates and configures TFC workspaces programmatically using the tfe
  Terraform provider, setting up VCS connections, variable sets, and run triggers
  between dependent workspaces. It manages sensitive variables through the Variables
  API with proper HCL vs string type handling. For governance, the skill integrates
  Sentinel policy-as-code frameworks, generating policy sets that enforce tagging
  standards, allowed instance types, and cost thresholds. It hooks into TFC cost estimation
  to block runs exceeding budget limits. The agent monitors run states through the
  Runs API, handling plan, policy-check, and apply phases. It supports speculative
  plans for PR previews, auto-apply configurations for staging environments, and manual
  approval gates for production workspaces with Slack notification integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# Terraform Cloud Pipeline Agent

The Terraform Cloud Pipeline Agent skill provides end-to-end automation of infrastructure deployment pipelines through Terraform Cloud. It interfaces with the TFC API v2 endpoints for workspace management, run triggering, and state inspection. This skill creates and configures TFC workspaces programmatically using the tfe Terraform provider, setting up VCS connections, variable sets, and run triggers between dependent workspaces. It manages sensitive variables through the Variables API with proper HCL vs string type handling. For governance, the skill integrates Sentinel policy-as-code frameworks, generating policy sets that enforce tagging standards, allowed instance types, and cost thresholds. It hooks into TFC cost estimation to block runs exceeding budget limits. The agent monitors run states through the Runs API, handling plan, policy-check, and apply phases. It supports speculative plans for PR previews, auto-apply configurations for staging environments, and manual approval gates for production workspaces with Slack notification integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/)
