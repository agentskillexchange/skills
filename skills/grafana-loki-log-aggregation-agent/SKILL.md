---
title: "Grafana Loki Log Aggregation Agent"
description: "Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces."
slug: "grafana-loki-log-aggregation-agent"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/"
listed: true
---

# Grafana Loki Log Aggregation Agent

Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install grafana-loki-log-aggregation-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/)
