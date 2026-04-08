---
title: Grafana OnCall Escalation Chain Manager
description: The Grafana OnCall Escalation Chain Manager automates the configuration
  and maintenance of incident response workflows within Grafana OnCall. Using the
  Grafana OnCall HTTP API, it creates and updates escalation chains with multi-step
  notification policies that progress through Slack messages, phone calls, SMS alerts,
  and mobile push notifications based on acknowledgment timeouts. On-call schedule
  management handles rotation definitions with configurable shift lengths, override
  periods for holidays and planned absences, and handoff notifications between rotating
  team members. Integration routes are configured for alert sources including Prometheus
  Alertmanager, Zabbix, Datadog, and generic webhook endpoints, with routing rules
  that direct alerts to appropriate escalation chains based on severity labels, service
  ownership, and time-of-day routing policies. The manager implements automatic responder
  assignment using team membership and skill-based routing, ensuring database incidents
  reach DBAs and network issues reach infrastructure engineers. Alert grouping rules
  are configured to prevent notification storms during cascading failures by correlating
  related alerts into single incident timelines. Maintenance window scheduling temporarily
  adjusts escalation behavior during planned deployments, suppressing non-critical
  alerts while preserving emergency notification paths.
verification: security_reviewed
source: https://github.com/grafana/oncall
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
tool_ecosystem:
  github_repo: grafana/oncall
  github_stars: 3880
---

# Grafana OnCall Escalation Chain Manager

The Grafana OnCall Escalation Chain Manager automates the configuration and maintenance of incident response workflows within Grafana OnCall. Using the Grafana OnCall HTTP API, it creates and updates escalation chains with multi-step notification policies that progress through Slack messages, phone calls, SMS alerts, and mobile push notifications based on acknowledgment timeouts. On-call schedule management handles rotation definitions with configurable shift lengths, override periods for holidays and planned absences, and handoff notifications between rotating team members. Integration routes are configured for alert sources including Prometheus Alertmanager, Zabbix, Datadog, and generic webhook endpoints, with routing rules that direct alerts to appropriate escalation chains based on severity labels, service ownership, and time-of-day routing policies. The manager implements automatic responder assignment using team membership and skill-based routing, ensuring database incidents reach DBAs and network issues reach infrastructure engineers. Alert grouping rules are configured to prevent notification storms during cascading failures by correlating related alerts into single incident timelines. Maintenance window scheduling temporarily adjusts escalation behavior during planned deployments, suppressing non-critical alerts while preserving emergency notification paths.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-oncall-escalation-chain-manager/)
