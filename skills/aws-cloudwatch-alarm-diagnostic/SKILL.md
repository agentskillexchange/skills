---
title: "AWS CloudWatch Alarm Diagnostic"
description: "Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Alarm Diagnostic

This skill uses the AWS SDK for JavaScript (CloudWatch, CloudTrail, and AWS Config APIs) to investigate active alarm states. When an alarm fires, the skill fetches the last 24 hours of metric datapoints via GetMetricData, retrieves alarm state history via DescribeAlarmHistory, and queries AWS CloudTrail for API calls in the affected resource scope within the alarm period. AWS Config is queried via GetResourceConfigHistory to identify recent configuration changes. The skill generates a structured incident summary mapping the metric spike to the most likely causal event, with confidence scores for each hypothesis. Optional integration with AWS Systems Manager Parameter Store allows dynamic threshold tuning suggestions. Output includes remediation options formatted for both CLI execution and AWS Console navigation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-alarm-diagnostic
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudwatch-alarm-diagnostic`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/)
