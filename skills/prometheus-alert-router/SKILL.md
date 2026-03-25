---
name: "Prometheus Alert Router"
description: "Routes and escalates Prometheus AlertManager notifications based on severity and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs for multi-channel incident routing."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-router/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63289  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus Alert Router

Routes and escalates Prometheus AlertManager notifications based on severity and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs for multi-channel incident routing.

## Overview

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-router
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alert-router/
