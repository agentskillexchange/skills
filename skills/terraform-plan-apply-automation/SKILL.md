---
name: "Terraform Plan & Apply Automation"
description: "Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection."
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
# Terraform Plan & Apply Automation

Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection.

## Overview

Terraform Plan & Apply Automation is built around Terraform infrastructure as code. The underlying ecosystem is represented by hashicorp/terraform (47,996+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like plans, applies, state, workspaces, providers, Sentinel, cloud runs and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to terraform so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs terraform plan against changed modules, posts a structured diff as a PR comment via GitHub API, and gates terraform apply on reviewer approval. Supports S3 and GCS remote state backends with automatic workspace detection. Integrates with AWS STS and GCP Workload Identity for short-lived credential injection. The implementation typically relies on plans, applies, state, workspaces, providers, Sentinel, cloud runs, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses plans, applies, state, workspaces, providers, Sentinel, cloud runs instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as cloud provisioning, diff review, policy checks, and infra CI/CD.

 Key integration points include cloud provisioning, diff review, policy checks, and infra CI/CD. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-apply-automation -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-apply-automation
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-apply-automation/)
