---
name: "Metabase Dashboard Snapshot & Alerting"
description: "Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
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

**Metabase Dashboard Snapshot & Alerting** is built around PagerDuty incident response platform. The underlying ecosystem is represented by `PagerDuty/pdjs` (69+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like incidents, escalation policies, schedules, services, responders, analytics and preserving the operational context that matters for real tasks.

For incident response, the skill uses pagerduty APIs to pull the exact monitors, traces, schedules, or logs that matter, reducing dashboard hopping and making it easier to produce a handoff-quality timeline. The original use case is clear: Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments. The implementation typically relies on incidents, escalation policies, schedules, services, responders, analytics, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses incidents, escalation policies, schedules, services, responders, analytics instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as on-call checks, incident routing, and response coordination.

Key integration points include on-call checks, incident routing, and response coordination. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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
