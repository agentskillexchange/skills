---
title: "Prometheus PromQL Alert Builder"
description: "Constructs Prometheus alerting rules using PromQL expressions with proper label matchers, aggregation operators, and for-duration thresholds. Integrates with Alertmanager routing trees for notification dispatch."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus PromQL Alert Builder

The Prometheus PromQL Alert Builder generates production-ready alerting rules by composing PromQL expressions with correct metric type awareness. It distinguishes between counters (using rate/increase), gauges (using avg_over_time), histograms (using histogram_quantile with le label), and summaries. The skill constructs multi-condition alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating metrics across different label dimensions. Alert for-durations are calculated based on scrape intervals and evaluation periods to avoid false positives from brief spikes. It generates matching Alertmanager configuration blocks with routing trees, grouping rules, inhibition rules for dependent alerts, and receiver configurations for Slack webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations and dashboard link templates using Grafana UID references.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-promql-alert-builder/)
