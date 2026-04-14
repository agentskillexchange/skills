---
title: "AWS CloudWatch Log Anomaly Investigator"
description: "Investigates anomalous patterns in AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection. Correlates log spikes with deployment events via AWS CodeDeploy API."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Log Anomaly Investigator

The AWS CloudWatch Log Anomaly Investigator skill automates root cause analysis for production incidents detected in AWS CloudWatch Logs. It uses the CloudWatch Logs Insights API to run targeted queries across log groups, identifying error rate spikes, latency outliers, and unusual log patterns.

Leveraging CloudWatch Anomaly Detection, the skill establishes baseline metrics and alerts when log volumes or error rates deviate significantly from expected patterns. It automatically correlates anomalies with recent deployment events by querying the AWS CodeDeploy API for deployment timelines.

The investigation workflow includes automatic extraction of stack traces, error codes, and request IDs from structured JSON logs. Using the AWS X-Ray API, the skill traces individual requests across microservices to pinpoint the failing component.

Results are compiled into a structured incident report with timeline, probable root cause, affected services, and recommended remediation steps. The skill supports integration with PagerDuty and Opsgenie via their REST APIs for automated incident escalation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/)
