---
name: "Metabase Dashboard Snapshot & Alerting"
description: "Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/metabase-dashboard-snapshot-alerting-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Metabase Dashboard Snapshot & Alerting

Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments.

## Overview

Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill metabase-dashboard-snapshot-alerting-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill metabase-dashboard-snapshot-alerting-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill metabase-dashboard-snapshot-alerting-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill metabase-dashboard-snapshot-alerting-2 -a codex
```

### OpenClaw

```bash
clawhub install metabase-dashboard-snapshot-alerting-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/metabase-dashboard-snapshot-alerting-2/
