---
title: "Terraform Cloud Run Trigger"
description: "The Terraform Cloud Run Trigger automates infrastructure provisioning workflows through the Terraform Cloud API v2. It manages the full run lifecycle including plan, cost estimation, policy checks, and apply phases for Terraform workspaces. Run management starts with POST /api/v2/runs to create new runs, supporting plan-only mode for preview, auto-apply for automated deployments, and targeted resource operations via target-addrs. The skill monitors run progress through state polling at /api/v2/runs/{id}, tracking transitions through pending, planning, planned, policy_checked, applying, and applied states. Plan output is streamed from /api/v2/plans/{id}/log for human-readable change summaries. The agent parses plan output to extract resource counts (add/change/destroy), identifies potentially destructive changes, and generates approval summaries. Cost estimation results from /api/v2/cost-estimates/{id} provide projected spend deltas. Workspace variable management through /api/v2/workspaces/{id}/vars handles both Terraform variables and environment variables, supporting sensitive values, HCL complex types, and variable sets for cross-workspace sharing. The skill also manages workspace settings including VCS connections, execution mode (remote/agent/local), and trigger patterns. Advanced features include run triggers for cross-workspace dependencies, Sentinel policy management via /api/v2/policies, state version management for disaster recovery, and workspace tagging for fleet operations across multiple environments."
source: "https://github.com/hashicorp/terraform"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Cloud Run Trigger

The Terraform Cloud Run Trigger automates infrastructure provisioning workflows through the Terraform Cloud API v2. It manages the full run lifecycle including plan, cost estimation, policy checks, and apply phases for Terraform workspaces. Run management starts with POST /api/v2/runs to create new runs, supporting plan-only mode for preview, auto-apply for automated deployments, and targeted resource operations via target-addrs. The skill monitors run progress through state polling at /api/v2/runs/{id}, tracking transitions through pending, planning, planned, policy_checked, applying, and applied states. Plan output is streamed from /api/v2/plans/{id}/log for human-readable change summaries. The agent parses plan output to extract resource counts (add/change/destroy), identifies potentially destructive changes, and generates approval summaries. Cost estimation results from /api/v2/cost-estimates/{id} provide projected spend deltas. Workspace variable management through /api/v2/workspaces/{id}/vars handles both Terraform variables and environment variables, supporting sensitive values, HCL complex types, and variable sets for cross-workspace sharing. The skill also manages workspace settings including VCS connections, execution mode (remote/agent/local), and trigger patterns. Advanced features include run triggers for cross-workspace dependencies, Sentinel policy management via /api/v2/policies, state version management for disaster recovery, and workspace tagging for fleet operations across multiple environments.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-run-trigger/)
