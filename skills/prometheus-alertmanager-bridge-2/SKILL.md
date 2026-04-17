---
title: "Prometheus Alertmanager Bridge"
description: "The Prometheus Alertmanager Bridge skill receives webhook notifications from Prometheus Alertmanager and transforms them into rich notifications for messaging platforms. It uses Microsoft Teams Adaptive Cards, Discord embeds via webhook API, and Telegram Bot API with inline keyboards for alert acknowledgment.\nAlert correlation uses PromQL queries against the Prometheus HTTP API to fetch related metrics and attach sparkline graphs generated with the QuickChart.io API. The skill groups related alerts using configurable inhibition rules and time-based correlation windows to reduce notification fatigue.\nTemplate customization supports Go template syntax matching Alertmanager’s native templating. The skill maintains alert state in a Redis cache for deduplication and tracks acknowledgment status across platforms. Runbook links are automatically generated from alert labels using configurable URL templates. The skill exposes its own metrics endpoint for monitoring notification delivery rates and latencies."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alertmanager Bridge

The Prometheus Alertmanager Bridge skill receives webhook notifications from Prometheus Alertmanager and transforms them into rich notifications for messaging platforms. It uses Microsoft Teams Adaptive Cards, Discord embeds via webhook API, and Telegram Bot API with inline keyboards for alert acknowledgment.
Alert correlation uses PromQL queries against the Prometheus HTTP API to fetch related metrics and attach sparkline graphs generated with the QuickChart.io API. The skill groups related alerts using configurable inhibition rules and time-based correlation windows to reduce notification fatigue.
Template customization supports Go template syntax matching Alertmanager’s native templating. The skill maintains alert state in a Redis cache for deduplication and tracks acknowledgment status across platforms. Runbook links are automatically generated from alert labels using configurable URL templates. The skill exposes its own metrics endpoint for monitoring notification delivery rates and latencies.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alertmanager-bridge-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alertmanager-bridge-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/)
