---
name: Terraform Plan Reviewer
description: Reviews Terraform plan output to detect risky resource changes, IAM policy drift, and cost anomalies. Parses terraform show JSON output and cross-references with AWS Pricing API.
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
rating: 4.9
reviews: 84
source: https://agentskillexchange.com/skill/terraform-plan-reviewer/
---

# Terraform Plan Reviewer

Reviews Terraform plan output to detect risky resource changes, IAM policy drift, and cost anomalies. Parses terraform show JSON output and cross-references with AWS Pricing API.

## Overview

The Terraform Plan Reviewer agent provides intelligent review of Terraform plan outputs before infrastructure changes are applied. It parses the structured JSON output from terraform show to analyze proposed resource modifications, detecting potentially dangerous changes that could cause downtime or security issues.
The agent identifies high-risk operations such as resource replacements that could cause data loss (e.g., RDS instance recreation), security group rule changes that open wide network access, IAM policy modifications that grant excessive permissions, and changes to production-tagged resources during non-maintenance windows. It uses the AWS IAM Policy Simulator API to validate that proposed IAM changes follow least-privilege principles.
Cost analysis is performed by cross-referencing proposed resource configurations with the AWS Pricing API, providing estimated monthly cost deltas for each change. The reviewer understands Terraform state concepts including resource dependencies, lifecycle rules, and module boundaries, enabling it to predict cascading effects of changes across the infrastructure graph.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer
```

### OpenClaw

```bash
openclaw install terraform-plan-reviewer
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (84 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-reviewer/)*
