---
name: Prometheus AlertManager Rules Engine
description: Generates and validates Prometheus alerting rules and AlertManager routing
  configurations using the Prometheus HTTP API. Implements alert grouping, inhibition
  rules, and silence management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-rules-engine/
category:
- Monitoring &amp; Alerts
framework:
- Custom Agents
---
# Prometheus AlertManager Rules Engine

The Prometheus AlertManager Rules Engine skill creates comprehensive alerting configurations for Prometheus monitoring stacks. It queries the Prometheus HTTP API to analyze existing metric names, label cardinality, and recording rules before generating PromQL alert expressions with appropriate thresholds and for-durations. The skill generates AlertManager routing trees with receiver configurations for Slack, PagerDuty, and email notification channels, implementing proper grouping with group_by labels and group_wait/group_interval timing. It configures inhibition rules to suppress downstream alerts when upstream dependencies are already alerting, manages silence windows through the AlertManager Silence API for planned maintenance, and validates all generated rules using the promtool check rules command syntax. The engine analyzes historical alert firing patterns via the Prometheus Alerts API to recommend threshold adjustments that reduce alert fatigue while maintaining coverage for genuine incidents.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-rules-engine/)
