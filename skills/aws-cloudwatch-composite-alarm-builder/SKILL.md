---
title: "AWS CloudWatch Composite Alarm Builder"
description: "The AWS CloudWatch Composite Alarm Builder constructs sophisticated multi-signal alerting rules by combining existing CloudWatch metric alarms into composite expressions. Using the AWS CloudWatch PutCompositeAlarm API, it creates alarm rules using boolean logic (ALARM, OK, INSUFFICIENT_DATA states combined with AND, OR, NOT operators). The skill queries existing alarms via DescribeAlarms to build a dependency graph of available signals, then guides construction of composite rule expressions. It supports nested composition where composite alarms reference other composite alarms for hierarchical alerting patterns. Each composite alarm is configured with SNS topic actions for state transitions via the AlarmActions, OKActions, and InsufficientDataActions parameters. The builder validates rule expressions against the CloudWatch rule expression grammar before deployment, catching syntax errors and circular references. It includes a simulation mode that evaluates the composite expression against historical alarm state data from CloudWatch alarm history via DescribeAlarmHistory. Integration with AWS Systems Manager OpsCenter allows automatic OpsItem creation when composite alarms fire. The skill manages alarm tags via TagResource for cost allocation and supports cross-account alarm references using ARN-based alarm identifiers."
source: "https://github.com/aws/aws-sdk-js-v3"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Composite Alarm Builder

The AWS CloudWatch Composite Alarm Builder constructs sophisticated multi-signal alerting rules by combining existing CloudWatch metric alarms into composite expressions. Using the AWS CloudWatch PutCompositeAlarm API, it creates alarm rules using boolean logic (ALARM, OK, INSUFFICIENT_DATA states combined with AND, OR, NOT operators). The skill queries existing alarms via DescribeAlarms to build a dependency graph of available signals, then guides construction of composite rule expressions. It supports nested composition where composite alarms reference other composite alarms for hierarchical alerting patterns. Each composite alarm is configured with SNS topic actions for state transitions via the AlarmActions, OKActions, and InsufficientDataActions parameters. The builder validates rule expressions against the CloudWatch rule expression grammar before deployment, catching syntax errors and circular references. It includes a simulation mode that evaluates the composite expression against historical alarm state data from CloudWatch alarm history via DescribeAlarmHistory. Integration with AWS Systems Manager OpsCenter allows automatic OpsItem creation when composite alarms fire. The skill manages alarm tags via TagResource for cost allocation and supports cross-account alarm references using ARN-based alarm identifiers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/)
