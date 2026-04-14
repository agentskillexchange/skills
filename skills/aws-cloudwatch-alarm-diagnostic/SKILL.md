---
title: "AWS CloudWatch Alarm Diagnostic"
description: "Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Alarm Diagnostic

This skill uses the AWS SDK for JavaScript (CloudWatch, CloudTrail, and AWS Config APIs) to investigate active alarm states. When an alarm fires, the skill fetches the last 24 hours of metric datapoints via GetMetricData, retrieves alarm state history via DescribeAlarmHistory, and queries AWS CloudTrail for API calls in the affected resource scope within the alarm period. AWS Config is queried via GetResourceConfigHistory to identify recent configuration changes. The skill generates a structured incident summary mapping the metric spike to the most likely causal event, with confidence scores for each hypothesis. Optional integration with AWS Systems Manager Parameter Store allows dynamic threshold tuning suggestions. Output includes remediation options formatted for both CLI execution and AWS Console navigation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/)
