---
title: "Grafana Loki Log Correlation Agent"
description: "Queries Grafana Loki via the LogQL API to correlate log streams across services. Builds cross-service trace-to-log mappings using Tempo integration and generates alert rule suggestions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# Grafana Loki Log Correlation Agent

The Grafana Loki Log Correlation Agent skill queries distributed log data through the Loki HTTP API using LogQL expressions. It performs multi-stream correlation by joining log lines across services using shared trace IDs, request IDs, and timestamp windows. The skill leverages the Loki Series API to discover active label combinations and builds LogQL pipeline expressions with line_format, json, and regexp parsers for structured field extraction. It integrates with the Grafana Tempo API to create trace-to-log links, enabling seamless navigation between distributed traces and corresponding log entries. The agent analyzes log volume patterns using the Loki Stats API to identify unusual error rate spikes, generates Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions, and configures recording rules for frequently queried aggregations. Output includes correlated log summaries, suggested dashboard panels in JSON format, and LogQL query templates for common debugging scenarios.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/)
