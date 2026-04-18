---
title: "Prometheus Alert Tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Tuner

The Prometheus Alert Tuner skill optimizes your Prometheus alerting rules to reduce false positives and alert fatigue while maintaining coverage for real incidents. It uses the Prometheus HTTP API (/api/v1/query, /api/v1/query_range, /api/v1/rules) to analyze current alerting behavior.

The tuning process begins by querying ALERTS and ALERTS_FOR_STATE metrics over a configurable lookback window to identify noisy alerts — those that fire frequently for short durations or fire constantly without actionable outcomes. For each alert rule, the skill evaluates the PromQL expression against historical data to determine optimal thresholds.

Threshold optimization uses histogram_quantile() and quantile_over_time() functions to find statistically appropriate trigger points. For example, a high CPU alert threshold might be adjusted from a static 80% to the p99 of the trailing 7-day range plus a configurable margin. The skill also recommends appropriate for durations based on metric volatility analysis.

Inhibition and grouping rules are generated for the Alertmanager configuration (alertmanager.yml) to prevent cascading alerts. The skill identifies parent-child relationships between alerts (e.g., NodeDown should inhibit all pod-level alerts on that node) and generates route and inhibit_rules configurations. All modified alert rules maintain the original recording rules and annotation templates.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-tuner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-tuner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/)
