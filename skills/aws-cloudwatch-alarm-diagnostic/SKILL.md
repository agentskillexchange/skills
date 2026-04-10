---
name: AWS CloudWatch Alarm Diagnostic
description: Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics,
  alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates
  metric anomalies with recent infrastructure changes to suggest root cause hypotheses.
  Outputs a structured incident summary with remediation options.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---
# AWS CloudWatch Alarm Diagnostic

This skill uses the AWS SDK for JavaScript (CloudWatch, CloudTrail, and AWS Config APIs) to investigate active alarm states. When an alarm fires, the skill fetches the last 24 hours of metric datapoints via GetMetricData, retrieves alarm state history via DescribeAlarmHistory, and queries AWS CloudTrail for API calls in the affected resource scope within the alarm period. AWS Config is queried via GetResourceConfigHistory to identify recent configuration changes. The skill generates a structured incident summary mapping the metric spike to the most likely causal event, with confidence scores for each hypothesis. Optional integration with AWS Systems Manager Parameter Store allows dynamic threshold tuning suggestions. Output includes remediation options formatted for both CLI execution and AWS Console navigation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/)
