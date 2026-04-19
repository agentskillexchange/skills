---
title: "Prometheus Alert Router"
description: "The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff."
source: "https://github.com/prometheus/prometheus"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Router

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
