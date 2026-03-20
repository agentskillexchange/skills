---
name: AWS CloudFormation Drift Detector
description: Detects and reports configuration drift in AWS CloudFormation stacks using the detect-stack-drift and describe-stack-resource-drifts APIs via boto3. Generates remediation templates using cfn-flip for YAML/JSON conversion.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.5
reviews: 86
source: https://agentskillexchange.com/skill/aws-cloudformation-drift-detector-2/
---

# AWS CloudFormation Drift Detector

Detects and reports configuration drift in AWS CloudFormation stacks using the detect-stack-drift and describe-stack-resource-drifts APIs via boto3. Generates remediation templates using cfn-flip for YAML/JSON conversion.

## Overview

Detects and reports configuration drift in AWS CloudFormation stacks using the detect-stack-drift and describe-stack-resource-drifts APIs via boto3. Generates remediation templates using cfn-flip for YAML/JSON conversion.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-2
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector-2
```

### Claude Code

```bash
claude mcp add aws-cloudformation-drift-detector-2
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/aws-cloudformation-drift-detector-2/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.5/5 (86 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudformation-drift-detector-2/)
