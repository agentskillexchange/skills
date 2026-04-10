---
name: Prometheus Alert Router
description: Routes and escalates Prometheus AlertManager notifications based on severity
  and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs
  for multi-channel incident routing.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
