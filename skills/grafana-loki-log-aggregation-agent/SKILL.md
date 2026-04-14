---
title: "Grafana Loki Log Aggregation Agent"
description: "Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# Grafana Loki Log Aggregation Agent

The Grafana Loki Log Aggregation Agent skill sets up and manages centralized logging infrastructure using Grafana Loki as the log storage backend. It configures Promtail agents for log collection from Kubernetes pods, systemd journals, Docker containers, and flat files with automatic label extraction and pipeline stages. The skill writes LogQL queries for log searching, filtering, and metric generation from log lines. Multi-tenant log routing ensures proper data isolation between teams and environments. Integration with Grafana Tempo enables jumping from log entries directly to correlated distributed traces using trace IDs embedded in structured logs. The skill manages retention policies, compaction schedules, and chunk storage configuration for cost-effective long-term log retention on object storage backends like S3 or GCS. Alerting rules defined in LogQL can trigger notifications through Grafana Alerting contact points.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/)
