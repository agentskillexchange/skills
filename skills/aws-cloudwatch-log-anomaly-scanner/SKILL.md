---
title: "AWS CloudWatch Log Anomaly Scanner"
description: "The AWS CloudWatch Log Anomaly Scanner skill uses the CloudWatch Logs Insights API (StartQuery/GetQueryResults) to run analytical queries across multiple log groups simultaneously. It constructs dynamic Insights queries that aggregate error frequencies, parse structured JSON log fields, and compute percentile latency distributions. The skill leverages the CloudWatch Anomaly Detection API to establish baseline patterns for error rates and log volumes, then flags deviations exceeding configurable sigma thresholds. Cross-log-group correlation identifies cascading failures by matching request IDs and trace headers across Lambda, ECS, and API Gateway log groups. The skill integrates with the X-Ray API (GetTraceSummaries) to correlate log anomalies with distributed trace data. Export functionality uses the CreateExportTask API to archive anomalous log windows to S3 for forensic analysis. Alert rules can be generated as CloudWatch Metric Filter definitions with proper namespace and dimension configurations."
source: "https://github.com/aws/aws-sdk-js-v3"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Log Anomaly Scanner

The AWS CloudWatch Log Anomaly Scanner skill uses the CloudWatch Logs Insights API (StartQuery/GetQueryResults) to run analytical queries across multiple log groups simultaneously. It constructs dynamic Insights queries that aggregate error frequencies, parse structured JSON log fields, and compute percentile latency distributions. The skill leverages the CloudWatch Anomaly Detection API to establish baseline patterns for error rates and log volumes, then flags deviations exceeding configurable sigma thresholds. Cross-log-group correlation identifies cascading failures by matching request IDs and trace headers across Lambda, ECS, and API Gateway log groups. The skill integrates with the X-Ray API (GetTraceSummaries) to correlate log anomalies with distributed trace data. Export functionality uses the CreateExportTask API to archive anomalous log windows to S3 for forensic analysis. Alert rules can be generated as CloudWatch Metric Filter definitions with proper namespace and dimension configurations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/)
