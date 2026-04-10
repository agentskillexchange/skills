---
name: Prometheus PromQL Alert Builder
description: Constructs Prometheus alerting rules using PromQL expressions with proper
  label matchers, aggregation operators, and for-duration thresholds. Integrates with
  Alertmanager routing trees for notification dispatch.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-promql-alert-builder/)
