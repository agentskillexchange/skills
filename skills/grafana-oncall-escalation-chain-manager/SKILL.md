---
name: "Grafana OnCall Escalation Chain Manager"
category: "Monitoring & Alerts"
verification: "security_reviewed"
source: "https://github.com/grafana/oncall"
tool_ecosystem:
  github_repo: "grafana/oncall"
  github_stars: 3880
---

# Grafana OnCall Escalation Chain Manager

Configures Grafana OnCall escalation chains, notification policies, and on-call schedules via the Grafana OnCall HTTP API. Manages integration routes from Alertmanager, Zabbix, and Datadog with automatic responder assignment.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install grafana-oncall-escalation-chain-manager

# OpenClaw CLI
openclaw skills install grafana-oncall-escalation-chain-manager

# Chat command
/skill install grafana-oncall-escalation-chain-manager

# Direct download
curl -L https://agentskillexchange.com/skills/grafana-oncall-escalation-chain-manager/download -o grafana-oncall-escalation-chain-manager.zip

# Git clone this repo and copy the skill folder
cp -r skills/grafana-oncall-escalation-chain-manager ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-oncall-escalation-chain-manager/)
