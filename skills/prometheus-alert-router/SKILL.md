---
title: Prometheus Alert Router
description: The Prometheus Alert Router skill provides intelligent routing of Prometheus
  AlertManager webhook payloads to the appropriate incident response channels. It
  parses alert labels and annotations to determine severity, team ownership, and escalation
  path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie
  Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time
  team notifications. The skill includes configurable routing rules using label matchers
  (regex and exact match), silence management via the AlertManager API, and deduplication
  logic to prevent alert storms. Features automatic grouping of related alerts, customizable
  templates for notification messages, and runbook URL injection. Built-in retry logic
  handles transient API failures with exponential backoff.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-router/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# Prometheus Alert Router

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
