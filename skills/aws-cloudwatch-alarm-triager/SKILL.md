---
name: AWS CloudWatch Alarm Triager
description: Triages AWS CloudWatch alarms by correlating alarm state changes with
  CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity,
  identifies root cause candidates, and updates OpsGenie alerts.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---
# AWS CloudWatch Alarm Triager

The AWS CloudWatch Alarm Triager skill automates the initial triage of CloudWatch alarms by performing multi-signal correlation. When an alarm transitions to ALARM state, the skill uses boto3 to fetch the alarm configuration, metric data points, and evaluation period details. It then queries CloudTrail for recent API calls that may have triggered the condition — deployment events, configuration changes, scaling actions, or security group modifications. For EC2-related alarms, it checks instance status checks, system status checks, and scheduled events via the EC2 DescribeInstanceStatus API. The skill classifies alarms into severity tiers based on impact scope and blast radius analysis. For each alarm, it generates a triage summary with probable root cause, affected resources, and recommended investigation steps. Updates OpsGenie alerts with enriched context via the OpsGenie REST API. Supports alarm suppression during maintenance windows defined in SSM Parameter Store.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/)
