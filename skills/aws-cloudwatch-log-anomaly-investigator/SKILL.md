---
title: AWS CloudWatch Log Anomaly Investigator
description: The AWS CloudWatch Log Anomaly Investigator skill automates root cause
  analysis for production incidents detected in AWS CloudWatch Logs. It uses the CloudWatch
  Logs Insights API to run targeted queries across log groups, identifying error rate
  spikes, latency outliers, and unusual log patterns. Leveraging CloudWatch Anomaly
  Detection, the skill establishes baseline metrics and alerts when log volumes or
  error rates deviate significantly from expected patterns. It automatically correlates
  anomalies with recent deployment events by querying the AWS CodeDeploy API for deployment
  timelines. The investigation workflow includes automatic extraction of stack traces,
  error codes, and request IDs from structured JSON logs. Using the AWS X-Ray API,
  the skill traces individual requests across microservices to pinpoint the failing
  component. Results are compiled into a structured incident report with timeline,
  probable root cause, affected services, and recommended remediation steps. The skill
  supports integration with PagerDuty and Opsgenie via their REST APIs for automated
  incident escalation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# AWS CloudWatch Log Anomaly Investigator

The AWS CloudWatch Log Anomaly Investigator skill automates root cause analysis for production incidents detected in AWS CloudWatch Logs. It uses the CloudWatch Logs Insights API to run targeted queries across log groups, identifying error rate spikes, latency outliers, and unusual log patterns. Leveraging CloudWatch Anomaly Detection, the skill establishes baseline metrics and alerts when log volumes or error rates deviate significantly from expected patterns. It automatically correlates anomalies with recent deployment events by querying the AWS CodeDeploy API for deployment timelines. The investigation workflow includes automatic extraction of stack traces, error codes, and request IDs from structured JSON logs. Using the AWS X-Ray API, the skill traces individual requests across microservices to pinpoint the failing component. Results are compiled into a structured incident report with timeline, probable root cause, affected services, and recommended remediation steps. The skill supports integration with PagerDuty and Opsgenie via their REST APIs for automated incident escalation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/)
