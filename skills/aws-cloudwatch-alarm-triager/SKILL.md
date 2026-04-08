---
title: AWS CloudWatch Alarm Triager
description: The AWS CloudWatch Alarm Triager skill automates the initial triage of
  CloudWatch alarms by performing multi-signal correlation. When an alarm transitions
  to ALARM state, the skill uses boto3 to fetch the alarm configuration, metric data
  points, and evaluation period details. It then queries CloudTrail for recent API
  calls that may have triggered the condition — deployment events, configuration changes,
  scaling actions, or security group modifications. For EC2-related alarms, it checks
  instance status checks, system status checks, and scheduled events via the EC2 DescribeInstanceStatus
  API. The skill classifies alarms into severity tiers based on impact scope and blast
  radius analysis. For each alarm, it generates a triage summary with probable root
  cause, affected resources, and recommended investigation steps. Updates OpsGenie
  alerts with enriched context via the OpsGenie REST API. Supports alarm suppression
  during maintenance windows defined in SSM Parameter Store.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/)
