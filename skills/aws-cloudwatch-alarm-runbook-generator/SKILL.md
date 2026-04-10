---
title: "AWS CloudWatch Alarm Runbook Generator"
description: "Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically."
slug: "aws-cloudwatch-alarm-runbook-generator"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/"
listed: true
---

# AWS CloudWatch Alarm Runbook Generator

Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically.

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
clawhub install aws-cloudwatch-alarm-runbook-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Runbook Generator skill reads CloudWatch alarm configurations via the AWS SDK DescribeAlarms and DescribeAlarmsForMetric API calls to automatically generate incident response runbooks. For each alarm, it identifies the monitored metric, threshold conditions, evaluation periods, and associated SNS notification targets. The skill maps alarms to relevant AWS resources using resource tags and CloudFormation stack associations. It generates structured runbook documents that include alarm context, likely root causes based on the metric type, diagnostic steps using specific AWS CLI commands, and remediation procedures. The tool integrates with AWS Systems Manager to link runbooks to SSM Automation documents for one-click remediation. It supports custom runbook templates with organization-specific escalation procedures and communication channels. Output formats include Markdown, Confluence wiki markup, and PagerDuty service integration specifications.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/)
