---
title: AWS CloudWatch Alarm Diagnostic
description: This skill uses the AWS SDK for JavaScript (CloudWatch, CloudTrail, and
  AWS Config APIs) to investigate active alarm states. When an alarm fires, the skill
  fetches the last 24 hours of metric datapoints via GetMetricData, retrieves alarm
  state history via DescribeAlarmHistory, and queries AWS CloudTrail for API calls
  in the affected resource scope within the alarm period. AWS Config is queried via
  GetResourceConfigHistory to identify recent configuration changes. The skill generates
  a structured incident summary mapping the metric spike to the most likely causal
  event, with confidence scores for each hypothesis. Optional integration with AWS
  Systems Manager Parameter Store allows dynamic threshold tuning suggestions. Output
  includes remediation options formatted for both CLI execution and AWS Console navigation.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/)
