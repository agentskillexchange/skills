---
title: Grafana Alert Router
description: The Grafana Alert Router skill processes incoming webhook payloads from
  Grafana Unified Alerting and routes them to the appropriate notification channels
  based on configurable label matchers. It integrates with Slack (via Block Kit API),
  PagerDuty (Events API v2), and OpsGenie (Alert API). The skill manages alert lifecycle
  states including firing, resolved, and silenced. It supports alert grouping by configurable
  labels to reduce notification noise, and can auto-create silences via the Grafana
  Silences API for scheduled maintenance windows. Advanced routing rules use CEL (Common
  Expression Language) expressions for complex matching logic. The skill maintains
  a local SQLite database of alert history for trend analysis and includes a dashboard
  template that visualizes alert frequency, MTTR, and channel distribution using Grafana’s
  own visualization capabilities.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-alert-router/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# Grafana Alert Router

The Grafana Alert Router skill processes incoming webhook payloads from Grafana Unified Alerting and routes them to the appropriate notification channels based on configurable label matchers. It integrates with Slack (via Block Kit API), PagerDuty (Events API v2), and OpsGenie (Alert API). The skill manages alert lifecycle states including firing, resolved, and silenced. It supports alert grouping by configurable labels to reduce notification noise, and can auto-create silences via the Grafana Silences API for scheduled maintenance windows. Advanced routing rules use CEL (Common Expression Language) expressions for complex matching logic. The skill maintains a local SQLite database of alert history for trend analysis and includes a dashboard template that visualizes alert frequency, MTTR, and channel distribution using Grafana’s own visualization capabilities.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-alert-router/)
