---
name: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/
