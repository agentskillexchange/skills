---
title: AWS CloudWatch Log Anomaly Scanner
description: The AWS CloudWatch Log Anomaly Scanner skill uses the CloudWatch Logs
  Insights API (StartQuery/GetQueryResults) to run analytical queries across multiple
  log groups simultaneously. It constructs dynamic Insights queries that aggregate
  error frequencies, parse structured JSON log fields, and compute percentile latency
  distributions. The skill leverages the CloudWatch Anomaly Detection API to establish
  baseline patterns for error rates and log volumes, then flags deviations exceeding
  configurable sigma thresholds. Cross-log-group correlation identifies cascading
  failures by matching request IDs and trace headers across Lambda, ECS, and API Gateway
  log groups. The skill integrates with the X-Ray API (GetTraceSummaries) to correlate
  log anomalies with distributed trace data. Export functionality uses the CreateExportTask
  API to archive anomalous log windows to S3 for forensic analysis. Alert rules can
  be generated as CloudWatch Metric Filter definitions with proper namespace and dimension
  configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# AWS CloudWatch Log Anomaly Scanner

The AWS CloudWatch Log Anomaly Scanner skill uses the CloudWatch Logs Insights API (StartQuery/GetQueryResults) to run analytical queries across multiple log groups simultaneously. It constructs dynamic Insights queries that aggregate error frequencies, parse structured JSON log fields, and compute percentile latency distributions. The skill leverages the CloudWatch Anomaly Detection API to establish baseline patterns for error rates and log volumes, then flags deviations exceeding configurable sigma thresholds. Cross-log-group correlation identifies cascading failures by matching request IDs and trace headers across Lambda, ECS, and API Gateway log groups. The skill integrates with the X-Ray API (GetTraceSummaries) to correlate log anomalies with distributed trace data. Export functionality uses the CreateExportTask API to archive anomalous log windows to S3 for forensic analysis. Alert rules can be generated as CloudWatch Metric Filter definitions with proper namespace and dimension configurations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/)
