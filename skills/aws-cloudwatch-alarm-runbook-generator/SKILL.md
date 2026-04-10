---
name: AWS CloudWatch Alarm Runbook Generator
description: Generates structured incident runbooks from AWS CloudWatch alarm configurations
  using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links
  alarms to remediation procedures automatically.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---
# AWS CloudWatch Alarm Runbook Generator

The AWS CloudWatch Alarm Runbook Generator skill reads CloudWatch alarm configurations via the AWS SDK DescribeAlarms and DescribeAlarmsForMetric API calls to automatically generate incident response runbooks. For each alarm, it identifies the monitored metric, threshold conditions, evaluation periods, and associated SNS notification targets. The skill maps alarms to relevant AWS resources using resource tags and CloudFormation stack associations. It generates structured runbook documents that include alarm context, likely root causes based on the metric type, diagnostic steps using specific AWS CLI commands, and remediation procedures. The tool integrates with AWS Systems Manager to link runbooks to SSM Automation documents for one-click remediation. It supports custom runbook templates with organization-specific escalation procedures and communication channels. Output formats include Markdown, Confluence wiki markup, and PagerDuty service integration specifications.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/)
