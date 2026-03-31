---
name: "Prometheus Alert Tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-tuner/"
---
# Prometheus Alert Tuner

Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Overview

The Prometheus Alert Tuner skill optimizes your Prometheus alerting rules to reduce false positives and alert fatigue while maintaining coverage for real incidents. It uses the Prometheus HTTP API (/api/v1/query, /api/v1/query_range, /api/v1/rules) to analyze current alerting behavior.

The tuning process begins by querying ALERTS and ALERTS_FOR_STATE metrics over a configurable lookback window to identify noisy alerts — those that fire frequently for short durations or fire constantly without actionable outcomes. For each alert rule, the skill evaluates the PromQL expression against historical data to determine optimal thresholds.

Threshold optimization uses histogram_quantile() and quantile_over_time() functions to find statistically appropriate trigger points. For example, a high CPU alert threshold might be adjusted from a static 80% to the p99 of the trailing 7-day range plus a configurable margin. The skill also recommends appropriate for durations based on metric volatility analysis.

Inhibition and grouping rules are generated for the Alertmanager configuration (alertmanager.yml) to prevent cascading alerts. The skill identifies parent-child relationships between alerts (e.g., NodeDown should inhibit all pod-level alerts on that node) and generates route and inhibit_rules configurations. All modified alert rules maintain the original recording rules and annotation templates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-tuner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)
