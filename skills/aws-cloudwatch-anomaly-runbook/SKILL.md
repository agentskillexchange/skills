---
title: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
slug: "aws-cloudwatch-anomaly-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/"
---

# AWS CloudWatch Anomaly Runbook

Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations.

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
clawhub install aws-cloudwatch-anomaly-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Anomaly Runbook skill activates when CloudWatch Anomaly Detection identifies metric deviations beyond trained baselines. Using the AWS SDK CloudWatch client, it calls GetMetricData to retrieve the anomalous metric series alongside its expected band, then DescribeAlarms to gather alarm configuration and state transition history. The skill follows structured diagnostic runbooks organized by metric namespace: for EC2 it checks CPU, network, and disk metrics correlation; for RDS it examines connection counts, replica lag, and freeable memory; for ALB it correlates 5xx spikes with target group health. Each runbook step queries additional AWS APIs (EC2 DescribeInstances, RDS DescribeDBInstances, ECS DescribeServices) to build a complete diagnostic picture. The skill outputs a timeline-ordered investigation report with root cause probability scores and specific remediation actions, including AWS CLI commands to execute fixes and CloudFormation snippets to prevent recurrence.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/)
