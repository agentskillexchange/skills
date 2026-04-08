---
title: Grafana Loki Log Correlation Agent
description: The Grafana Loki Log Correlation Agent skill queries distributed log
  data through the Loki HTTP API using LogQL expressions. It performs multi-stream
  correlation by joining log lines across services using shared trace IDs, request
  IDs, and timestamp windows. The skill leverages the Loki Series API to discover
  active label combinations and builds LogQL pipeline expressions with line_format,
  json, and regexp parsers for structured field extraction. It integrates with the
  Grafana Tempo API to create trace-to-log links, enabling seamless navigation between
  distributed traces and corresponding log entries. The agent analyzes log volume
  patterns using the Loki Stats API to identify unusual error rate spikes, generates
  Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions,
  and configures recording rules for frequently queried aggregations. Output includes
  correlated log summaries, suggested dashboard panels in JSON format, and LogQL query
  templates for common debugging scenarios.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---

# Grafana Loki Log Correlation Agent

The Grafana Loki Log Correlation Agent skill queries distributed log data through the Loki HTTP API using LogQL expressions. It performs multi-stream correlation by joining log lines across services using shared trace IDs, request IDs, and timestamp windows. The skill leverages the Loki Series API to discover active label combinations and builds LogQL pipeline expressions with line_format, json, and regexp parsers for structured field extraction. It integrates with the Grafana Tempo API to create trace-to-log links, enabling seamless navigation between distributed traces and corresponding log entries. The agent analyzes log volume patterns using the Loki Stats API to identify unusual error rate spikes, generates Grafana alerting rule YAML for Cortex/Mimir ruler compatible alert definitions, and configures recording rules for frequently queried aggregations. Output includes correlated log summaries, suggested dashboard panels in JSON format, and LogQL query templates for common debugging scenarios.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-correlation-agent-2/)
