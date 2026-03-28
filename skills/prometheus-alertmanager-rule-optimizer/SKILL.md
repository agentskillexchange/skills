---
name: "Prometheus AlertManager Rule Optimizer"
description: "Analyzes Prometheus alerting rules and AlertManager configuration to reduce alert fatigue. Uses PromQL query analysis and historical firing patterns to suggest rule consolidation and threshold adjustments."
category: "Monitoring & Alerts"
framework: "Claude Code"
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

# Prometheus AlertManager Rule Optimizer

Analyzes Prometheus alerting rules and AlertManager configuration to reduce alert fatigue. Uses PromQL query analysis and historical firing patterns to suggest rule consolidation and threshold adjustments.

## Overview

The Prometheus AlertManager Rule Optimizer tackles alert fatigue by performing deep analysis of your Prometheus alerting rules and AlertManager routing configuration. It connects to the Prometheus HTTP API to fetch rule definitions, evaluate PromQL expressions, and retrieve historical alert firing data.

The optimizer identifies common anti-patterns: overly sensitive thresholds that fire on transient spikes, redundant rules that generate duplicate alerts, missing inhibition rules that should suppress correlated alerts, and poorly configured group_wait/group_interval/repeat_interval timings. It produces actionable recommendations with before/after PromQL comparisons.

Additionally, it analyzes AlertManager routing trees to detect dead routes, overlapping matchers, and missing fallback receivers. The agent generates optimized YAML configurations that can be applied directly, along with a simulation report showing projected alert volume reduction. Supports integration with Grafana Annotations API to mark optimization events on dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-optimizer -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-rule-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alertmanager-rule-optimizer/
