---
name: "Grafana Dashboard Sync Agent"
description: "Synchronizes Grafana dashboards between instances using the Grafana HTTP API v5. Handles provisioning, folder management, and datasource remapping for multi-environment observability setups."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grafana"  # from ase_tool_match
  github_stars: 72796  # from ase_github_stars (integer, not string)
  github_repo: "grafana/grafana"  # from ase_github_repo
  license: "AGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Grafana Dashboard Sync Agent

Synchronizes Grafana dashboards between instances using the Grafana HTTP API v5. Handles provisioning, folder management, and datasource remapping for multi-environment observability setups.

## Overview

The Grafana Dashboard Sync Agent manages dashboard lifecycle across multiple Grafana instances using the Grafana HTTP API. It exports dashboards from source instances including all panel configurations, variable definitions, and annotation settings. During import to target instances, the agent automatically remaps datasource UIDs to match the target environment, ensuring panels connect to the correct Prometheus, Elasticsearch, or InfluxDB instances. Folder structures are preserved and created as needed in target instances. The agent supports selective sync based on folder, tag, or dashboard title patterns. Version conflict detection prevents overwriting newer changes in target instances. A dry-run mode previews all changes before applying them. The sync process maintains an audit log of all dashboard changes with before/after snapshots. Integration with Git repositories enables dashboard-as-code workflows where synced dashboards are committed as JSON files for version control.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-sync-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-dashboard-sync-agent/
