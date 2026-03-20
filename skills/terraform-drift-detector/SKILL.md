---
name: Terraform Drift Detector
description: Detects infrastructure drift by running terraform plan with -detailed-exitcode and parsing state files using the Terraform CLI and HCP Terraform API. Reports resource-level changes with diff summaries.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.4
reviews: 63
source: https://agentskillexchange.com/skill/terraform-drift-detector/
---

# Terraform Drift Detector

Detects infrastructure drift by running terraform plan with -detailed-exitcode and parsing state files using the Terraform CLI and HCP Terraform API. Reports resource-level changes with diff summaries.

## Overview

Detects infrastructure drift by running terraform plan with -detailed-exitcode and parsing state files using the Terraform CLI and HCP Terraform API. Reports resource-level changes with diff summaries.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector
```

### OpenClaw

```bash
clawhub install terraform-drift-detector
```

### Claude Code

```bash
claude mcp add terraform-drift-detector
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/terraform-drift-detector/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.4/5 (63 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/terraform-drift-detector/)
