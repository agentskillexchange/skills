---
title: AWS Systems Manager Runbook Engine
description: The AWS Systems Manager Runbook Engine skill automates operational diagnostics
  and remediation on AWS infrastructure. It creates and executes SSM Automation documents
  that define multi-step runbooks with conditional branching, approval gates, and
  error handling. The skill uses the AWS Systems Manager Automation API to trigger
  runbooks against individual instances or entire fleets using rate-controlled execution.
  Diagnostic data is collected through the CloudWatch GetMetricData API, pulling CPU
  utilization, disk I/O, network throughput, and custom application metrics for correlation
  analysis. AWS Health events are monitored to provide context during incidents, linking
  infrastructure changes to observed symptoms. The skill supports Run Command for
  ad-hoc diagnostics across instance fleets, Session Manager for interactive troubleshooting
  without SSH, Parameter Store integration for runbook configuration, and OpsCenter
  OpsItem creation for tracking operational issues. It generates comprehensive diagnostic
  reports combining CloudWatch metrics, SSM inventory data, and Config compliance
  status.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-ssm-runbook-engine/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# AWS Systems Manager Runbook Engine

The AWS Systems Manager Runbook Engine skill automates operational diagnostics and remediation on AWS infrastructure. It creates and executes SSM Automation documents that define multi-step runbooks with conditional branching, approval gates, and error handling. The skill uses the AWS Systems Manager Automation API to trigger runbooks against individual instances or entire fleets using rate-controlled execution. Diagnostic data is collected through the CloudWatch GetMetricData API, pulling CPU utilization, disk I/O, network throughput, and custom application metrics for correlation analysis. AWS Health events are monitored to provide context during incidents, linking infrastructure changes to observed symptoms. The skill supports Run Command for ad-hoc diagnostics across instance fleets, Session Manager for interactive troubleshooting without SSH, Parameter Store integration for runbook configuration, and OpsCenter OpsItem creation for tracking operational issues. It generates comprehensive diagnostic reports combining CloudWatch metrics, SSM inventory data, and Config compliance status.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-engine/)
