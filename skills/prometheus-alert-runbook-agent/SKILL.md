---
title: "Prometheus Alert Runbook Agent"
description: "The Prometheus Alert Runbook Agent processes alerts from Alertmanager via its API (api/v2/alerts, api/v2/silences) and maps them to structured diagnostic runbooks. It executes PromQL queries against Prometheus HTTP API (/api/v1/query, /api/v1/query_range) to gather context for each alert.\nWhen alerts fire, the agent retrieves metric history to determine trend direction and anomaly severity. For CPU/memory alerts, it queries process-level metrics (process_cpu_seconds_total, container_memory_working_set_bytes) and correlates with deployment events. For latency alerts, it analyzes histogram percentiles (histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))).\nRunbook execution includes automated diagnostic steps: checking recent deployments via Kubernetes API, querying error logs via Loki LogQL, verifying downstream service health through blackbox_exporter probes, and testing database connectivity metrics (pg_up, mysql_up).\nGrafana dashboard links are generated dynamically with time range and variable parameters for visual investigation. The agent creates Alertmanager silences for known maintenance windows and generates incident summaries with metric snapshots, timeline of events, and recommended remediation actions."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook Agent

The Prometheus Alert Runbook Agent processes alerts from Alertmanager via its API (api/v2/alerts, api/v2/silences) and maps them to structured diagnostic runbooks. It executes PromQL queries against Prometheus HTTP API (/api/v1/query, /api/v1/query_range) to gather context for each alert.
When alerts fire, the agent retrieves metric history to determine trend direction and anomaly severity. For CPU/memory alerts, it queries process-level metrics (process_cpu_seconds_total, container_memory_working_set_bytes) and correlates with deployment events. For latency alerts, it analyzes histogram percentiles (histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))).
Runbook execution includes automated diagnostic steps: checking recent deployments via Kubernetes API, querying error logs via Loki LogQL, verifying downstream service health through blackbox_exporter probes, and testing database connectivity metrics (pg_up, mysql_up).
Grafana dashboard links are generated dynamically with time range and variable parameters for visual investigation. The agent creates Alertmanager silences for known maintenance windows and generates incident summaries with metric snapshots, timeline of events, and recommended remediation actions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-runbook-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-runbook-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-agent/)
