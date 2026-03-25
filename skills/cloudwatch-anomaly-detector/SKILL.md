---
name: "CloudWatch Anomaly Detector"
description: "Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# CloudWatch Anomaly Detector

Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity.

## Overview

The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines.

The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function.

Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-anomaly-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-anomaly-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-anomaly-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-anomaly-detector -a codex
```

### OpenClaw

```bash
clawhub install cloudwatch-anomaly-detector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/
