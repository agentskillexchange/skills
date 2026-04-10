---
title: "Prometheus AlertManager Router"
description: "Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules."
slug: "prometheus-alertmanager-router"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-router/"
---

# Prometheus AlertManager Router

Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules.

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
clawhub install prometheus-alertmanager-router
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prometheus AlertManager Router skill provides intelligent alert routing and management through the AlertManager HTTP API. It enables agents to programmatically create, modify, and debug complex routing trees that determine how alerts flow from Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email.
Key features include routing tree visualization and validation before applying changes, automatic silence creation during maintenance windows with scheduled expiry, and inhibition rule management to suppress dependent alerts when root-cause alerts are already firing. The skill can analyze alert group patterns to suggest routing optimizations.
It supports match and match_re label-based routing, continue flags for multi-receiver fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver template customization using Go template syntax. Integration with Prometheus’s /api/v1/rules endpoint enables correlation between recording rules, alerting rules, and their AlertManager routing destinations for end-to-end observability pipeline verification.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)
