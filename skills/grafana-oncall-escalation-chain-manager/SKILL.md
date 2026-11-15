---
name: "Grafana OnCall Escalation Chain Manager"
slug: "grafana-oncall-escalation-chain-manager"
description: "Configures Grafana OnCall escalation chains, notification policies, and on-call schedules via the Grafana OnCall HTTP API. Manages integration routes from Alertmanager, Zabbix, and Datadog with automatic responder assignment."
github_stars: 3880
verification: "security_reviewed"
source: "https://github.com/grafana/oncall"
author: "grafana"
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "grafana/oncall"
  github_stars: 3880
---

# Grafana OnCall Escalation Chain Manager

Configures Grafana OnCall escalation chains, notification policies, and on-call schedules via the Grafana OnCall HTTP API. Manages integration routes from Alertmanager, Zabbix, and Datadog with automatic responder assignment.

## Installation

Use the upstream install or setup path that matches your environment:
- docker-compose pull && docker-compose up -d
- docker-compose pull engine
- docker-compose up -d

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/grafana/oncall)](https://hub.docker.com/r/grafana/oncall/tags)
- These instructions are for using Grafana 11 or newer. You must enable the feature toggle for
- externalServiceAccounts. This is already done for the docker files and helm charts. If you are running Grafana

Basic usage or getting-started notes:
- [!IMPORTANT]
- separately see the Grafana documentation on how to enable this.
- We prepared multiple environments:

- Source: https://github.com/grafana/oncall
- Extracted from upstream docs: https://raw.githubusercontent.com/grafana/oncall/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-oncall-escalation-chain-manager/)
