---
title: "AWS CloudWatch Composite Alarm Builder"
description: "Creates and manages AWS CloudWatch composite alarms using the CloudWatch PutCompositeAlarm API. Builds alarm rule expressions from existing metric alarms with AND/OR/NOT logic for multi-signal alerting."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/)
