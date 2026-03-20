---
name: Terraform State Drift Detector
description: Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: verified_metadata
rating: 4.6
reviews: 86
source: https://agentskillexchange.com/skill/terraform-state-drift-detector/
---

# Terraform State Drift Detector

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Overview

Detects infrastructure drift by running terraform plan -detailed-exitcode and parsing the JSON output via terraform show -json. Categorizes drift by resource type and generates targeted terraform apply plans for reconciliation.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-state-drift-detector
```

### OpenClaw

```bash
clawhub install terraform-state-drift-detector
```

### Claude Code

```bash
claude mcp add terraform-state-drift-detector
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-state-drift-detector/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.6/5 (86 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-state-drift-detector/)
