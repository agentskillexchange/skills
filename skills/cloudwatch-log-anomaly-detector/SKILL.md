---
name: "CloudWatch Log Anomaly Detector"
description: "Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples."
category: "Monitoring &amp; Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/"
---
# CloudWatch Log Anomaly Detector

Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-log-anomaly-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-log-anomaly-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-log-anomaly-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-log-anomaly-detector -a codex
```

### OpenClaw

```bash
clawhub install cloudwatch-log-anomaly-detector
```

## Details

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
