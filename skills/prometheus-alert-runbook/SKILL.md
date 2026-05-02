---
title: "Prometheus Alert Runbook"
description: "Execute structured runbook procedures triggered by Prometheus AlertManager webhooks. Queries PromQL metrics via the Prometheus HTTP API for automated incident diagnosis and escalation."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook

The Prometheus Alert Runbook skill provides automated incident response procedures triggered by Prometheus AlertManager webhook notifications. When alerts fire, it queries the Prometheus HTTP API (/api/v1/query, /api/v1/query_range) using PromQL expressions to gather diagnostic context—rate(http_requests_total{status=~”5..”}[5m]) for error rate spikes, node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes for memory pressure, and container_cpu_usage_seconds_total for CPU saturation. The skill maps alert labels (alertname, severity, namespace, pod) to specific runbook procedures stored as structured decision trees. Each runbook step executes diagnostic queries, evaluates thresholds, and branches to remediation actions or escalation paths. It integrates with AlertManager API (/api/v2/alerts, /api/v2/silences) for alert acknowledgment and silence creation during maintenance windows. The skill supports Grafana annotation creation via the Grafana HTTP API for incident timeline tracking, generates structured incident summaries with affected services, blast radius estimation, and recommended actions, and can trigger PagerDuty incidents via the Events API v2 for human escalation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook/)
