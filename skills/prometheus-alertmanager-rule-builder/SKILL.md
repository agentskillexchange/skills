---
name: "Prometheus AlertManager Rule Builder"
description: "Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63289  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus AlertManager Rule Builder

Generates Prometheus alerting rules and AlertManager routing configs using PromQL validation via the Prometheus HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configurations.

## Overview

The Prometheus AlertManager Rule Builder creates and validates alerting rules by interfacing with the Prometheus HTTP API for PromQL expression validation and metric discovery. It generates recording rules for performance-critical queries and alerting rules with proper for-duration, severity labels, and runbook annotations following SRE best practices. The skill configures AlertManager routing trees with proper grouping, inhibition rules, and silence management via the AlertManager API. It supports receiver configurations for PagerDuty (using the Events API v2), OpsGenie (via the Alert API), Slack (using Block Kit message formatting), and custom webhook endpoints. The builder implements alert fatigue reduction strategies including proper group_wait, group_interval, and repeat_interval tuning based on alert severity. It validates rule configurations against promtool for syntax correctness and tests alert conditions using Prometheus’s unit testing framework with mock time series data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rule-builder -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-rule-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alertmanager-rule-builder/
