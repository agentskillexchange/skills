---
title: "Prometheus Alert Rule Synthesizer"
description: "Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Synthesizer

The Prometheus Alert Rule Synthesizer connects to your Prometheus server via the HTTP API v1 to analyze historical metric data and automatically generate intelligent alerting rules. It queries the /api/v1/query_range endpoint to establish baseline patterns for key metrics like request latency, error rates, CPU utilization, and memory consumption. Using statistical analysis on PromQL query results, it calculates dynamic thresholds that account for daily and weekly seasonality patterns. Generated alert rules include proper for-duration clauses, severity labels, and detailed annotation templates with runbook links. The agent integrates with the Alertmanager API to configure routing trees, grouping rules, and inhibition policies. It connects to PagerDuty Events API v2 for critical alert escalation and Slack Incoming Webhooks for warning-level notifications. Alert rules are output in standard Prometheus YAML format ready for deployment.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-rule-synthesizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-rule-synthesizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)
