---
name: Terraform Plan Analyzer
description: Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.
category: CI/CD Integrations
framework: Any Agent
verification: security_reviewed
rating: 4.9
reviews: 86
source: https://agentskillexchange.com/skill/terraform-plan-analyzer-agent/
---

# Terraform Plan Analyzer

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Overview

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent
```

### OpenClaw

```bash
clawhub install terraform-plan-analyzer-agent
```

### Claude Code

```bash
claude mcp add terraform-plan-analyzer-agent
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-plan-analyzer-agent/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.9/5 (86 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-analyzer-agent/)
