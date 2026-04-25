---
title: "CloudWatch Anomaly Detector"
description: "Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
---

# CloudWatch Anomaly Detector

The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines.

The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function.

Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudwatch-anomaly-detector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudwatch-anomaly-detector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/)
