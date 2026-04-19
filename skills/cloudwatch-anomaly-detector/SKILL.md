---
title: "CloudWatch Anomaly Detector"
description: "The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines. The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function. Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates."
source: "https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# CloudWatch Anomaly Detector

The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines. The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function. Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/)
