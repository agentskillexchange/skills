---
title: "Grafana Alert Router"
description: "The Grafana Alert Router skill processes incoming webhook payloads from Grafana Unified Alerting and routes them to the appropriate notification channels based on configurable label matchers. It integrates with Slack (via Block Kit API), PagerDuty (Events API v2), and OpsGenie (Alert API). The skill manages alert lifecycle states including firing, resolved, and silenced. It supports alert grouping by configurable labels to reduce notification noise, and can auto-create silences via the Grafana Silences API for scheduled maintenance windows. Advanced routing rules use CEL (Common Expression Language) expressions for complex matching logic. The skill maintains a local SQLite database of alert history for trend analysis and includes a dashboard template that visualizes alert frequency, MTTR, and channel distribution using Grafana&#8217;s own visualization capabilities."
source: "https://github.com/grafana/grafana"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Alert Router

The Grafana Alert Router skill processes incoming webhook payloads from Grafana Unified Alerting and routes them to the appropriate notification channels based on configurable label matchers. It integrates with Slack (via Block Kit API), PagerDuty (Events API v2), and OpsGenie (Alert API). The skill manages alert lifecycle states including firing, resolved, and silenced. It supports alert grouping by configurable labels to reduce notification noise, and can auto-create silences via the Grafana Silences API for scheduled maintenance windows. Advanced routing rules use CEL (Common Expression Language) expressions for complex matching logic. The skill maintains a local SQLite database of alert history for trend analysis and includes a dashboard template that visualizes alert frequency, MTTR, and channel distribution using Grafana&#8217;s own visualization capabilities.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-alert-router/)
