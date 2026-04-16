---
title: "Prometheus Alertmanager Bridge"
description: "Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alertmanager Bridge

The Prometheus Alertmanager Bridge skill receives webhook notifications from Prometheus Alertmanager and transforms them into rich notifications for messaging platforms. It uses Microsoft Teams Adaptive Cards, Discord embeds via webhook API, and Telegram Bot API with inline keyboards for alert acknowledgment.


Alert correlation uses PromQL queries against the Prometheus HTTP API to fetch related metrics and attach sparkline graphs generated with the QuickChart.io API. The skill groups related alerts using configurable inhibition rules and time-based correlation windows to reduce notification fatigue.


Template customization supports Go template syntax matching Alertmanager’s native templating. The skill maintains alert state in a Redis cache for deduplication and tracks acknowledgment status across platforms. Runbook links are automatically generated from alert labels using configurable URL templates. The skill exposes its own metrics endpoint for monitoring notification delivery rates and latencies.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/)
