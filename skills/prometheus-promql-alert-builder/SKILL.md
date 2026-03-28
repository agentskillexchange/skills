---
name: "Prometheus PromQL Alert Builder"
description: "Constructs Prometheus alerting rules using PromQL expressions with proper label matchers, aggregation operators, and for-duration thresholds. Integrates with Alertmanager routing trees for notification dispatch."
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
tool_ecosystem:
  tool: prometheus
  github_stars: 63289
  npm_weekly_downloads: 5319832
  github_repo: prometheus/prometheus
  license: Apache-2.0
  maintained: true
---

# Prometheus PromQL Alert Builder

Constructs Prometheus alerting rules using PromQL expressions with proper label matchers, aggregation operators, and for-duration thresholds. Integrates with Alertmanager routing trees for notification dispatch.

## Overview

The Prometheus PromQL Alert Builder generates production-ready alerting rules by composing PromQL expressions with correct metric type awareness. It distinguishes between counters (using rate/increase), gauges (using avg_over_time), histograms (using histogram_quantile with le label), and summaries. The skill constructs multi-condition alerts using PromQL vector matching with on/ignoring/group_left semantics for correlating metrics across different label dimensions. Alert for-durations are calculated based on scrape intervals and evaluation periods to avoid false positives from brief spikes. It generates matching Alertmanager configuration blocks with routing trees, grouping rules, inhibition rules for dependent alerts, and receiver configurations for Slack webhooks, PagerDuty service keys, and email SMTP relays. Includes runbook URL annotations and dashboard link templates using Grafana UID references.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-promql-alert-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-promql-alert-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-promql-alert-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-promql-alert-builder -a codex
```

### OpenClaw

```bash
clawhub install prometheus-promql-alert-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-promql-alert-builder/
