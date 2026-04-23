---
title: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Anomaly Runbook

Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-anomaly-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudwatch-anomaly-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/)
