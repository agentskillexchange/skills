---
name: "AWS CloudFormation Drift Detector"
description: "Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS CloudFormation Drift Detector

Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance.

## Overview

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.

The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.

Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector-4
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/
