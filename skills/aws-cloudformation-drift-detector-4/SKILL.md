---
title: "AWS CloudFormation Drift Detector"
description: "Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance."
slug: "aws-cloudformation-drift-detector-4"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/"
listed: true
---

# AWS CloudFormation Drift Detector

Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install aws-cloudformation-drift-detector-4
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.
The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.
Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/)
