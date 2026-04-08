---
title: AWS CloudWatch Alarm Runbook
description: The AWS CloudWatch Alarm Runbook skill provides automated incident response
  workflows triggered by CloudWatch alarm state changes. Using boto3 and the CloudWatch
  API, it retrieves alarm details, associated metric data, and alarm history to build
  a comprehensive incident context before executing diagnostic procedures. When an
  alarm enters the ALARM state, the skill identifies the alarm type (metric alarm,
  composite alarm, anomaly detection alarm) and retrieves contributing metrics using
  GetMetricData with appropriate period and stat configurations. It correlates alarm
  timing with CloudTrail events to identify potential root causes from recent infrastructure
  changes. The skill maps specific alarm patterns to AWS Systems Manager (SSM) Automation
  runbook documents. For example, high CPU alarms on EC2 trigger instance diagnostics
  via SSM Run Command (top, ps, netstat), while RDS connection count alarms invoke
  RDS Performance Insights queries to identify blocking queries or connection leaks.
  Advanced features include composite alarm decomposition to identify which child
  alarms are contributing, metric math expression evaluation for alarms using METRICS()
  functions, and integration with AWS Health Dashboard to correlate alarms with known
  service issues. The skill also manages alarm suppression during maintenance windows
  using alarm actions disable/enable.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-wave48/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---

# AWS CloudWatch Alarm Runbook

The AWS CloudWatch Alarm Runbook skill provides automated incident response workflows triggered by CloudWatch alarm state changes. Using boto3 and the CloudWatch API, it retrieves alarm details, associated metric data, and alarm history to build a comprehensive incident context before executing diagnostic procedures. When an alarm enters the ALARM state, the skill identifies the alarm type (metric alarm, composite alarm, anomaly detection alarm) and retrieves contributing metrics using GetMetricData with appropriate period and stat configurations. It correlates alarm timing with CloudTrail events to identify potential root causes from recent infrastructure changes. The skill maps specific alarm patterns to AWS Systems Manager (SSM) Automation runbook documents. For example, high CPU alarms on EC2 trigger instance diagnostics via SSM Run Command (top, ps, netstat), while RDS connection count alarms invoke RDS Performance Insights queries to identify blocking queries or connection leaks. Advanced features include composite alarm decomposition to identify which child alarms are contributing, metric math expression evaluation for alarms using METRICS() functions, and integration with AWS Health Dashboard to correlate alarms with known service issues. The skill also manages alarm suppression during maintenance windows using alarm actions disable/enable.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-wave48/)
