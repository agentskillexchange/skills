---
name: "Grafana Unified Alerting Manager"
description: "Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-unified-alerting-manager/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
---

# Grafana Unified Alerting Manager

The Grafana Unified Alerting Manager skill provides full lifecycle management of alerting configurations across Grafana instances using the Grafana Alerting HTTP API. It creates and updates alert rules with PromQL, LogQL, or SQL expressions, configures contact points for email, Slack, PagerDuty, and webhook receivers, and manages notification policies with label-based routing trees. The skill supports alert rule provisioning via the Provisioning API for GitOps workflows, silence creation and expiry management, and mute timing configurations for maintenance windows. Features include bulk rule import/export in JSON and YAML formats, alert rule testing with sample data evaluation, and cross-instance rule synchronization for high-availability Grafana deployments. Integrates with Grafana OnCall API for escalation chain management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-unified-alerting-manager/)
