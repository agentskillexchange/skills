---
title: Grafana Dashboard Sync Agent
description: The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple
  Grafana instances using the Grafana HTTP API. It exports dashboards from source
  instances including all panel configurations, variable definitions, and annotation
  settings. During import to target instances, the agent automatically remaps datasource
  UIDs to match the target environment, ensuring panels connect to the correct Prometheus,
  Elasticsearch, or InfluxDB instances. Folder structures are preserved and created
  as needed in target instances. The agent supports selective sync based on folder,
  tag, or dashboard title patterns. Version conflict detection prevents overwriting
  newer changes in target instances. A dry-run mode previews all changes before applying
  them. The sync process maintains an audit log of all dashboard changes with before/after
  snapshots. Integration with Git repositories enables dashboard-as-code workflows
  where synced dashboards are committed as JSON files for version control.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/
category:
- Monitoring &amp; Alerts
framework:
- Gemini
---

# Grafana Dashboard Sync Agent

The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/)
