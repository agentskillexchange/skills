---
name: "Terraform Plan Validator Agent"
description: "Validates Terraform plans using terraform CLI, tfsec, and Checkov. Detects infrastructure misconfigurations, cost anomalies, and compliance violations before apply."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-validator-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
