---
name: AWS CloudWatch Alarm Triage
description: Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms,
  CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk.
  Correlates alarm triggers with deployment events.
category: "Runbooks &amp; Diagnostics"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/"
---
# AWS CloudWatch Alarm Triage

Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events.

The AWS CloudWatch Alarm Triage skill automates the investigation and correlation of CloudWatch alarm events. It uses boto3 CloudWatch.describe_alarms and describe_alarm_history to retrieve alarm state transitions, threshold configurations, and evaluation periods. CloudWatch Logs Insights queries are executed via logs.start_query to search for error patterns, exception stack traces, and anomalous log volumes around alarm trigger times. AWS X-Ray trace analysis through the aws-xray-sdk identifies latency bottlenecks, fault segments, and downstream service failures correlated with alarm events. The skill cross-references alarm timestamps with CodeDeploy deployment events via codedeploy.list_deployments to determine if recent deployments caused the issue. Additional correlations include ECS task state changes, Lambda cold start patterns, RDS performance insights metrics, and ALB target group health checks. The triage process generates a root cause probability matrix ranking potential causes by evidence strength. It supports custom metric alarms, composite alarms with AND/OR logic, and anomaly detection band alarms. Remediation suggestions include automatic scaling policy adjustments, Lambda concurrency reservation changes, and RDS parameter group modifications. The skill outputs structured incident reports suitable for PagerDuty or OpsGenie integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-triage-5
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/)
