---
title: "Prometheus PromQL Alert Builder"
description: "The Prometheus PromQL Alert Builder generates production-ready alerting rules by composing PromQL expressions with correct metric type awareness. It distinguishes between counters (using rate/increase), gauges (using avg_over_time), histograms (using histogram_quantile with le label), and summaries. The skill constructs multi-condition alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating metrics across different label dimensions. Alert for-durations are calculated based on scrape intervals and evaluation periods to avoid false positives from brief spikes. It generates matching Alertmanager configuration blocks with routing trees, grouping rules, inhibition rules for dependent alerts, and receiver configurations for Slack webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations and dashboard link templates using Grafana UID references."
source: "https://github.com/prometheus/prometheus"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus PromQL Alert Builder

The Prometheus PromQL Alert Builder generates production-ready alerting rules by composing PromQL expressions with correct metric type awareness. It distinguishes between counters (using rate/increase), gauges (using avg_over_time), histograms (using histogram_quantile with le label), and summaries. The skill constructs multi-condition alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating metrics across different label dimensions. Alert for-durations are calculated based on scrape intervals and evaluation periods to avoid false positives from brief spikes. It generates matching Alertmanager configuration blocks with routing trees, grouping rules, inhibition rules for dependent alerts, and receiver configurations for Slack webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations and dashboard link templates using Grafana UID references.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-promql-alert-builder/)
