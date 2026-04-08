---
title: Datadog Anomaly Alert Router
description: 'The Datadog Anomaly Alert Router processes anomaly detection alerts
  from Datadog monitors and routes them to the appropriate incident response channels.
  It listens to Datadog webhook payloads containing monitor state transitions (OK
  → Alert → Warn → No Data) and applies configurable routing rules based on monitor
  tags, alert severity, and affected service. The skill queries the Datadog Monitors
  API v1 /api/v1/monitor/{monitor_id} endpoint to fetch full monitor configuration
  including thresholds, evaluation windows, and tagged scopes. Severity classification
  uses a three-tier model: P1 alerts trigger PagerDuty incidents via the PagerDuty
  Events API v2 /enqueue endpoint, P2 alerts post to team-specific Slack channels
  via incoming webhooks, and P3 alerts are logged to a Datadog Event stream via POST
  /api/v1/events. The router maintains an alert correlation engine that groups related
  anomalies by service tag and time window, preventing alert storms from generating
  duplicate pages. Includes automatic escalation: if a P2 alert remains unacknowledged
  for a configurable timeout (checked via Datadog /api/v1/monitor/{id}?group_states=alert),
  it escalates to P1. Dashboard integration exposes routing statistics through Datadog
  custom metrics via the /api/v2/series endpoint.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-anomaly-alert-router/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# Datadog Anomaly Alert Router

The Datadog Anomaly Alert Router processes anomaly detection alerts from Datadog monitors and routes them to the appropriate incident response channels. It listens to Datadog webhook payloads containing monitor state transitions (OK → Alert → Warn → No Data) and applies configurable routing rules based on monitor tags, alert severity, and affected service. The skill queries the Datadog Monitors API v1 /api/v1/monitor/{monitor_id} endpoint to fetch full monitor configuration including thresholds, evaluation windows, and tagged scopes. Severity classification uses a three-tier model: P1 alerts trigger PagerDuty incidents via the PagerDuty Events API v2 /enqueue endpoint, P2 alerts post to team-specific Slack channels via incoming webhooks, and P3 alerts are logged to a Datadog Event stream via POST /api/v1/events. The router maintains an alert correlation engine that groups related anomalies by service tag and time window, preventing alert storms from generating duplicate pages. Includes automatic escalation: if a P2 alert remains unacknowledged for a configurable timeout (checked via Datadog /api/v1/monitor/{id}?group_states=alert), it escalates to P1. Dashboard integration exposes routing statistics through Datadog custom metrics via the /api/v2/series endpoint.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-alert-router/)
