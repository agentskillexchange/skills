---
name: "Prometheus Alert Rule Synthesizer"
description: "Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/"
---
# Prometheus Alert Rule Synthesizer

Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation.

## Overview

The Prometheus Alert Rule Synthesizer connects to your Prometheus server via the HTTP API v1 to analyze historical metric data and automatically generate intelligent alerting rules. It queries the /api/v1/query_range endpoint to establish baseline patterns for key metrics like request latency, error rates, CPU utilization, and memory consumption. Using statistical analysis on PromQL query results, it calculates dynamic thresholds that account for daily and weekly seasonality patterns. Generated alert rules include proper for-duration clauses, severity labels, and detailed annotation templates with runbook links. The agent integrates with the Alertmanager API to configure routing trees, grouping rules, and inhibition policies. It connects to PagerDuty Events API v2 for critical alert escalation and Slack Incoming Webhooks for warning-level notifications. Alert rules are output in standard Prometheus YAML format ready for deployment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-synthesizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-synthesizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-synthesizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-synthesizer -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-rule-synthesizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)
