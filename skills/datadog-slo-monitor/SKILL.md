---
name: "Datadog SLO Monitor"
description: "Monitors Datadog Service Level Objectives and burn rate alerts via the Datadog API v2. Generates SLO compliance reports and triggers remediation workflows when error budgets are exhausted."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-slo-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog SLO Monitor

Monitors Datadog Service Level Objectives and burn rate alerts via the Datadog API v2. Generates SLO compliance reports and triggers remediation workflows when error budgets are exhausted.

## Overview

The Datadog SLO Monitor skill continuously tracks Service Level Objectives defined in Datadog using the SLO API v2 endpoints. It calculates real-time burn rates across 5-minute, 1-hour, and 30-day windows to detect fast-burn and slow-burn scenarios. When error budgets approach exhaustion thresholds, the skill triggers configurable remediation workflows including automated rollbacks via deployment APIs, traffic shifting through load balancer configurations, and team notifications via Datadog Events. Features include SLO history export to CSV for compliance reporting, multi-SLO dashboard generation using Datadog Dashboards API, and integration with Datadog Monitors API for creating composite alert conditions. Supports custom burn rate alerting rules and weekly SLO digest summaries sent via email or Slack.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-slo-monitor -a codex
```

### OpenClaw

```bash
clawhub install datadog-slo-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-slo-monitor/
