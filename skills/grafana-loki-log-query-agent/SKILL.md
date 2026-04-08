---
title: Grafana Loki Log Query Agent
description: The Grafana Loki Log Query Agent skill enables Claude to search and analyze
  logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from
  natural language descriptions, handling both log stream selectors and log pipeline
  stages for filtering, parsing, and formatting. The skill supports label-based stream
  selection ({job=”api-server”, level=”error”}), line filter expressions for text
  matching, and parser stages for extracting structured fields from JSON, logfmt,
  and regex-patterned logs. It handles the Loki query range endpoint with configurable
  time windows and result limits. For incident investigation, the skill correlates
  log entries with Grafana dashboard panels by querying the Grafana API for dashboard
  JSON models and matching datasource references. This lets Claude explain which logs
  correspond to which visual anomalies on dashboards. Rate and volume queries using
  LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based
  alerting analysis without Prometheus. The skill manages Loki’s query timeout and
  chunk limits, splitting large time ranges into smaller windows for reliable retrieval.
  Authentication supports both API key and OAuth token methods. Built for DevOps teams
  running the Grafana/Loki/Promtail stack.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-loki-log-query-agent/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# Grafana Loki Log Query Agent

The Grafana Loki Log Query Agent skill enables Claude to search and analyze logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from natural language descriptions, handling both log stream selectors and log pipeline stages for filtering, parsing, and formatting. The skill supports label-based stream selection ({job=”api-server”, level=”error”}), line filter expressions for text matching, and parser stages for extracting structured fields from JSON, logfmt, and regex-patterned logs. It handles the Loki query range endpoint with configurable time windows and result limits. For incident investigation, the skill correlates log entries with Grafana dashboard panels by querying the Grafana API for dashboard JSON models and matching datasource references. This lets Claude explain which logs correspond to which visual anomalies on dashboards. Rate and volume queries using LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based alerting analysis without Prometheus. The skill manages Loki’s query timeout and chunk limits, splitting large time ranges into smaller windows for reliable retrieval. Authentication supports both API key and OAuth token methods. Built for DevOps teams running the Grafana/Loki/Promtail stack.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)
