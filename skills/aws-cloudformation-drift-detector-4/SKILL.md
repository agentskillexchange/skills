---
title: "AWS CloudFormation Drift Detector"
description: "Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
---

# AWS CloudFormation Drift Detector

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.

The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.

Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/)
