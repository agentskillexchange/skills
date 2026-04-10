---
name: AWS CloudWatch Composite Alarm Builder
description: Creates and manages AWS CloudWatch composite alarms using the CloudWatch
  PutCompositeAlarm API. Builds alarm rule expressions from existing metric alarms
  with AND/OR/NOT logic for multi-signal alerting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---
# AWS CloudWatch Composite Alarm Builder

The AWS CloudWatch Composite Alarm Builder constructs sophisticated multi-signal alerting rules by combining existing CloudWatch metric alarms into composite expressions. Using the AWS CloudWatch PutCompositeAlarm API, it creates alarm rules using boolean logic (ALARM, OK, INSUFFICIENT_DATA states combined with AND, OR, NOT operators). The skill queries existing alarms via DescribeAlarms to build a dependency graph of available signals, then guides construction of composite rule expressions. It supports nested composition where composite alarms reference other composite alarms for hierarchical alerting patterns. Each composite alarm is configured with SNS topic actions for state transitions via the AlarmActions, OKActions, and InsufficientDataActions parameters. The builder validates rule expressions against the CloudWatch rule expression grammar before deployment, catching syntax errors and circular references. It includes a simulation mode that evaluates the composite expression against historical alarm state data from CloudWatch alarm history via DescribeAlarmHistory. Integration with AWS Systems Manager OpsCenter allows automatic OpsItem creation when composite alarms fire. The skill manages alarm tags via TagResource for cost allocation and supports cross-account alarm references using ARN-based alarm identifiers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/)
