---
title: "CloudWatch Anomaly Detector"
description: "Creates and manages CloudWatch Anomaly Detection bands using AWS SDK PutAnomalyDetector and GetMetricData APIs. Generates alerts when metrics breach learned baselines with configurable sensitivity."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# CloudWatch Anomaly Detector

The CloudWatch Anomaly Detector skill automates the creation and management of AWS CloudWatch anomaly detection models for infrastructure and application metrics. Using the AWS SDK v3 CloudWatch client, it calls PutAnomalyDetector to create detection bands and GetMetricData to evaluate metric values against learned baselines.

The skill supports batch configuration where you define metric namespaces, dimensions, and sensitivity levels in a YAML manifest. It automatically creates anomaly detectors for each metric, configures exclusion windows for known maintenance periods, and sets up CloudWatch Alarms that fire when metrics breach the anomaly band using the ANOMALY_DETECTION_BAND function.

Advanced features include cross-account metric collection via CloudWatch cross-account observability, automatic dashboard generation using the CloudWatch Dashboard API with anomaly band widgets, and SNS topic integration for alert delivery. The skill also provides a daily digest that summarizes anomaly events, model training status, and recommended sensitivity adjustments based on false positive rates.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-anomaly-detector/)
