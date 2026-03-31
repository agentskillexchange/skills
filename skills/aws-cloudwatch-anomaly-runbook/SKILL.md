---
name: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
category: "Runbooks &amp; Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
tool_ecosystem:
  tool: aws
  github_repo: aws/aws-sdk-js-v3
  github_stars: 3596
  license: Apache-2.0
  maintained: true
---
# AWS CloudWatch Anomaly Runbook

Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations.

## Overview

The AWS CloudWatch Anomaly Runbook skill activates when CloudWatch Anomaly Detection identifies metric deviations beyond trained baselines. Using the AWS SDK CloudWatch client, it calls GetMetricData to retrieve the anomalous metric series alongside its expected band, then DescribeAlarms to gather alarm configuration and state transition history. The skill follows structured diagnostic runbooks organized by metric namespace: for EC2 it checks CPU, network, and disk metrics correlation; for RDS it examines connection counts, replica lag, and freeable memory; for ALB it correlates 5xx spikes with target group health. Each runbook step queries additional AWS APIs (EC2 DescribeInstances, RDS DescribeDBInstances, ECS DescribeServices) to build a complete diagnostic picture. The skill outputs a timeline-ordered investigation report with root cause probability scores and specific remediation actions, including AWS CLI commands to execute fixes and CloudFormation snippets to prevent recurrence.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-anomaly-runbook
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/)
