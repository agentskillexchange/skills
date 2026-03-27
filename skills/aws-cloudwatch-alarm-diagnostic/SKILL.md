---
name: "AWS CloudWatch Alarm Diagnostic"
description: "Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS CloudWatch Alarm Diagnostic

Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options.

## Overview

This skill uses the AWS SDK for JavaScript (CloudWatch, CloudTrail, and AWS Config APIs) to investigate active alarm states. When an alarm fires, the skill fetches the last 24 hours of metric datapoints via GetMetricData, retrieves alarm state history via DescribeAlarmHistory, and queries AWS CloudTrail for API calls in the affected resource scope within the alarm period. AWS Config is queried via GetResourceConfigHistory to identify recent configuration changes. The skill generates a structured incident summary mapping the metric spike to the most likely causal event, with confidence scores for each hypothesis. Optional integration with AWS Systems Manager Parameter Store allows dynamic threshold tuning suggestions. Output includes remediation options formatted for both CLI execution and AWS Console navigation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-diagnostic
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/
