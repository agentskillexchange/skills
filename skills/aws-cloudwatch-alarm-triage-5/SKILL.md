---
title: "AWS CloudWatch Alarm Triage"
description: "Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events."
slug: "aws-cloudwatch-alarm-triage-5"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/"
---

# AWS CloudWatch Alarm Triage

Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install aws-cloudwatch-alarm-triage-5
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Triage skill automates the investigation and correlation of CloudWatch alarm events. It uses boto3 CloudWatch.describe_alarms and describe_alarm_history to retrieve alarm state transitions, threshold configurations, and evaluation periods. CloudWatch Logs Insights queries are executed via logs.start_query to search for error patterns, exception stack traces, and anomalous log volumes around alarm trigger times. AWS X-Ray trace analysis through the aws-xray-sdk identifies latency bottlenecks, fault segments, and downstream service failures correlated with alarm events. The skill cross-references alarm timestamps with CodeDeploy deployment events via codedeploy.list_deployments to determine if recent deployments caused the issue. Additional correlations include ECS task state changes, Lambda cold start patterns, RDS performance insights metrics, and ALB target group health checks. The triage process generates a root cause probability matrix ranking potential causes by evidence strength. It supports custom metric alarms, composite alarms with AND/OR logic, and anomaly detection band alarms. Remediation suggestions include automatic scaling policy adjustments, Lambda concurrency reservation changes, and RDS parameter group modifications. The skill outputs structured incident reports suitable for PagerDuty or OpsGenie integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/)
