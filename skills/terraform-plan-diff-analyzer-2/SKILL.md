---
name: Terraform Plan Diff Analyzer
description: Parses terraform plan JSON output using the Terraform CLI show -json command and HashiCorp HCL2 library. Summarizes infrastructure drift, resource changes, and cost impact estimates via the Infracost 
category: CI/CD Integrations
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 51
source: https://agentskillexchange.com/skill/terraform-plan-diff-analyzer-2/
---

# Terraform Plan Diff Analyzer

Parses terraform plan JSON output using the Terraform CLI show -json command and HashiCorp HCL2 library. Summarizes infrastructure drift, resource changes, and cost impact estimates via the Infracost API.

## Overview

The Terraform Plan Diff Analyzer skill processes Terraform plan output to provide human-readable summaries of infrastructure changes. It uses the terraform show -json command to parse plan files into structured JSON format.
The skill leverages the HashiCorp HCL2 Go library bindings to deeply analyze resource configuration changes, detecting attribute modifications, resource replacements, and dependency chain impacts. It classifies changes by risk level based on resource type and modification scope.
Cost impact estimation is provided through integration with the Infracost API, calculating projected monthly cost differences for AWS, GCP, and Azure resources affected by the plan. The skill generates markdown-formatted diff reports suitable for PR comments.
Additional features include detection of potentially dangerous operations like security group rule removals, IAM policy changes, and database instance modifications. It supports Terraform workspaces, remote state backends, and module-level change aggregation.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-analyzer-2
```

### OpenClaw

```bash
openclaw install terraform-plan-diff-analyzer-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (51 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-diff-analyzer-2/)*
