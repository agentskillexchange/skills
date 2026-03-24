---
name: "Prometheus / Grafana MCP Server"
description: "Use this skill when you need to query Prometheus metrics with PromQL, inspect Grafana dashboards, or check alerting rules via AI. It enables agents to fetch time-series data, investigate metric anomalies, and verify alert states without direct access to the monitoring stack."
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-grafana-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grafana"  # from ase_tool_match
  github_stars: 72784  # from ase_github_stars (integer, not string)
  github_repo: "grafana/grafana"  # from ase_github_repo
  license: "AGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus / Grafana MCP Server

Use this skill when you need to query Prometheus metrics with PromQL, inspect Grafana dashboards, or check alerting rules via AI. It enables agents to fetch time-series data, investigate metric anomalies, and verify alert states without direct access to the monitoring stack.

## Overview

Use this skill when you need to query Prometheus metrics with PromQL, inspect Grafana dashboards, or check alerting rules via AI. It enables agents to fetch time-series data, investigate metric anomalies, and verify alert states without direct access to the monitoring stack.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-grafana-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-grafana-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-grafana-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-grafana-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install prometheus-grafana-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-grafana-mcp-server/
