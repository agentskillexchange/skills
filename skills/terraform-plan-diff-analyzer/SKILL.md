---
name: Terraform Plan Diff Analyzer
description: Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.
category: CI/CD Integrations
framework: Any Agent
verification: security_reviewed
rating: 4.1
reviews: 80
source: https://agentskillexchange.com/skill/terraform-plan-diff-analyzer/
---

# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Overview

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer
```

### OpenClaw

```bash
clawhub install terraform-plan-diff-analyzer
```

### Claude Code

```bash
claude mcp add terraform-plan-diff-analyzer
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-plan-diff-analyzer/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.1/5 (80 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-diff-analyzer/)
