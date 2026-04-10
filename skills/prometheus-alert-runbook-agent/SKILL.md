---
name: Prometheus Alert Runbook Agent
description: Automates incident response for Prometheus alerts using PromQL queries,
  Alertmanager API, and Grafana dashboards. Maps alerts to diagnostic runbooks with
  remediation steps.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-runbook-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---
# Prometheus Alert Runbook Agent

The Prometheus Alert Runbook Agent processes alerts from Alertmanager via its API (api/v2/alerts, api/v2/silences) and maps them to structured diagnostic runbooks. It executes PromQL queries against Prometheus HTTP API (/api/v1/query, /api/v1/query_range) to gather context for each alert.
When alerts fire, the agent retrieves metric history to determine trend direction and anomaly severity. For CPU/memory alerts, it queries process-level metrics (process_cpu_seconds_total, container_memory_working_set_bytes) and correlates with deployment events. For latency alerts, it analyzes histogram percentiles (histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))).
Runbook execution includes automated diagnostic steps: checking recent deployments via Kubernetes API, querying error logs via Loki LogQL, verifying downstream service health through blackbox_exporter probes, and testing database connectivity metrics (pg_up, mysql_up).
Grafana dashboard links are generated dynamically with time range and variable parameters for visual investigation. The agent creates Alertmanager silences for known maintenance windows and generates incident summaries with metric snapshots, timeline of events, and recommended remediation actions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-agent/)
