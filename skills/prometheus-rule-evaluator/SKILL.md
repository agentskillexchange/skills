---
name: "Prometheus Rule Evaluator"
description: "Validates and tests Prometheus alerting rules against historical metrics data using the Prometheus HTTP API /api/v1/query_range endpoint. Runs rule simulations with configurable time windows and threshold testing."
category: "Monitoring &amp; Alerts"
framework: "Claude Agents"
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
tool_ecosystem:
  tool: prometheus
  github_repo: prometheus/prometheus
  github_stars: 63306
  license: Apache-2.0
  maintained: true
---
# Prometheus Rule Evaluator

Validates and tests Prometheus alerting rules against historical metrics data using the Prometheus HTTP API /api/v1/query_range endpoint. Runs rule simulations with configurable time windows and threshold testing.

## Overview

The Prometheus Rule Evaluator validates alerting and recording rules before deployment to production Prometheus instances. It parses rule YAML files following the Prometheus rule_group schema and tests each rule expression against historical metrics data via the Prometheus HTTP API /api/v1/query_range endpoint. For each rule, the evaluator runs the PromQL expression across configurable time windows (default: 7 days) to determine historical firing patterns. The skill reports false positive rates, alert frequency, and duration distributions to help tune thresholds before deployment. It supports all PromQL functions including rate(), histogram_quantile(), predict_linear(), and aggregation operators. Test scenarios can be defined in YAML format specifying expected alert states at given timestamps, enabling unit-test-style validation of alerting logic. The evaluator integrates with the Prometheus /api/v1/rules endpoint to compare proposed rules against existing active rules, detecting conflicts and redundancies. Output includes a coverage report showing which metrics are monitored, gaps in monitoring, and recommendations for additional rules based on available metric labels. Compatible with Thanos and Cortex long-term storage backends via their compatible query APIs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-rule-evaluator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-rule-evaluator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-rule-evaluator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-rule-evaluator -a codex
```

### OpenClaw

```bash
clawhub install prometheus-rule-evaluator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-rule-evaluator/)
