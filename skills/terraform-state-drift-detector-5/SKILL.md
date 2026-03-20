---
name: Terraform State Drift Detector
description: Identifies infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the AWS/GCP provider APIs. Generates targeted remediation plans for out-of-sync resources.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.7
reviews: 32
source: https://agentskillexchange.com/skill/terraform-state-drift-detector-5/
---

# Terraform State Drift Detector

Identifies infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the AWS/GCP provider APIs. Generates targeted remediation plans for out-of-sync resources.

## Overview

Identifies infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the AWS/GCP provider APIs. Generates targeted remediation plans for out-of-sync resources.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-5
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector-5
```

### Claude Code

```bash
claude mcp add terraform-state-drift-detector-5
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-state-drift-detector-5/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.7/5 (32 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-drift-detector-5/)
