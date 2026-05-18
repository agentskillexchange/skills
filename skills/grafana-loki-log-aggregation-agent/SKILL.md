---
name: "Grafana Loki Log Aggregation Agent"
slug: "grafana-loki-log-aggregation-agent"
description: "Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces."
github_stars: 27993
verification: "listed"
source: "https://github.com/grafana/loki"
category: "Monitoring & Alerts"
framework: "Gemini"
tool_ecosystem:
  github_repo: "grafana/loki"
  github_stars: 27993
---

# Grafana Loki Log Aggregation Agent

Configures Grafana Loki log pipelines with Promtail collectors and LogQL queries. Supports multi-tenant log routing, retention policies, and correlation with Grafana Tempo traces.

## Installation

Use the upstream install or setup path that matches your environment:
- $ git clone https://github.com/grafana/loki
- Alternatively, on Unix systems you can use make to build the binary, which adds additional arguments to the go build command.
- $ make loki

Requirements and caveats from upstream:
- [Docker Driver Client](https://grafana.com/docs/loki/latest/clients/docker-driver/) is a Docker plugin to send logs directly to Loki from Docker containers.

Basic usage or getting-started notes:
- does not do full text indexing on logs. By storing compressed, unstructured logs and only indexing metadata, Loki is simpler to operate and cheaper to run.
- [Installing Loki](https://grafana.com/docs/loki/latest/installation/)
- [Installing Alloy](https://grafana.com/docs/loki/latest/send-data/alloy/)

- Source: https://github.com/grafana/loki
- Extracted from upstream docs: https://raw.githubusercontent.com/grafana/loki/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-loki-log-aggregation-agent/)
