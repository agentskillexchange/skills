---
title: "Netdata Real-Time Infrastructure Monitoring and Alerting"
description: "Netdata is an open-source observability platform for real-time metrics, anomaly detection, and alerting across servers, containers, databases, and cloud services. This skill helps agents install Netdata, connect nodes, inspect dashboards, and route alerts using the project’s documented collectors, streaming, and cloud integrations."
verification: "security_reviewed"
source: "https://github.com/netdata/netdata"
author: "netdata"
publisher_type: "Company"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "netdata/netdata"
  github_stars: 78430
---

# Netdata Real-Time Infrastructure Monitoring and Alerting

Netdata is an open-source observability platform for real-time metrics, anomaly detection, and alerting across servers, containers, databases, and cloud services. This skill helps agents install Netdata, connect nodes, inspect dashboards, and route alerts using the project’s documented collectors, streaming, and cloud integrations.

## Prerequisites

Linux, Docker or Kubernetes environment for deployment; optional Netdata Cloud account for centralized dashboards; alert destinations such as email, Slack, Discord, PagerDuty, or Telegram.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

## Documentation

- https://learn.netdata.cloud

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/netdata-real-time-infrastructure-monitoring-and-alerting/)
