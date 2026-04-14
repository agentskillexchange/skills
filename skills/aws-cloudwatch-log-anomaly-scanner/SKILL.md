---
title: "AWS CloudWatch Log Anomaly Scanner"
description: "Scans AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection API. Identifies unusual error patterns, latency spikes, and log volume anomalies across log groups."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/)
