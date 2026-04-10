---
title: "AWS CloudWatch Alarm Triager"
description: "Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts."
slug: "aws-cloudwatch-alarm-triager"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/"
listed: true
---

# AWS CloudWatch Alarm Triager

Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts.

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
clawhub install aws-cloudwatch-alarm-triager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Triager skill automates the initial triage of CloudWatch alarms by performing multi-signal correlation. When an alarm transitions to ALARM state, the skill uses boto3 to fetch the alarm configuration, metric data points, and evaluation period details. It then queries CloudTrail for recent API calls that may have triggered the condition — deployment events, configuration changes, scaling actions, or security group modifications. For EC2-related alarms, it checks instance status checks, system status checks, and scheduled events via the EC2 DescribeInstanceStatus API. The skill classifies alarms into severity tiers based on impact scope and blast radius analysis. For each alarm, it generates a triage summary with probable root cause, affected resources, and recommended investigation steps. Updates OpsGenie alerts with enriched context via the OpsGenie REST API. Supports alarm suppression during maintenance windows defined in SSM Parameter Store.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/)
