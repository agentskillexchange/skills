---
title: "Grafana Loki Log Aggregation Agent"
description: "Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces."
verification: "security_reviewed"
source: "https://github.com/grafana/loki"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Aggregation Agent

The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-loki-log-aggregation-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-loki-log-aggregation-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/)
