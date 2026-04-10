---
title: "CloudWatch Anomaly Detector"
description: "Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity."
slug: "cloudwatch-anomaly-detector"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/"
---

# CloudWatch Anomaly Detector

Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cloudwatch-anomaly-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines.
The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function.
Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/)
