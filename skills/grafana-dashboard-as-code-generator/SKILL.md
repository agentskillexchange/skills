---
name: "Grafana Dashboard as Code Generator"
slug: "grafana-dashboard-as-code-generator"
description: "Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries."
github_stars: 528
verification: "security_reviewed"
source: "https://github.com/grafana/grafonnet"
author: "Grafana"
category: "Monitoring & Alerts"
framework: "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafonnet"
  github_stars: 528
---

# Grafana Dashboard as Code Generator

Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries.

## Prerequisites

Grafonnet, Jsonnet, Grafana HTTP API, grafana-toolkit

## Installation

Basic usage or getting-started notes:
- Grafonnet uses the [Jsonnet](https://jsonnet.org/) programming language.
- **NOTE**: There is a significant performance issue with the C implementation of Jsonnet. You are strongly
- recommended to use the newer [go-jsonnet](https://github.com/google/go-jsonnet) Jsonnet implementation.

- Source: https://github.com/grafana/grafonnet
- Extracted from upstream docs: https://raw.githubusercontent.com/grafana/grafonnet/HEAD/README.md

## Documentation

- https://grafana.github.io/grafonnet/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)
