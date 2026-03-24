---
name: "Terraform Plan Analyzer"
description: "Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Plan Analyzer

Analyzes Terraform plan output using the terraform show -json command and HCL2 parser library. Detects destructive changes, cost implications via Infracost API, and policy violations against Open Policy Agent (OPA) rules.

## Overview

The Terraform Plan Analyzer Agent processes Terraform execution plans to identify risks before infrastructure changes are applied. It uses the terraform show -json command to parse plan files into structured JSON, then analyzes resource changes across create, update, and destroy operations.

The agent integrates with the Infracost API to estimate cost implications of planned changes, comparing monthly costs before and after modifications across AWS, GCP, and Azure resources. It evaluates plans against organizational policies defined in Open Policy Agent (OPA) Rego rules, checking for compliance with tagging standards, network security group configurations, and IAM permission boundaries.

For state management, it queries the Terraform Cloud API /api/v2/state-versions to compare plan changes against current state, detecting potential state lock conflicts and workspace dependency issues. The agent validates provider version constraints using the Terraform Registry API, checks module source integrity via Git commit SHA verification, and produces detailed change summaries compatible with GitHub PR comments via the GitHub Checks API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-analyzer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-analyzer-agent/
