---
title: "Grafana Dashboard Sync Agent"
description: "The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control."
source: "https://github.com/grafana/grafana"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Sync Agent

The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/)
