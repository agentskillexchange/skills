---
title: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks."
slug: "aws-cloudwatch-alarm-triage-agent"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/"
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

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
clawhub install aws-cloudwatch-alarm-triage-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Triage Agent automates incident response for CloudWatch alarm notifications. It uses the DescribeAlarms API to retrieve alarm configuration details including metric name, namespace, threshold, comparison operator, and evaluation periods, then queries GetMetricData to pull historical metric values for trend analysis.
The agent correlates alarm triggers with infrastructure changes by querying AWS CloudTrail via the LookupEvents API, identifying recent API calls that may have caused the alert (deployments, configuration changes, scaling events). It integrates with AWS Health API to check for ongoing AWS service issues that could explain metric anomalies.
For EC2-related alarms, it queries the DescribeInstances API for instance status checks and DescribeInstanceStatus for system/instance reachability. For RDS alarms, it uses DescribeDBInstances and DescribeEvents to check for maintenance windows, failovers, and storage issues. The agent calculates blast radius by mapping affected resources through AWS Resource Groups Tagging API and service dependency graphs defined in AWS Systems Manager OpsCenter. Remediation playbooks include AWS CLI commands for common fixes like scaling adjustments, security group corrections, and RDS parameter group modifications.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/)
