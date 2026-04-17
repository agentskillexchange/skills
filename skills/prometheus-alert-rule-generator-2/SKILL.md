---
title: "Prometheus Alert Rule Generator"
description: "Generates and validates Prometheus alerting rules from natural language descriptions using the Prometheus HTTP API and PromQL query engine. Supports Alertmanager routing configuration and Grafana dashboard annotation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Generator

The Prometheus Alert Rule Generator translates natural language alert descriptions into valid PromQL expressions and Prometheus alerting rule YAML configurations. It queries the Prometheus HTTP API to discover available metrics, labels, and recording rules, then constructs appropriate PromQL expressions with correct aggregation and threshold logic. The agent validates generated rules by executing them against the Prometheus query endpoint to ensure they return expected result types. It also generates corresponding Alertmanager routing configurations with receiver definitions for Slack, email, and webhook targets. Grafana dashboard annotations are automatically created to correlate alert windows with metric visualizations. The tool supports templating for common patterns like SLO-based alerting, rate-of-change detection, and percentile threshold monitoring. Rule files are output in standard Prometheus rule group format ready for deployment via Prometheus Operator or static configuration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-generator-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-rule-generator-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/)
