---
title: AWS CloudFormation Drift Detector
description: The AWS CloudFormation Drift Detector automates infrastructure compliance
  monitoring by continuously checking CloudFormation stacks for configuration drift.
  It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift
  detection status, and retrieves detailed results via DescribeStackResourceDrifts
  for each stack resource. The skill categorizes drift by resource type and modification
  scope, distinguishing between property-level changes and resource deletions. It
  generates remediation CloudFormation template patches that bring drifted resources
  back into compliance, with change set previews before execution. Integration with
  AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check
  and custom Lambda-backed rules for organization-specific policies. The detector
  also interfaces with AWS Systems Manager Parameter Store to track configuration
  baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled
  drift detection across multiple accounts using AWS Organizations StackSets. Reports
  are generated in both JSON and HTML formats for audit documentation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# AWS CloudFormation Drift Detector

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource. The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution. Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/)
