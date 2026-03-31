---
name: "Prometheus Alertmanager Bridge"
description: "Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/"
---
# Prometheus Alertmanager Bridge

Bridges Prometheus Alertmanager notifications to Microsoft Teams, Discord, and Telegram using adaptive card templates and PromQL-based alert correlation.

## Overview

The Prometheus Alertmanager Bridge skill receives webhook notifications from Prometheus Alertmanager and transforms them into rich notifications for messaging platforms. It uses Microsoft Teams Adaptive Cards, Discord embeds via webhook API, and Telegram Bot API with inline keyboards for alert acknowledgment.

Alert correlation uses PromQL queries against the Prometheus HTTP API to fetch related metrics and attach sparkline graphs generated with the QuickChart.io API. The skill groups related alerts using configurable inhibition rules and time-based correlation windows to reduce notification fatigue.

Template customization supports Go template syntax matching Alertmanager’s native templating. The skill maintains alert state in a Redis cache for deduplication and tracks acknowledgment status across platforms. Runbook links are automatically generated from alert labels using configurable URL templates. The skill exposes its own metrics endpoint for monitoring notification delivery rates and latencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-bridge-2 -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-bridge-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge-2/)
