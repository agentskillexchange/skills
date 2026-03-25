---
name: "Prometheus Alert Runbook Agent"
description: "Automates incident response for Prometheus alerts using PromQL queries, Alertmanager API, and Grafana dashboards. Maps alerts to diagnostic runbooks with remediation steps."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-runbook-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63278  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus Alert Runbook Agent

Automates incident response for Prometheus alerts using PromQL queries, Alertmanager API, and Grafana dashboards. Maps alerts to diagnostic runbooks with remediation steps.

## Overview

The Prometheus Alert Runbook Agent processes alerts from Alertmanager via its API (api/v2/alerts, api/v2/silences) and maps them to structured diagnostic runbooks. It executes PromQL queries against Prometheus HTTP API (/api/v1/query, /api/v1/query_range) to gather context for each alert.

When alerts fire, the agent retrieves metric history to determine trend direction and anomaly severity. For CPU/memory alerts, it queries process-level metrics (process_cpu_seconds_total, container_memory_working_set_bytes) and correlates with deployment events. For latency alerts, it analyzes histogram percentiles (histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))).

Runbook execution includes automated diagnostic steps: checking recent deployments via Kubernetes API, querying error logs via Loki LogQL, verifying downstream service health through blackbox_exporter probes, and testing database connectivity metrics (pg_up, mysql_up).

Grafana dashboard links are generated dynamically with time range and variable parameters for visual investigation. The agent creates Alertmanager silences for known maintenance windows and generates incident summaries with metric snapshots, timeline of events, and recommended remediation actions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-agent -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-runbook-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alert-runbook-agent/
