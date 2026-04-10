---
name: "CloudWatch Intelligent Alarms"
description: "Uses AWS CloudWatch SDK (boto3) to create composite alarms with ML-powered anomaly detection bands. Integrates with AWS SNS for notifications and EventBridge for automated remediation triggers."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-intelligent-alarms/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# CloudWatch Intelligent Alarms

The CloudWatch Intelligent Alarms skill enables AI agents to deploy sophisticated monitoring strategies on AWS infrastructure using the boto3 CloudWatch client. It creates and manages metric alarms, composite alarms, and anomaly detection bands through the put_metric_alarm and put_composite_alarm API calls.
The skill leverages CloudWatch Anomaly Detection models via the put_anomaly_detector API, training on two weeks of historical metric data to establish dynamic baselines that account for daily and weekly seasonality. Composite alarms combine multiple signals (CPU, memory, network, application metrics) into service-level health indicators using Boolean algebra expressions.
Alert routing is configured through AWS SNS (Simple Notification Service) topics with subscription filters targeting specific engineering teams based on AWS resource tags. For automated remediation, the skill creates EventBridge rules that trigger Step Functions state machines or Lambda functions. Integration with AWS Systems Manager Incident Manager creates structured incidents with runbook associations. The skill also configures CloudWatch Dashboards via the put_dashboard API, generating CloudFormation-compatible widget JSON for infrastructure-as-code workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-intelligent-alarms/)
