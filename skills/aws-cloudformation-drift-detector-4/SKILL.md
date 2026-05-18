---
name: "AWS CloudFormation Drift Detector"
slug: "aws-cloudformation-drift-detector-4"
description: "Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance."
verification: "listed"
source: "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html"
author: "Amazon Web Services"
category: "Runbooks & Diagnostics"
framework: "Gemini"
---

# AWS CloudFormation Drift Detector

Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance.

## Installation

Requirements and caveats from upstream:
- Resources that support drift detection and allow or require attachments from

Basic usage or getting-started notes:
- the underlying service that created the resource. For example, you can use the Amazon EC2 console
- the stack. For example, if the stack includes an AWS::EC2::Instance
- example, the AWS::EC2::SecurityGroupIngress and

- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html

## Documentation

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/)
