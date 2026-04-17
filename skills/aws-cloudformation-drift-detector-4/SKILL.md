---
title: "AWS CloudFormation Drift Detector"
description: "The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.\nThe skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.\nIntegration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/"
framework:
  - "Gemini"
---

# AWS CloudFormation Drift Detector

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.
The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.
Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudformation-drift-detector-4
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudformation-drift-detector-4` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/)
