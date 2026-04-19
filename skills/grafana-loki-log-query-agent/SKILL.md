---
title: "Grafana Loki Log Query Agent"
description: "The Grafana Loki Log Query Agent skill enables Claude to search and analyze logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from natural language descriptions, handling both log stream selectors and log pipeline stages for filtering, parsing, and formatting. The skill supports label-based stream selection ({job=&#8221;api-server&#8221;, level=&#8221;error&#8221;}), line filter expressions for text matching, and parser stages for extracting structured fields from JSON, logfmt, and regex-patterned logs. It handles the Loki query range endpoint with configurable time windows and result limits. For incident investigation, the skill correlates log entries with Grafana dashboard panels by querying the Grafana API for dashboard JSON models and matching datasource references. This lets Claude explain which logs correspond to which visual anomalies on dashboards. Rate and volume queries using LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based alerting analysis without Prometheus. The skill manages Loki&#8217;s query timeout and chunk limits, splitting large time ranges into smaller windows for reliable retrieval. Authentication supports both API key and OAuth token methods. Built for DevOps teams running the Grafana/Loki/Promtail stack."
source: "https://github.com/grafana/loki"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Query Agent

The Grafana Loki Log Query Agent skill enables Claude to search and analyze logs stored in Grafana Loki through its HTTP API. It constructs LogQL queries from natural language descriptions, handling both log stream selectors and log pipeline stages for filtering, parsing, and formatting. The skill supports label-based stream selection ({job=&#8221;api-server&#8221;, level=&#8221;error&#8221;}), line filter expressions for text matching, and parser stages for extracting structured fields from JSON, logfmt, and regex-patterned logs. It handles the Loki query range endpoint with configurable time windows and result limits. For incident investigation, the skill correlates log entries with Grafana dashboard panels by querying the Grafana API for dashboard JSON models and matching datasource references. This lets Claude explain which logs correspond to which visual anomalies on dashboards. Rate and volume queries using LogQL metric expressions (rate, count_over_time, bytes_over_time) enable log-based alerting analysis without Prometheus. The skill manages Loki&#8217;s query timeout and chunk limits, splitting large time ranges into smaller windows for reliable retrieval. Authentication supports both API key and OAuth token methods. Built for DevOps teams running the Grafana/Loki/Promtail stack.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-query-agent/)
