---
title: "Grafana Loki Log Aggregation Agent"
description: "The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points."
source: "https://github.com/grafana/loki"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Aggregation Agent

The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/)
