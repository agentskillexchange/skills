---
title: "Grafana Unified Alerting Manager"
description: "Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances."
slug: "grafana-unified-alerting-manager"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-unified-alerting-manager/"
listed: true
---

# Grafana Unified Alerting Manager

Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances.

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
clawhub install grafana-unified-alerting-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Unified Alerting Manager skill provides full lifecycle management of alerting configurations across Grafana instances using the Grafana Alerting HTTP API. It creates and updates alert rules with PromQL, LogQL, or SQL expressions, configures contact points for email, Slack, PagerDuty, and webhook receivers, and manages notification policies with label-based routing trees. The skill supports alert rule provisioning via the Provisioning API for GitOps workflows, silence creation and expiry management, and mute timing configurations for maintenance windows. Features include bulk rule import/export in JSON and YAML formats, alert rule testing with sample data evaluation, and cross-instance rule synchronization for high-availability Grafana deployments. Integrates with Grafana OnCall API for escalation chain management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-unified-alerting-manager/)
