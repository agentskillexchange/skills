---
title: "Grafana Loki Log Correlation Agent"
description: "Queries Grafana Loki via the LogQL API to correlate log streams across services. Builds cross-service trace-to-log mappings using Tempo integration and generates alert rule suggestions."
verification: "security_reviewed"
source: "https://github.com/grafana/loki"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
  license: "AGPL-3.0"
---

# Grafana Loki Log Correlation Agent

The Grafana Loki Log Correlation Agent skill queries distributed log data through the Loki HTTP API using LogQL expressions. It performs multi-stream correlation by joining log lines across services using shared trace IDs, request IDs, and timestamp windows. The skill leverages the Loki Series API to discover active label combinations and builds LogQL pipeline expressions with line_format, json, and regexp parsers for structured field extraction. It integrates with the Grafana Tempo API to create trace-to-log links, enabling seamless navigation between distributed traces and corresponding log entries. The agent analyzes log volume patterns using the Loki Stats API to identify unusual error rate spikes, generates Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions, and configures recording rules for frequently queried aggregations. Output includes correlated log summaries, suggested dashboard panels in JSON format, and LogQL query templates for common debugging scenarios.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/)
