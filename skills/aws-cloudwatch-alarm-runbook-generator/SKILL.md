---
name: "AWS CloudWatch Alarm Runbook Generator"
description: "Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS CloudWatch Alarm Runbook Generator

Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically.

## Overview

The AWS CloudWatch Alarm Runbook Generator skill reads CloudWatch alarm configurations via the AWS SDK DescribeAlarms and DescribeAlarmsForMetric API calls to automatically generate incident response runbooks. For each alarm, it identifies the monitored metric, threshold conditions, evaluation periods, and associated SNS notification targets. The skill maps alarms to relevant AWS resources using resource tags and CloudFormation stack associations. It generates structured runbook documents that include alarm context, likely root causes based on the metric type, diagnostic steps using specific AWS CLI commands, and remediation procedures. The tool integrates with AWS Systems Manager to link runbooks to SSM Automation documents for one-click remediation. It supports custom runbook templates with organization-specific escalation procedures and communication channels. Output formats include Markdown, Confluence wiki markup, and PagerDuty service integration specifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-runbook-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-runbook-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-runbook-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-runbook-generator -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-runbook-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/
