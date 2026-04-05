---
name: "Terraform Cloud Run Trigger"
description: "Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-cloud-run-trigger/"
---
# Terraform Cloud Run Trigger

Automates Terraform Cloud workspace runs using the TFC API v2. Creates runs via POST /api/v2/runs with plan-only or auto-apply modes, streams plan output from /api/v2/plans/{id}/log, and manages workspace variables through /api/v2/workspaces/{id}/vars for infrastructure-as-code pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-cloud-run-trigger -a codex
```

### OpenClaw

```bash
clawhub install terraform-cloud-run-trigger
```

## Details

The Terraform Cloud Run Trigger automates infrastructure provisioning workflows through the Terraform Cloud API v2. It manages the full run lifecycle including plan, cost estimation, policy checks, and apply phases for Terraform workspaces.

Run management starts with POST /api/v2/runs to create new runs, supporting plan-only mode for preview, auto-apply for automated deployments, and targeted resource operations via target-addrs. The skill monitors run progress through state polling at /api/v2/runs/{id}, tracking transitions through pending, planning, planned, policy_checked, applying, and applied states.

Plan output is streamed from /api/v2/plans/{id}/log for human-readable change summaries. The agent parses plan output to extract resource counts (add/change/destroy), identifies potentially destructive changes, and generates approval summaries. Cost estimation results from /api/v2/cost-estimates/{id} provide projected spend deltas.

Workspace variable management through /api/v2/workspaces/{id}/vars handles both Terraform variables and environment variables, supporting sensitive values, HCL complex types, and variable sets for cross-workspace sharing. The skill also manages workspace settings including VCS connections, execution mode (remote/agent/local), and trigger patterns.

Advanced features include run triggers for cross-workspace dependencies, Sentinel policy management via /api/v2/policies, state version management for disaster recovery, and workspace tagging for fleet operations across multiple environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-cloud-run-trigger/)
