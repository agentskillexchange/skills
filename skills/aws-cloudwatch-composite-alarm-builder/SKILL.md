---
name: "AWS CloudWatch Composite Alarm Builder"
description: "Creates and manages AWS CloudWatch composite alarms using the CloudWatch PutCompositeAlarm API. Builds alarm rule expressions from existing metric alarms with AND/OR/NOT logic for multi-signal alerting."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudWatch Composite Alarm Builder

Creates and manages AWS CloudWatch composite alarms using the CloudWatch PutCompositeAlarm API. Builds alarm rule expressions from existing metric alarms with AND/OR/NOT logic for multi-signal alerting.

## Overview

The AWS CloudWatch Composite Alarm Builder constructs sophisticated multi-signal alerting rules by combining existing CloudWatch metric alarms into composite expressions. Using the AWS CloudWatch PutCompositeAlarm API, it creates alarm rules using boolean logic (ALARM, OK, INSUFFICIENT_DATA states combined with AND, OR, NOT operators). The skill queries existing alarms via DescribeAlarms to build a dependency graph of available signals, then guides construction of composite rule expressions. It supports nested composition where composite alarms reference other composite alarms for hierarchical alerting patterns. Each composite alarm is configured with SNS topic actions for state transitions via the AlarmActions, OKActions, and InsufficientDataActions parameters. The builder validates rule expressions against the CloudWatch rule expression grammar before deployment, catching syntax errors and circular references. It includes a simulation mode that evaluates the composite expression against historical alarm state data from CloudWatch alarm history via DescribeAlarmHistory. Integration with AWS Systems Manager OpsCenter allows automatic OpsItem creation when composite alarms fire. The skill manages alarm tags via TagResource for cost allocation and supports cross-account alarm references using ARN-based alarm identifiers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-composite-alarm-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-composite-alarm-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-composite-alarm-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-composite-alarm-builder -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-composite-alarm-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-composite-alarm-builder/
