---
name: "Terraform Cloud Orchestrator"
description: "Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-cloud-orchestrator-skill/"
---
# Terraform Cloud Orchestrator

Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks.

Overview

Orchestrates Terraform Cloud runs via the TFC API v2 /runs endpoint with plan-only and auto-apply modes. Manages workspace variables through /vars API, parses plan output for resource drift detection, and integrates Sentinel policy checks.

Key Features

- Automated detection and reporting with structured output formats for downstream integrations

- Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

- Real-time feedback loops integrated into developer workflows for immediate actionable insights

- Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works

Terraform Cloud Orchestrator connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

- Valid API credentials with appropriate read/write scopes for the target service

- Network access to the relevant API endpoints from the agent runtime environment

- Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-orchestrator-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-orchestrator-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-orchestrator-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-orchestrator-skill -a codex
```

### OpenClaw

```bash
clawhub install terraform-cloud-orchestrator-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-orchestrator-skill/)
