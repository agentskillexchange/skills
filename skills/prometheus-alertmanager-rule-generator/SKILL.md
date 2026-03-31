---
name: "Prometheus AlertManager Rule Generator"
description: "Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation."
category: "Monitoring &amp; Alerts"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/"
---
# Prometheus AlertManager Rule Generator

Generates Prometheus alerting rules and AlertManager routing configs from natural language descriptions. Leverages PromQL query builder and the Alertmanager API v2 for live rule validation.

## Overview

The Prometheus AlertManager Rule Generator converts natural language alert descriptions into production-ready PromQL alerting rules and AlertManager routing configurations. It uses the Prometheus HTTP API to validate queries against live metric endpoints, ensuring rules match actual metric names and label sets. The skill generates YAML rule groups compatible with Prometheus Operator PrometheusRule CRDs and standalone rule_files configurations. It supports complex PromQL functions including rate(), histogram_quantile(), predict_linear(), and absent(). AlertManager routing trees are generated with proper grouping, inhibition rules, and receiver configurations for Slack, PagerDuty, Opsgenie, and email. The skill includes a dry-run mode that evaluates rules against the last 24 hours of data to estimate alert frequency, preventing noisy alerting. It also handles recording rules for expensive queries that need pre-computation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-generator -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-rule-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rule-generator/)
