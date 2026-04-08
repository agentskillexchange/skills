---
title: Prometheus PromQL Alert Builder
description: The Prometheus PromQL Alert Builder generates production-ready alerting
  rules by composing PromQL expressions with correct metric type awareness. It distinguishes
  between counters (using rate/increase), gauges (using avg_over_time), histograms
  (using histogram_quantile with le label), and summaries. The skill constructs multi-condition
  alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating
  metrics across different label dimensions. Alert for-durations are calculated based
  on scrape intervals and evaluation periods to avoid false positives from brief spikes.
  It generates matching Alertmanager configuration blocks with routing trees, grouping
  rules, inhibition rules for dependent alerts, and receiver configurations for Slack
  webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations
  and dashboard link templates using Grafana UID references.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-promql-alert-builder/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# Prometheus PromQL Alert Builder

The Prometheus PromQL Alert Builder generates production-ready alerting rules by composing PromQL expressions with correct metric type awareness. It distinguishes between counters (using rate/increase), gauges (using avg_over_time), histograms (using histogram_quantile with le label), and summaries. The skill constructs multi-condition alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating metrics across different label dimensions. Alert for-durations are calculated based on scrape intervals and evaluation periods to avoid false positives from brief spikes. It generates matching Alertmanager configuration blocks with routing trees, grouping rules, inhibition rules for dependent alerts, and receiver configurations for Slack webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations and dashboard link templates using Grafana UID references.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-promql-alert-builder/)
