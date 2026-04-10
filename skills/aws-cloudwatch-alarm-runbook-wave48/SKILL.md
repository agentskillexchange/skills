---
title: "AWS CloudWatch Alarm Runbook"
description: "Automates incident response for AWS CloudWatch alarms using boto3, the CloudWatch GetMetricData API, and AWS Systems Manager runbook documents. Maps alarm states to diagnostic procedures and remediation actions."
slug: "aws-cloudwatch-alarm-runbook-wave48"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-wave48/"
---

# AWS CloudWatch Alarm Runbook

Automates incident response for AWS CloudWatch alarms using boto3, the CloudWatch GetMetricData API, and AWS Systems Manager runbook documents. Maps alarm states to diagnostic procedures and remediation actions.

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
clawhub install aws-cloudwatch-alarm-runbook-wave48
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Runbook skill provides automated incident response workflows triggered by CloudWatch alarm state changes. Using boto3 and the CloudWatch API, it retrieves alarm details, associated metric data, and alarm history to build a comprehensive incident context before executing diagnostic procedures.
When an alarm enters the ALARM state, the skill identifies the alarm type (metric alarm, composite alarm, anomaly detection alarm) and retrieves contributing metrics using GetMetricData with appropriate period and stat configurations. It correlates alarm timing with CloudTrail events to identify potential root causes from recent infrastructure changes.
The skill maps specific alarm patterns to AWS Systems Manager (SSM) Automation runbook documents. For example, high CPU alarms on EC2 trigger instance diagnostics via SSM Run Command (top, ps, netstat), while RDS connection count alarms invoke RDS Performance Insights queries to identify blocking queries or connection leaks.
Advanced features include composite alarm decomposition to identify which child alarms are contributing, metric math expression evaluation for alarms using METRICS() functions, and integration with AWS Health Dashboard to correlate alarms with known service issues. The skill also manages alarm suppression during maintenance windows using alarm actions disable/enable.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-wave48/)
