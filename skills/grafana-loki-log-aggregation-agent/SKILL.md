---
name: "Grafana Loki Log Aggregation Agent"
description: "Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/"
tool_ecosystem:
  tool: "grafana"
  github_stars: 72796
  github_repo: "grafana/grafana"
  license: "AGPL-3.0"
  maintained: true
---

# Grafana Loki Log Aggregation Agent

Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces.

## Overview

The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-aggregation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-aggregation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-aggregation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-loki-log-aggregation-agent -a codex
```

### OpenClaw

```bash
clawhub install grafana-loki-log-aggregation-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/
