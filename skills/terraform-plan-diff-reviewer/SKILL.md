---
name: Terraform Plan Diff Reviewer
description: Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.0
reviews: 85
source: https://agentskillexchange.com/skill/terraform-plan-diff-reviewer/
---

# Terraform Plan Diff Reviewer

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Overview

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-diff-reviewer
```

### OpenClaw

```bash
clawhub install terraform-plan-diff-reviewer
```

### Claude Code

```bash
claude mcp add terraform-plan-diff-reviewer
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-plan-diff-reviewer/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.0/5 (85 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-plan-diff-reviewer/)
