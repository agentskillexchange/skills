---
name: "Metrics Dashboard Builder"
description: "Use this skill when you need to generate a metrics dashboard definition (Grafana JSON, Datadog dashboard, or CloudWatch) based on a description of what you want to monitor. It creates dashboard configs from natural language requirements, covering chart types, metric queries, and threshold lines."
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/metrics-dashboard-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Metrics Dashboard Builder

Use this skill when you need to generate a metrics dashboard definition (Grafana JSON, Datadog dashboard, or CloudWatch) based on a description of what you want to monitor. It creates dashboard configs from natural language requirements, covering chart types, metric queries, and threshold lines.

## Overview

Use this skill when you need to generate a metrics dashboard definition (Grafana JSON, Datadog dashboard, or CloudWatch) based on a description of what you want to monitor. It creates dashboard configs from natural language requirements, covering chart types, metric queries, and threshold lines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill metrics-dashboard-builder -a codex
```

### OpenClaw

```bash
clawhub install metrics-dashboard-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/metrics-dashboard-builder/
