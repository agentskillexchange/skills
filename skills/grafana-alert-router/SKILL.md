---
name: "Grafana Alert Router"
description: "Routes Grafana alerting webhook payloads to Slack, PagerDuty, and OpsGenie channels based on label matching rules. Supports alert grouping and silence management via the Grafana Alerting API."
category: "Monitoring &amp; Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-alert-router/"
---
# Grafana Alert Router

Routes Grafana alerting webhook payloads to Slack, PagerDuty, and OpsGenie channels based on label matching rules. Supports alert grouping and silence management via the Grafana Alerting API.

## Overview

The Grafana Alert Router skill processes incoming webhook payloads from Grafana Unified Alerting and routes them to the appropriate notification channels based on configurable label matchers. It integrates with Slack (via Block Kit API), PagerDuty (Events API v2), and OpsGenie (Alert API).

The skill manages alert lifecycle states including firing, resolved, and silenced. It supports alert grouping by configurable labels to reduce notification noise, and can auto-create silences via the Grafana Silences API for scheduled maintenance windows.

Advanced routing rules use CEL (Common Expression Language) expressions for complex matching logic. The skill maintains a local SQLite database of alert history for trend analysis and includes a dashboard template that visualizes alert frequency, MTTR, and channel distribution using Grafana's own visualization capabilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-alert-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-alert-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-alert-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-alert-router -a codex
```

### OpenClaw

```bash
clawhub install grafana-alert-router
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-alert-router/)
