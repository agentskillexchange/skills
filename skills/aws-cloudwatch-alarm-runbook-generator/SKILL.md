---
title: "AWS CloudWatch Alarm Runbook Generator"
description: "Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Alarm Runbook Generator

The AWS CloudWatch Alarm Runbook Generator skill reads CloudWatch alarm configurations via the AWS SDK DescribeAlarms and DescribeAlarmsForMetric API calls to automatically generate incident response runbooks. For each alarm, it identifies the monitored metric, threshold conditions, evaluation periods, and associated SNS notification targets. The skill maps alarms to relevant AWS resources using resource tags and CloudFormation stack associations. It generates structured runbook documents that include alarm context, likely root causes based on the metric type, diagnostic steps using specific AWS CLI commands, and remediation procedures. The tool integrates with AWS Systems Manager to link runbooks to SSM Automation documents for one-click remediation. It supports custom runbook templates with organization-specific escalation procedures and communication channels. Output formats include Markdown, Confluence wiki markup, and PagerDuty service integration specifications.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/)
