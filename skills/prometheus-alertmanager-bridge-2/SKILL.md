---
title: "Prometheus Alertmanager Bridge"
description: "Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/)
