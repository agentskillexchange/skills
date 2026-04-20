---
title: Grafana Loki Log Query Agent
description: Queries Grafana Loki log aggregation system using LogQL via the Loki
  HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates
  log entries with Grafana dashboard panels.
verification: security_reviewed
source: https://github.com/grafana/loki
category:
- Monitoring &amp; Alerts
framework:
- MCP
tool_ecosystem:
  github_repo: grafana/loki
  github_stars: 27993
---

# Grafana Loki Log Query Agent

Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)
