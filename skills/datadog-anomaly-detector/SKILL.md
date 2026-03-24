---
name: "Datadog Anomaly Detector"
description: "Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-anomaly-detector/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Anomaly Detector

Leverages the Datadog API v2 metrics and events endpoints to detect anomalous patterns. Uses the Datadog Monitors API to create dynamic thresholds and sends escalations via OpsGenie REST API.

## Overview

The Datadog Anomaly Detector skill enables AI agents to perform proactive infrastructure monitoring by interfacing with the Datadog API v2. It queries the /api/v2/query/timeseries endpoint to pull metric data across configurable time windows, supporting all Datadog metric types including count, rate, gauge, and distribution.

Anomaly detection uses a combination of Datadog built-in anomaly functions (anomalies() with basic, agile, and robust algorithms) and custom statistical analysis. The skill creates and manages monitors via the /api/v1/monitor endpoint, implementing dynamic thresholds that adapt to seasonal patterns detected through Fourier decomposition of historical data.

When anomalies trigger, the skill creates OpsGenie alerts via the REST API v2 (/v2/alerts), attaching metric visualizations generated from the Datadog Embeddable Graphs API. Incident timelines are automatically populated with correlated events from the Datadog Events API, including recent deployments, configuration changes, and related monitor state transitions. The skill maintains an anomaly knowledge base in PostgreSQL for pattern recognition across incidents.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-anomaly-detector -a codex
```

### OpenClaw

```bash
clawhub install datadog-anomaly-detector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-anomaly-detector/
