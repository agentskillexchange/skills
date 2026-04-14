---
title: "Grafana Dashboard Sync Agent"
description: "Synchronizes Grafana dashboards between instances using the Grafana HTTP API v5. Handles provisioning, folder management, and datasource remapping for multi-environment observability setups."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/)
