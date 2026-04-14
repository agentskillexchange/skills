---
title: "Prometheus Alert Rule Generator"
description: "Generates and validates Prometheus alerting rules from natural language descriptions using the Prometheus HTTP API and PromQL query engine. Supports Alertmanager routing configuration and Grafana dashboard annotation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Rule Generator

The Prometheus Alert Rule Generator translates natural language alert descriptions into valid PromQL expressions and Prometheus alerting rule YAML configurations. It queries the Prometheus HTTP API to discover available metrics, labels, and recording rules, then constructs appropriate PromQL expressions with correct aggregation and threshold logic. The agent validates generated rules by executing them against the Prometheus query endpoint to ensure they return expected result types. It also generates corresponding Alertmanager routing configurations with receiver definitions for Slack, email, and webhook targets. Grafana dashboard annotations are automatically created to correlate alert windows with metric visualizations. The tool supports templating for common patterns like SLO-based alerting, rate-of-change detection, and percentile threshold monitoring. Rule files are output in standard Prometheus rule group format ready for deployment via Prometheus Operator or static configuration.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/)
