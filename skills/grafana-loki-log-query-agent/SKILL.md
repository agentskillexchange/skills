---
title: "Grafana Loki Log Query Agent"
description: "Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels."
verification: security_reviewed
source: "https://github.com/grafana/loki"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Query Agent

Queries Grafana Loki log aggregation system using LogQL via the Loki HTTP API. Filters log streams by labels, parses structured JSON logs, and correlates log entries with Grafana dashboard panels.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grafana-loki-log-query-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-loki-log-query-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grafana-loki-log-query-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)
