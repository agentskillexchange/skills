---
title: "AWS CloudWatch Alarm Triage"
description: "Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Alarm Triage

The AWS CloudWatch Alarm Triage skill automates the investigation and correlation of CloudWatch alarm events. It uses boto3 CloudWatch.describe_alarms and describe_alarm_history to retrieve alarm state transitions, threshold configurations, and evaluation periods. CloudWatch Logs Insights queries are executed via logs.start_query to search for error patterns, exception stack traces, and anomalous log volumes around alarm trigger times. AWS X-Ray trace analysis through the aws-xray-sdk identifies latency bottlenecks, fault segments, and downstream service failures correlated with alarm events. The skill cross-references alarm timestamps with CodeDeploy deployment events via codedeploy.list_deployments to determine if recent deployments caused the issue. Additional correlations include ECS task state changes, Lambda cold start patterns, RDS performance insights metrics, and ALB target group health checks. The triage process generates a root cause probability matrix ranking potential causes by evidence strength. It supports custom metric alarms, composite alarms with AND/OR logic, and anomaly detection band alarms. Remediation suggestions include automatic scaling policy adjustments, Lambda concurrency reservation changes, and RDS parameter group modifications. The skill outputs structured incident reports suitable for PagerDuty or OpsGenie integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/)
