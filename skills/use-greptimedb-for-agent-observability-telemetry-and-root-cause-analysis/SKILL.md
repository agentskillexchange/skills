---
name: "Use GreptimeDB for agent observability telemetry and root cause analysis"
slug: "use-greptimedb-for-agent-observability-telemetry-and-root-cause-analysis"
description: "Store OpenTelemetry metrics, logs, traces, and GenAI telemetry in one queryable backend so agents can correlate incidents and root-cause signals with SQL or PromQL."
github_stars: 6683
verification: "security_reviewed"
source: "https://github.com/GreptimeTeam/greptimedb"
author: "GreptimeTeam"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "GreptimeTeam/greptimedb"
  github_stars: 6683
---

# Use GreptimeDB for agent observability telemetry and root cause analysis

Store OpenTelemetry metrics, logs, traces, and GenAI telemetry in one queryable backend so agents can correlate incidents and root-cause signals with SQL or PromQL.

## Prerequisites

GreptimeDB, OpenTelemetry Collector or compatible telemetry pipeline, SQL or PromQL query access, optional Grafana or Greptime dashboard

## Installation

Install or set up from the source-backed instructions:

Follow the GreptimeDB installation guide for Docker, binary, or Kubernetes deployment, configure OpenTelemetry or Prometheus/Loki/Elasticsearch-compatible ingestion, then give the agent the documented GreptimeDB skill instructions at https://docs.greptime.com/SKILL.md before it queries telemetry.

- Source: https://github.com/GreptimeTeam/greptimedb

## Documentation

- https://docs.greptime.com/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-greptimedb-for-agent-observability-telemetry-and-root-cause-analysis/)
