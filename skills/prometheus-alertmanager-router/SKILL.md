---
title: Prometheus AlertManager Router
description: The Prometheus AlertManager Router skill provides intelligent alert routing
  and management through the AlertManager HTTP API. It enables agents to programmatically
  create, modify, and debug complex routing trees that determine how alerts flow from
  Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email.
  Key features include routing tree visualization and validation before applying changes,
  automatic silence creation during maintenance windows with scheduled expiry, and
  inhibition rule management to suppress dependent alerts when root-cause alerts are
  already firing. The skill can analyze alert group patterns to suggest routing optimizations.
  It supports match and match_re label-based routing, continue flags for multi-receiver
  fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver
  template customization using Go template syntax. Integration with Prometheus’s /api/v1/rules
  endpoint enables correlation between recording rules, alerting rules, and their
  AlertManager routing destinations for end-to-end observability pipeline verification.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-router/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Prometheus AlertManager Router

The Prometheus AlertManager Router skill provides intelligent alert routing and management through the AlertManager HTTP API. It enables agents to programmatically create, modify, and debug complex routing trees that determine how alerts flow from Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email. Key features include routing tree visualization and validation before applying changes, automatic silence creation during maintenance windows with scheduled expiry, and inhibition rule management to suppress dependent alerts when root-cause alerts are already firing. The skill can analyze alert group patterns to suggest routing optimizations. It supports match and match_re label-based routing, continue flags for multi-receiver fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver template customization using Go template syntax. Integration with Prometheus’s /api/v1/rules endpoint enables correlation between recording rules, alerting rules, and their AlertManager routing destinations for end-to-end observability pipeline verification.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)
