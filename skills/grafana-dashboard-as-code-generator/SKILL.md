---
title: "Grafana Dashboard as Code Generator"
description: "Generates Grafana dashboards programmatically using Grafonnet (jsonnet), the Grafana HTTP API, and grafana-toolkit. Supports multi-datasource panels with Prometheus, Loki, and Tempo queries."
verification: security_reviewed
source: "https://github.com/grafana/grafonnet"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafonnet"
  github_stars: 528
---

# Grafana Dashboard as Code Generator

The Grafana Dashboard as Code Generator creates production-quality Grafana dashboards using Grafonnet, the official Jsonnet library for Grafana dashboard generation. It produces version-controlled dashboard definitions that compile to Grafana JSON model format, supporting all panel types including time series, stat, gauge, table, heatmap, and geomap visualizations. The skill interfaces with the Grafana HTTP API for dashboard provisioning, folder management, and datasource configuration. It generates multi-datasource panels combining Prometheus metrics queries, Loki log queries with LogQL, and Tempo trace queries for unified observability dashboards. The generator uses grafana-toolkit for dashboard linting and validation, ensuring compliance with organizational standards for variable naming, panel sizing, and annotation configurations. It supports dashboard templating with Grafana variables for environment, cluster, and service selection, and implements row-level repeating for dynamic dashboard sections. The tool also configures alert rules using Grafana Alerting with proper notification policies and contact point routing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-as-code-generator/)
