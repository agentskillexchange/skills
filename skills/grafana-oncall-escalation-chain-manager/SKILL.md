---
title: "Grafana OnCall Escalation Chain Manager"
description: "Configures Grafana OnCall escalation chains, notification policies, and on-call schedules via the Grafana OnCall HTTP API. Manages integration routes from Alertmanager, Zabbix, and Datadog with automatic responder assignment."
verification: "security_reviewed"
source: "https://github.com/grafana/oncall"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "grafana/oncall"
  github_stars: 3880
---

# Grafana OnCall Escalation Chain Manager

The Grafana OnCall Escalation Chain Manager automates the configuration and maintenance of incident response workflows within Grafana OnCall. Using the Grafana OnCall HTTP API, it creates and updates escalation chains with multi-step notification policies that progress through Slack messages, phone calls, SMS alerts, and mobile push notifications based on acknowledgment timeouts. On-call schedule management handles rotation definitions with configurable shift lengths, override periods for holidays and planned absences, and handoff notifications between rotating team members. Integration routes are configured for alert sources including Prometheus Alertmanager, Zabbix, Datadog, and generic webhook endpoints, with routing rules that direct alerts to appropriate escalation chains based on severity labels, service ownership, and time-of-day routing policies. The manager implements automatic responder assignment using team membership and skill-based routing, ensuring database incidents reach DBAs and network issues reach infrastructure engineers. Alert grouping rules are configured to prevent notification storms during cascading failures by correlating related alerts into single incident timelines. Maintenance window scheduling temporarily adjusts escalation behavior during planned deployments, suppressing non-critical alerts while preserving emergency notification paths.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-oncall-escalation-chain-manager/)
