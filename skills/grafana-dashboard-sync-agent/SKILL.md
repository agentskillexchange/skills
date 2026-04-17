---
title: "Grafana Dashboard Sync Agent"
description: "The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Sync Agent

The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-sync-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/grafana-dashboard-sync-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/)
