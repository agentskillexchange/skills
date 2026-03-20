---
name: AWS CloudFormation Drift Detector
description: Detects infrastructure drift in AWS CloudFormation stacks using the AWS SDK boto3 detect_stack_drift API. Compares actual resource configurations against template definitions and generates remediation changesets.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 24
source: https://agentskillexchange.com/skill/aws-cloudformation-drift-detector/
---

# AWS CloudFormation Drift Detector

Detects infrastructure drift in AWS CloudFormation stacks using the AWS SDK boto3 detect_stack_drift API. Compares actual resource configurations against template definitions and generates remediation changesets.

## Overview

Detects infrastructure drift in AWS CloudFormation stacks using the AWS SDK boto3 detect_stack_drift API. Compares actual resource configurations against template definitions and generates remediation changesets.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector
```

### Claude Code

```bash
claude mcp add aws-cloudformation-drift-detector
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/aws-cloudformation-drift-detector/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.3/5 (24 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudformation-drift-detector/)
