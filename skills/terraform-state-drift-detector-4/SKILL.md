---
name: Terraform State Drift Detector
description: Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the Terraform Cloud API v2. Generates drift reports with resource-level diffs via terraform show -json output.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.1
reviews: 58
source: https://agentskillexchange.com/skill/terraform-state-drift-detector-4/
---

# Terraform State Drift Detector

Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the Terraform Cloud API v2. Generates drift reports with resource-level diffs via terraform show -json output.

## Overview

Detects infrastructure drift by comparing Terraform state files against live cloud resources using terraform plan -detailed-exitcode and the Terraform Cloud API v2. Generates drift reports with resource-level diffs via terraform show -json output.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector-4
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector-4
```

### Claude Code

```bash
claude mcp add terraform-state-drift-detector-4
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-state-drift-detector-4/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.1/5 (58 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-drift-detector-4/)
