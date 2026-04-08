---
title: Prometheus Alert Runbook
description: The Prometheus Alert Runbook skill provides automated incident response
  procedures triggered by Prometheus AlertManager webhook notifications. When alerts
  fire, it queries the Prometheus HTTP API (/api/v1/query, /api/v1/query_range) using
  PromQL expressions to gather diagnostic context—rate(http_requests_total{status=~”5..”}[5m])
  for error rate spikes, node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes
  for memory pressure, and container_cpu_usage_seconds_total for CPU saturation. The
  skill maps alert labels (alertname, severity, namespace, pod) to specific runbook
  procedures stored as structured decision trees. Each runbook step executes diagnostic
  queries, evaluates thresholds, and branches to remediation actions or escalation
  paths. It integrates with AlertManager API (/api/v2/alerts, /api/v2/silences) for
  alert acknowledgment and silence creation during maintenance windows. The skill
  supports Grafana annotation creation via the Grafana HTTP API for incident timeline
  tracking, generates structured incident summaries with affected services, blast
  radius estimation, and recommended actions, and can trigger PagerDuty incidents
  via the Events API v2 for human escalation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# Prometheus Alert Runbook

The Prometheus Alert Runbook skill provides automated incident response procedures triggered by Prometheus AlertManager webhook notifications. When alerts fire, it queries the Prometheus HTTP API (/api/v1/query, /api/v1/query_range) using PromQL expressions to gather diagnostic context—rate(http_requests_total{status=~”5..”}[5m]) for error rate spikes, node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes for memory pressure, and container_cpu_usage_seconds_total for CPU saturation. The skill maps alert labels (alertname, severity, namespace, pod) to specific runbook procedures stored as structured decision trees. Each runbook step executes diagnostic queries, evaluates thresholds, and branches to remediation actions or escalation paths. It integrates with AlertManager API (/api/v2/alerts, /api/v2/silences) for alert acknowledgment and silence creation during maintenance windows. The skill supports Grafana annotation creation via the Grafana HTTP API for incident timeline tracking, generates structured incident summaries with affected services, blast radius estimation, and recommended actions, and can trigger PagerDuty incidents via the Events API v2 for human escalation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook/)
