---
title: "Prometheus Alertmanager Bridge"
description: "Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation."
slug: "prometheus-alertmanager-bridge-2"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/"
---

# Prometheus Alertmanager Bridge

Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install prometheus-alertmanager-bridge-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prometheus Alertmanager Bridge skill receives webhook notifications from Prometheus Alertmanager and transforms them into rich notifications for messaging platforms. It uses Microsoft Teams Adaptive Cards, Discord embeds via webhook API, and Telegram Bot API with inline keyboards for alert acknowledgment.
Alert correlation uses PromQL queries against the Prometheus HTTP API to fetch related metrics and attach sparkline graphs generated with the QuickChart.io API. The skill groups related alerts using configurable inhibition rules and time-based correlation windows to reduce notification fatigue.
Template customization supports Go template syntax matching Alertmanager’s native templating. The skill maintains alert state in a Redis cache for deduplication and tracks acknowledgment status across platforms. Runbook links are automatically generated from alert labels using configurable URL templates. The skill exposes its own metrics endpoint for monitoring notification delivery rates and latencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/)
