---
name: "AWS CloudFormation Stack Diagnostics"
slug: "aws-cloudformation-stack-diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
verification: "listed"
source: "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html"
author: "Amazon Web Services"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
---

# AWS CloudFormation Stack Diagnostics

Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/)
