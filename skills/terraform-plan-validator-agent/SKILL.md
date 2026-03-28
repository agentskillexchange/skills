---
name: "Terraform Plan Validator Agent"
description: "Validates Terraform plans using terraform CLI, tfsec, and Checkov. Detects infrastructure misconfigurations, cost anomalies, and compliance violations before apply."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_stars: 48003
  github_repo: hashicorp/terraform
  maintained: true
---

# Terraform Plan Validator Agent

Validates Terraform plans using terraform CLI, tfsec, and Checkov. Detects infrastructure misconfigurations, cost anomalies, and compliance violations before apply.

## Overview

The Terraform Plan Validator Agent runs terraform plan with JSON output (-out=plan.bin, terraform show -json plan.bin) and pipes results through tfsec and Checkov for security and compliance validation. It catches misconfigurations before infrastructure changes are applied.

The agent parses the Terraform plan JSON to detect resource additions, modifications, and destructions. It flags high-risk changes like security group rule modifications, IAM policy changes, and public access enablement on storage resources. Cost estimation is performed via Infracost API integration.

Checkov scans cover CIS benchmarks for AWS, Azure, and GCP including encryption at rest, logging enablement, network isolation, and least-privilege IAM. Custom Checkov policies in Python or YAML target organization-specific compliance requirements.

Tfsec rules detect hardcoded credentials, overly permissive security groups, unencrypted data stores, and missing resource tags. The agent generates pull request comments with severity-sorted findings, suggested fixes, and compliance framework mapping (SOC2, HIPAA, PCI-DSS). Failed checks block terraform apply through CI pipeline integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-validator-agent -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-validator-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-validator-agent/
