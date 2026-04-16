---
title: "Grafana Dashboard Sync Agent"
description: "Synchronizes Grafana dashboards between instances using the Grafana HTTP API v5. Handles provisioning, folder management, and datasource remapping for multi-environment observability setups."
verification: "security_reviewed"
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
  license: "AGPL-3.0"
---

# Grafana Dashboard Sync Agent

The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/)
