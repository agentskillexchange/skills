---
name: "Prometheus Alert Rule Generator"
description: "Generates and validates Prometheus alerting rules from natural language descriptions using the Prometheus HTTP API and PromQL query engine. Supports Alertmanager routing configuration and Grafana dashboard annotation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
---

# Prometheus Alert Rule Generator

The Prometheus Alert Rule Generator translates natural language alert descriptions into valid PromQL expressions and Prometheus alerting rule YAML configurations. It queries the Prometheus HTTP API to discover available metrics, labels, and recording rules, then constructs appropriate PromQL expressions with correct aggregation and threshold logic. The agent validates generated rules by executing them against the Prometheus query endpoint to ensure they return expected result types. It also generates corresponding Alertmanager routing configurations with receiver definitions for Slack, email, and webhook targets. Grafana dashboard annotations are automatically created to correlate alert windows with metric visualizations. The tool supports templating for common patterns like SLO-based alerting, rate-of-change detection, and percentile threshold monitoring. Rule files are output in standard Prometheus rule group format ready for deployment via Prometheus Operator or static configuration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/)
