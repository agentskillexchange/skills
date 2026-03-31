---
name: "Terraform Cloud Pipeline Agent"
description: "Orchestrates Terraform Cloud run pipelines via the TFC API v2 and tfe provider. Manages workspace variables, Sentinel policy checks, and cost estimation hooks with automatic plan approval workflows."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
---
# Terraform Cloud Pipeline Agent

Orchestrates Terraform Cloud run pipelines via the TFC API v2 and tfe provider. Manages workspace variables, Sentinel policy checks, and cost estimation hooks with automatic plan approval workflows.

## Overview

The Terraform Cloud Pipeline Agent skill provides end-to-end automation of infrastructure deployment pipelines through Terraform Cloud. It interfaces with the TFC API v2 endpoints for workspace management, run triggering, and state inspection.

This skill creates and configures TFC workspaces programmatically using the tfe Terraform provider, setting up VCS connections, variable sets, and run triggers between dependent workspaces. It manages sensitive variables through the Variables API with proper HCL vs string type handling.

For governance, the skill integrates Sentinel policy-as-code frameworks, generating policy sets that enforce tagging standards, allowed instance types, and cost thresholds. It hooks into TFC cost estimation to block runs exceeding budget limits.

The agent monitors run states through the Runs API, handling plan, policy-check, and apply phases. It supports speculative plans for PR previews, auto-apply configurations for staging environments, and manual approval gates for production workspaces with Slack notification integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-pipeline-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-pipeline-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-pipeline-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-pipeline-agent -a codex
```

### OpenClaw

```bash
clawhub install terraform-cloud-pipeline-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-pipeline-agent/)
